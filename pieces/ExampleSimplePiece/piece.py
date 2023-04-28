from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import os

import numpy as np


class ExampleSimplePiece(BasePiece):
    """
    This Piece serves as a simple example, from where you can start writing your own Piece.
    Remember to also change all other required files accordingly:
    - piece.py (this file)
    - models.py
    - metadata.json
    - requirements.txt or Dockerfile if needed
    """
    
    def piece_function(self, input_model: InputModel):

        # Input arguments are retrieved from the Input model object
        distribution_name = input_model.distribution_name
        distribution_mean = input_model.distribution_mean
        distribution_sd = input_model.distribution_sd

        # If this Piece needs to use a Secret value, it can retrieve it from ENV
        piece_secret = os.environ.get("EXAMPLE_OPERATOR_SECRET_1", None)

        # Basic logging is done with print()
        print("Starting sampling process...")

        # Here we add the Piece function logic
        message = ""
        if distribution_name == "gaussian":
            sample_result = np.random.normal(distribution_mean, distribution_sd)

        elif distribution_name == "poisson":
            if distribution_mean < 0:
                distribution_mean = abs(distribution_mean)
                message += "\n"
                message += "Poisson distributions only accept positive mean values. Applying abs() to the value received."
            sample_result = np.random.poisson(distribution_mean)

        print(f"Sampled from a gaussian distribution with mean={distribution_mean} and sd={distribution_sd}")
        message += "\n"
        message += "Sampling operation was successful!"

        # Finally, results should return as an Output model
        return OutputModel(
            message=message,
            sample_result=sample_result
        )