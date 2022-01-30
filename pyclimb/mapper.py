"""
The grade conversion implementation.

Each item of the mapper (dictionary) is a conversion path with:

  - key following the naming convention "A2B" (`A` is the input grading, `B` is the output grading)
  - value being the mapping from an `A` grade to a `B` grade.
  
Note that an "A2B" mapping is not bijective.
"""

mapper = {
    "French2YDS": {
        "1a": "N/A",
        "1a+": "N/A",
        "1b": "N/A",
        "1b+": "N/A",
        "1c": "5.0",
        "1c+": "5.0",
        "2a": "5.1",
        "2a+": "5.1",
        "2b": "5.1",
        "2b+": "5.2",
        "2c": "5.2",
        "2c+": "5.3",
        "3a": "5.3",
        "3a+": "5.4",
        "3b": "5.4",
        "3b+": "5.4",
        "3c": "5.5",
        "3c+": "5.5",
        "4a": "5.6",
        "4a+": "5.6",
        "4b": "5.6",
        "4b+": "5.7",
        "4c": "5.7",
        "4c+": "5.8",
        "5a": "5.8",
        "5a+": "5.8",
        "5b": "5.9",
        "5b+": "5.9",
        "5c": "5.10a",
        "5c+": "5.10a",
        "6a": "5.10a",
        "6a+": "5.10b",
        "6b": "5.10c",
        "6b+": "5.10d",
        "6c": "5.11b",
        "6c+": "5.11c",
        "7a": "5.11d",
        "7a+": "5.12a",
        "7b": "5.12b",
        "7b+": "5.12c",
        "7c": "5.12d",
        "7c+": "5.13a",
        "8a": "5.13b",
        "8a+": "5.13c",
        "8b": "5.13d",
        "8b+": "5.14a",
        "8c": "5.14b",
        "8c+": "5.14c",
        "9a": "5.14d",
        "9a+": "5.15a",
        "9b": "5.15b",
        "9b+": "5.15c",
        "9c": "5.15d",
    },
    "YDS2French": {
        "5.0": "1c+",
        "5.1": "2a+",
        "5.2": "2b+",
        "5.3": "3a",
        "5.4": "3b",
        "5.5": "3c+",
        "5.6": "4a+",
        "5.7": "4c",
        "5.8": "5a",
        "5.9": "5b+",
        "5.10a": "5c+",
        "5.10b": "6a+",
        "5.10c": "6b",
        "5.10d": "6b+",
        "5.11a": "6c",
        "5.11b": "6c+",
        "5.11c": "6c+",
        "5.11d": "7a",
        "5.12a": "7a+",
        "5.12b": "7b",
        "5.12c": "7b+",
        "5.12d": "7c",
        "5.13a": "7c+",
        "5.13b": "8a",
        "5.13c": "8a+",
        "5.13d": "8b",
        "5.14a": "8b+",
        "5.14b": "8c",
        "5.14c": "8c+",
        "5.14d": "9a",
        "5.15a": "9a+",
        "5.15b": "9b",
        "5.15c": "9b+",
        "5.15d": "9c",
    },
}


def get_conversion(from_system: str, to_system: str) -> str:
    """Heuristic method to obtain conversion path."""
    return f"{from_system}2{to_system}"