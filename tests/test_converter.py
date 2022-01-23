import pytest

import pyclimb


class TestConverter:

    french2yds_map = [
        ("1a", "N/A"),
        ("1a+", "N/A"),
        ("1b", "N/A"),
        ("1b+", "N/A"),
        ("1c", "5.0"),
        ("1c+", "5.0"),
        ("2a", "5.1"),
        ("2a+", "5.1"),
        ("2b", "5.1"),
        ("2b+", "5.2"),
        ("2c", "5.2"),
        ("2c+", "5.3"),
        ("3a", "5.3"),
        ("3a+", "5.4"),
        ("3b", "5.4"),
        ("3b+", "5.4"),
        ("3c", "5.5"),
        ("3c+", "5.5"),
        ("4a", "5.6"),
        ("4a+", "5.6"),
        ("4b", "5.6"),
        ("4b+", "5.7"),
        ("4c", "5.7"),
        ("4c+", "5.8"),
        ("5a", "5.8"),
        ("5a+", "5.8"),
        ("5b", "5.9"),
        ("5b+", "5.9"),
        ("5c", "5.10a"),
        ("5c+", "5.10a"),
        ("6a", "5.10a"),
        ("6a+", "5.10b"),
        ("6b", "5.10c"),
        ("6b+", "5.10d"),
        ("6c", "5.11b"),
        ("6c+", "5.11c"),
        ("7a", "5.11d"),
        ("7a+", "5.12a"),
        ("7b", "5.12b"),
        ("7b+", "5.12c"),
        ("7c", "5.12d"),
        ("7c+", "5.13a"),
        ("8a", "5.13b"),
        ("8a+", "5.13c"),
        ("8b", "5.13d"),
        ("8b+", "5.14a"),
        ("8c", "5.14b"),
        ("8c+", "5.14c"),
        ("9a", "5.14d"),
        ("9a+", "5.15a"),
        ("9b", "5.15b"),
        ("9b+", "5.15c"),
        ("9c", "5.15d"),
    ]

    def test_convert_with_unrecognized_grading_system(self):

        with pytest.raises(pyclimb.exceptions.GradeConversionError) as exc:
            pyclimb.convert("6a+", to="foo")

        assert "`to` is not a recognized grading system" in str(exc.value)

    def test_convert_with_unrecognized_grade(self):

        with pytest.raises(pyclimb.exceptions.GradeConversionError) as exc:
            pyclimb.convert(grade="foo bar", to="YDS")

        assert "`grade` not recognized" in str(exc.value)

    @pytest.mark.parametrize("grade, converted_grade", french2yds_map)
    def test_convert_french_to_yds(self, grade, converted_grade):

        assert pyclimb.convert(grade=grade, to="YDS") == converted_grade
