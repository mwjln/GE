"""
This is a template for creating custom SetBasedColumnMapExpectations.
For detailed instructions on how to use it, please see:
    https://docs.greatexpectations.io/docs/guides/expectations/creating_custom_expectations/how_to_create_custom_set_based_column_map_expectations
"""

from great_expectations.expectations.set_based_column_map_expectation import (
    SetBasedColumnMapExpectation,
)


# <snippet>
# This class defines the Expectation itself
class ExpectColumnValuesToBeInNaicsCodeSet(SetBasedColumnMapExpectation):
    """Values in this column should be valid values from North American Industry Classification System. Source: https://www.census.gov/naics/?48967"""

    # These values will be used to configure the metric created by your expectation
    set_ = []

    set_camel_name = "SetName"
    set_semantic_name = None

    # These examples will be shown in the public gallery.
    # They will also be executed as unit tests for your Expectation.
    # Additional test - random/wrong number codes e.g.112123; 31; 41 
    examples = [
    {
        "data": {
            "2022 NAICS US Code, String": [
                "11",
                "21",
                "311",
                "42",
                "51",
            ],
            "2022 NAICS US Code, Float": [
                11.0,
                21.0,
                311.0,
                42.0,
                51.0,
            ],
            "2022 NAICS US Code, Integer": [
                11,
                21,
                311,
                42,
                51,
            ],
        },
        "tests": [
            {
                "title": "positive_test_integer",
                "exact_match_out": False,
                "in": {"column": "2022 NAICS US Code, Integer"},
                "out": {
                    "success": True,
                },
                "include_in_gallery": True,
            },
            {
                "title": "negative_test",
                "exact_match_out": False,
                "in": {"column": "2022 NAICS US Code, String"},
                "out": {
                    "success": False,
                    "unexpected_index_list": [1,3,5,7],
                },
                "include_in_gallery": True,
            },
            {
                "title": "positive_test_float",
                "exact_match_out": False,
                "in": {"column": "2022 NACIS US Code, Float"},
                "out": {
                    "success": True,
                },
                "include_in_gallery": True,
            },
        ],
        "test_backends": [
            {
                "backend": "pandas",
                "dialects": None,
            },
            {
                "backend": "sqlalchemy",
                "dialects": ["sqlite", "postgresql"],
            },
            {
                "backend": "spark",
                "dialects": None,
            },
        ],
        }
    ]

    # Here your regex is used to create a custom metric for this expectation
    map_metric = SetBasedColumnMapExpectation.register_metric(
        set_camel_name=set_camel_name,
        set_=set_,
    )

    # This object contains metadata for display in the public Gallery
    library_metadata = {
        "tags": ["set-based"],  # Tags for this Expectation in the Gallery
        "contributors": [  # Github handles for all contributors to this Expectation.
            "@your_name_here",  # Don't forget to add your github handle here!
        ],
    }


# </snippet>
if __name__ == "__main__":
    ExpectColumnValuesToBeInNaicsCodeSet().print_diagnostic_checklist()
