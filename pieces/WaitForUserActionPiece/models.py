from pydantic import BaseModel, Field
from enum import Enum


class DefaultActionType(str, Enum):
    continue_ = "continue"
    stop = "stop"


class ProviderType(str, Enum):
    gmail = "gmail"
    outlook = "outlook"
    office365 = "office365"
    yahoo = "yahoo"


class InputModel(BaseModel):
    """
    WaitForUserAction Input Model
    """
    context: str = Field(
        default="",
        description="Context to be sent to user."
    )
    timeout: int = Field(
        default=36000,
        description="Timeout in seconds to wait for user action."
    )
    default_action: str = Field(
        default=DefaultActionType.continue_,
        description="Default action to be taken if timeout is reached."
    )
    email_provider: ProviderType = Field(
        description='The email provider to use.',
        default=ProviderType.gmail
    )
    email_receivers: str = Field(
        description='The receivers of the email, as comma-separated values.'
    )


class OutputModel(BaseModel):
    """
    WaitForUserAction Output Model
    """
    user_action: str = Field(
        description="User action."
    )


class SecretsModel(BaseModel):
    """
    WaitForUserAction Secrets Model
    """
    AWS_ACCESS_KEY_ID: str = Field(
        description="AWS Access Key ID."
    )
    AWS_SECRET_ACCESS_KEY: str = Field(
        description="AWS Secret Access Key."
    )
    AWS_REGION: str = Field(
        description="AWS Region."
    )
    EMAIL_SENDER_ACCOUNT: str = Field(
        description="The email sender account."
    )
    EMAIL_SENDER_PASSWORD: str = Field(
        description="The email sender password"
    )