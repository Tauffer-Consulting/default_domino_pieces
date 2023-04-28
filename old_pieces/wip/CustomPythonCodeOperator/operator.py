from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel, InputKwargsModel, OutputKwargsModel


class CustomPythonCodeOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):

        input_kwargs = input_model.input_kwargs
        input_dict = {kwarg.key: kwarg.value for kwarg in input_kwargs}
        output_kwargs = input_model.output_kwargs
        output_dict = {kwarg.key: kwarg.key for kwarg in output_kwargs}
        code = input_model.code

        # TODO: Implement save code to custom_code.py file and run it
        code_str = f"""
def custom_function(**{input_dict}):
    {code}
    return {output_dict}

if __name__ == '__main__':
    custom_function()
"""
        
        # TODO: Implement capture output kwargs

        msg = ""

        # TODO: Maybe we should not use a pre-defined OutputModel here,
        # but instead create a new OutputModel for each output_kwargs case
        return OutputModel(
            message=msg,
            output_kwargs=""
        )