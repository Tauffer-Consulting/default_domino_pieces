from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from datetime import datetime
from pathlib import Path
from email.message import EmailMessage
import ssl
import smtplib
import os
import re
import subprocess
import requests


class WaitForUserActionPiece(BasePiece):

    def piece_function(self, input_model: InputModel):
        # Prepare AWS credentials
        config_data = f"""[default]
aws_access_key_id={os.environ.get("AWS_ACCESS_KEY_ID")}
aws_secret_access_key={os.environ.get("AWS_SECRET_ACCESS_KEY")}
region={os.environ.get("AWS_REGION")}
"""
        home_directory = Path.home()
        aws_directory = home_directory / ".aws"
        aws_directory.mkdir(parents=True, exist_ok=True)
        config_file = aws_directory / "config"        
        with open(config_file, "w") as file:
            file.write(config_data)
        
        # Create Chalice app files
        result = subprocess.run(
            ["chalice", "new-project", "user_action_app"],
            cwd=str(home_directory), 
            capture_output=True, 
            text=True
        )
        app_directory = home_directory / "user_action_app"
        app_file = app_directory / "app.py"
        with open(app_file, "w") as file:
            file.write(app_string)
        
        # Deploy Chalice app
        try:
            result = subprocess.run(
                ["chalice", "deploy"],
                cwd=str(app_directory),
                capture_output=True,
                text=True
            )
            # Extract the deployment URL from the command output
            output = result.stdout
            match = re.search(r'URL: (https?://\S+)', output)
            if match:
                deployment_url = match.group(1)
            else:
                raise Exception(f"Chalice deployment URL could not be found in output: {output}")
        except subprocess.CalledProcessError as e:
            print(f"Chalice deployment failed. Error: {e}")
            raise Exception(f"Chalice deployment failed. Error: {e}")
        
        # Assemble information and send to user email
        workflow_name = "TODO - get workflow name"
        continue_url = f"{deployment_url}/continue"
        stop_url = f"{deployment_url}/stop"
        email_body = f"""<h1>Wait For User Action</h1>
<p>Workflow: {workflow_name}</p>
<p>Timestamp: {datetime.now().isoformat()}</p>
<p>Context: {input_model.context}</p>
<br>
<p>Workflow is waiting for user action</p>
<p>Continue URL: <a href="{continue_url}">Click here to continue the Workflow</a></p>
<p>Stop URL: <a href="{stop_url}">Click here to stop the Workflow</a></p>
"""
        email_account = self.secrets.EMAIL_SENDER_ACCOUNT
        email_password = self.secrets.EMAIL_SENDER_PASSWORD
        email_server = email_servers[input_model.email_provider]
        email_receivers = [r.strip() for r in input_model.email_receivers.split(",")]
        email_subject = input_model.email_subject
        email_message = EmailMessage()
        email_message["From"] = email_account
        email_message["To"] = email_receivers
        email_message["Subject"] = email_subject
        email_message.set_content(email_body)
        context = ssl.create_default_context()
        self.logger.info("Sending email...")
        try:
            with smtplib.SMTP_SSL(email_server, 465, context=context) as service:
                service.login(email_account, email_password)
                service.sendmail(email_account, email_receivers, email_message.as_string())
            self.logger.info("Email sent successfully")
        except Exception as e:
            self.logger.error(f"Email sending failed. Error: {e}")
            raise Exception(f"Email sending failed. Error: {e}")

        # Loop until user action happens, or until timeout
        # Probe user action every 5 seconds
        timeout = input_model.timeout
        start_time = datetime.now()
        while True:
            # Check if timeout has been reached
            current_time = datetime.now()
            elapsed_time = current_time - start_time
            if elapsed_time.total_seconds() > timeout:
                message = f"Timeout reached: {timeout} seconds"
                self.user_action = input_model.default_action
                break
            # Check if user action has happened
            try:
                response = requests.get(f"{deployment_url}/user-action")
                user_action = response.json()["user_action"]
                if user_action == "continue":
                    self.logger.info("User action: continue")
                    self.user_action = "continue"
                    break
                elif user_action == "stop":
                    self.logger.info("User action: stop")
                    self.user_action = "stop"
                    break
                elif user_action == "waiting":
                    self.logger.info("No user action taken yet. We'll keep waiting...")
            except Exception as e:
                self.logger.error(f"Error while probing user action. Error: {e}")
                raise Exception(f"Error while probing user action. Error: {e}")

        # Delete Chalice app
        try:
            result = subprocess.run(
                ["chalice", "delete"],
                cwd=str(app_directory),
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Chalice deletion failed. Error: {e}")
            raise Exception(f"Chalice deletion failed. Error: {e}")

        # Return output
        return OutputModel(
            user_action=self.user_action
        )
    

# Chalice app, which will write the user action to S3 and read it from there
app_string = """
import boto3
from chalice import Chalice

BUCKET_NAME = {template_bucket_name}
USER_ACTION_KEY = 'user-action'

app = Chalice(app_name='user_action_app')
s3_client = boto3.client('s3')

def set_user_action(user_action):
    s3_client.put_object(
        Body=user_action,
        Bucket=BUCKET_NAME,
        Key=USER_ACTION_KEY
    )

def get_user_action():
    try:
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=USER_ACTION_KEY)
        user_action = response['Body'].read().decode('utf-8')
        return user_action
    except s3_client.exceptions.NoSuchKey:
        return 'waiting'

@app.route('/user-action', methods=['GET'])
def user_action():
        # Retrieve user_action from S3
        user_action = get_user_action()
        return {{'user_action': user_action}}

@app.route('/continue', methods=['GET'])
def continue_():
    # Store user_action in S3
    set_user_action('continue')
    return {{'message': 'User action set successfully: continue'}}

@app.route('/stop', methods=['GET'])
def stop():
    # Store user_action in S3
    set_user_action('stop')
    return {{'message': 'User action set successfully: stop'}}
"""

# Email servers
email_servers = {
    "gmail": "smtp.gmail.com",
    "outlook": "smtp-mail.outlook.com",
    "office365": "smtp.office365.com",
    "yahoo": "smtp.mail.yahoo.com",
}