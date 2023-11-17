from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class OperationsTypes(str, Enum):
    concatenate = 'concatenate'
    lower_case = 'lower_case'
    upper_case = 'upper_case'
    split_by = 'split_by'
    replace_by = 'replace_by'
    strip_spaces = 'strip_spaces'


class OperationItem(BaseModel):
    operation: OperationsTypes = Field(
        description='Operation to perform. Options: `concatenate`, `lower_case`, `upper_case`, `split_by`, `replace_by`.',
        json_schema_extra={
            "from_upstream": "never"
        }
    )
    second_argument: str = Field(
        default='',
        description='Value for the second argument.',
    )
    auxiliary_argument: str = Field(
        default='',
        description="""Auxiliary argument for `split_by` and `replace_by` operations.
If `split_by` is selected, this argument will be used as the index of the split array.
If `replace_by` is selected, this argument will be used as the string to replace.
""",
    )


class InputModel(BaseModel):
    first_argument: str = Field(
        description='Value for the first argument.',
    )
    operations: List[OperationItem] = Field(
        description='Sequence of operations to perform.',
    )


class OutputModel(BaseModel):
    output_string: str = Field(
        description='Output string.',
    )
