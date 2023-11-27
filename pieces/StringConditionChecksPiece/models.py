from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class ChecksTypes(str, Enum):
    contains_case_sensitive = 'contains_case_sensitive'
    contains_case_insensitive = 'contains_case_insensitive'
    length_greater_than = 'length_greater_than'
    length_greater_than_or_equal_to = 'length_greater_than_or_equal_to'
    length_less_than = 'length_less_than'
    length_less_than_or_equal_to = 'length_less_than_or_equal_to'
    length_equal_to = 'length_equal_to'
    regex_match = 'regex_match'


class LogicalOperators(str, Enum):
    and_operator = 'and'
    or_operator = 'or'


class OperationItem(BaseModel):
    operation: ChecksTypes = Field(
        description="""Operation to perform.
Options: `contains_case_sensitive`, `contains_case_insensitive`, `length_greater_than`, `length_greater_than_or_equal_to`, `length_less_than`, `length_less_than_or_equal_to`, `length_equal_to`, `regex_match`.
""",
        json_schema_extra={
            "from_upstream": "never"
        }
    )
    second_argument: str = Field(
        default='',
        description="""Value for the second argument.
If `contains_case_sensitive` or `contains_case_insensitive` are selected, this argument will be used as the string to search for.
If `length_greater_than`, `length_greater_than_or_equal_to`, `length_less_than`, `length_less_than_or_equal_to` or `length_equal_to` are selected, this argument will be used as the integer value to compare with.
If `regex_match` is selected, this argument will be used as the string to match with the regex pattern.
""",
    )
    next_logical_operator: LogicalOperators = Field(
        default=LogicalOperators.and_operator,
        description="Logical operator to use with the next operation result.",
    )


class InputModel(BaseModel):
    input_string: str = Field(
        description='Input string.',
    )
    operations: List[OperationItem] = Field(
        description='Sequence of operations to perform.',
    )


class OutputModel(BaseModel):
    check_result: bool = Field(
        description='Result of the checks.',
    )
