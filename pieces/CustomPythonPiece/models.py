from pydantic import BaseModel, Field, Extra
from domino.models import OutputModifierModel, OutputModifierItemType
from typing import List, Union


class InputKwargsModel(BaseModel):
    kwarg_name: str = Field(
        default=None,
        description='Argument name.',
        from_upstream="never"
    )
    kwarg_value: Union[str, list, int, float, bool, dict] = Field(
        default=None,
        description='Argument value.',
        from_upstream="always"
    )


class InputModel(BaseModel):
    """
    CustomPythonPiece Input Model
    """
    
    input_args: List[InputKwargsModel] = Field(
        default=[
            InputKwargsModel(kwarg_value="", kwarg_name="kwarg_2"),
            InputKwargsModel(kwarg_value="", kwarg_name="kwarg_1"),
        ],
        description='Input arguments.',
        from_upstream="never",
    )
    script: str = Field(
        default="""# Do not modify the function definition line 
def custom_function(kwarg_1, kwarg_2):
    # Write your code here
    print(f"First argument: {kwarg_1}")
    print(f"Second argument: {kwarg_2}")

    # Return the output of the function as an object,
    # Matching the Output Args defined in the Form below
    return {
        "output_1": "this is a string", 
        "output_2": 420
    }
""",
        description='Python script.',
        widget="codeeditor",
        from_upstream="never"
    )
    output_args: List[OutputModifierModel] = Field(
        default=[
            OutputModifierModel(name="output_1", type=OutputModifierItemType.string, description="An example string output"),
            OutputModifierModel(name="output_2", type=OutputModifierItemType.integer, description="An example integer output"),
        ],
        description='Output arguments.',
        from_upstream="never"
    )


class OutputModel(BaseModel, extra=Extra.allow):
    """
    CustomPythonPiece Output Model
    """
    # ref: https://stackoverflow.com/a/75381426/11483674
    pass


if __name__ == '__main__':
    model = InputModel.schema_json()
    print(model)