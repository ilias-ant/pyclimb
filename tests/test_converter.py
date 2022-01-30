import pytest

import pyclimb


class TestConverter:
    def test_convert_with_unrecognized_output_grading_system(self):

        with pytest.raises(pyclimb.exceptions.GradeConversionError) as exc:
            pyclimb.convert("6a+", grade_system="French", to="bar")

        assert "bar is not a recognized grading system" in str(exc.value)

    def test_convert_with_unrecognized_input_grading_system(self):

        with pytest.raises(pyclimb.exceptions.GradeConversionError) as exc:
            pyclimb.convert("6a+", grade_system="foo", to="YDS")

        assert "foo is not a recognized grading system" in str(exc.value)

    def test_convert_with_unrecognized_grade(self):

        with pytest.raises(pyclimb.exceptions.GradeConversionError) as exc:
            pyclimb.convert(grade="foo", grade_system="French", to="YDS")

        assert "foo not recognized" in str(exc.value)


class TestConverterFrenchToYDS:

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

    @pytest.mark.parametrize("grade, converted_grade", french2yds_map)
    def test_convert_french_to_yds(self, grade, converted_grade):

        assert (
            pyclimb.convert(grade=grade, grade_system="French", to="YDS")
            == converted_grade
        )


class TestConverterYDSToFrench:

    yds2french_map = [
        ("5.0", "1c+"),
        ("5.1", "2a+"),
        ("5.2", "2b+"),
        ("5.3", "3a"),
        ("5.4", "3b"),
        ("5.5", "3c+"),
        ("5.6", "4a+"),
        ("5.7", "4c"),
        ("5.8", "5a"),
        ("5.9", "5b+"),
        ("5.10a", "5c+"),
        ("5.10b", "6a+"),
        ("5.10c", "6b"),
        ("5.10d", "6b+"),
        ("5.11a", "6c"),
        ("5.11b", "6c+"),
        ("5.11c", "6c+"),
        ("5.11d", "7a"),
        ("5.12a", "7a+"),
        ("5.12b", "7b"),
        ("5.12c", "7b+"),
        ("5.12d", "7c"),
        ("5.13a", "7c+"),
        ("5.13b", "8a"),
        ("5.13c", "8a+"),
        ("5.13d", "8b"),
        ("5.14a", "8b+"),
        ("5.14b", "8c"),
        ("5.14c", "8c+"),
        ("5.14d", "9a"),
        ("5.15a", "9a+"),
        ("5.15b", "9b"),
        ("5.15c", "9b+"),
        ("5.15d", "9c"),
    ]

    @pytest.mark.parametrize("grade, converted_grade", yds2french_map)
    def test_convert_yds_to_french(self, grade, converted_grade):

        assert (
            pyclimb.convert(grade=grade, grade_system="YDS", to="French")
            == converted_grade
        )
