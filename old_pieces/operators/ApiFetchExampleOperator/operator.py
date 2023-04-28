import requests
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import json


class ApiFetchExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # Return 20 records for a location id sorted by rating.
        secret_msg = f"""
        Secrets: {self.secrets}
        """
        self.logger.info(secret_msg)

        msg = "Fetching data for {}".format(input_model.dict())
        self.logger.info(msg)

        url = "https://airbnb19.p.rapidapi.com/api/v1/searchPropertyByPlace"
        querystring = {
            "id":input_model.airbnb_location_id, 
            "totalRecords":"20", 
            "currency": input_model.currency, 
            "adults": input_model.adults
        }
        headers = {
            "X-RapidAPI-Key": self.secrets.API_KEY,
            "X-RapidAPI-Host": "airbnb19.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_dict = json.loads(response.text)

        output = []
        for e in response_dict.get('data'):
            aux = {
                "rate": float(e.get('avgRating')),
                "beds": e.get('beds'),
                "city": e.get('city'),
                "price": e.get('price')
            }
            output.append(aux)
        output = sorted(output, key=lambda d: d['rate'], reverse=True)
        self.logger.info(output)

        return OutputModel(
            data=output,
            message="Task completed"
        )