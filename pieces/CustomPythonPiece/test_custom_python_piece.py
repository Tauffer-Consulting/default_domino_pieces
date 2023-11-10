from domino.testing import piece_dry_run


def test_custom_python_piece():
    script = """def custom_function(kwarg_1, kwarg_2):
    # Write your code here
    print(f"First argument: {kwarg_1}")
    print(f"Second argument: {kwarg_2}")

    # Return the output of the function as an object,
    # Matching the Output Args defined in the Form below
    return {
        "output_1": kwarg_1 + " + extra string",
        "output_2": kwarg_2 + 10
    }
"""
    input_data = dict(
        input_args=[
            dict(kwarg_value="string", kwarg_name="kwarg_1"),
            dict(kwarg_value=420, kwarg_name="kwarg_2"),
        ],
        script=script,
        output_args=[
            dict(name="output_1", type="string", description="An example string output"),
            dict(name="output_2", type="integer", description="An example integer output"),
        ]
    )

    piece_output = piece_dry_run(
        piece_name="CustomPythonPiece",
        input_data=input_data
    )

    assert "output_1" in piece_output
    assert "output_2" in piece_output
    assert piece_output["output_1"] == "string + extra string"
    assert piece_output["output_2"] == 430
