from pyclimb import exceptions
from pyclimb.grading_system import GradingSystem
from pyclimb.mapper import get_conversion, mapper


def convert(grade: str, grade_system: str, to: str) -> str:
    """Converts a climbing grade to a specified grading system.

    Example:
        >>> pyclimb.convert(grade='6a+', grade_system='French', to='YDS')
        >>> pyclimb.convert(grade='5.12a', grade_system='YDS', to='French')

    Args:
        grade: The grade to be converted.
        grade_system: The grade system to which `grade` belongs.
        to: The grading system onto which the `grade` will be converted.

    Returns:
        The converted grade.

    Raises:
        GradeConversionError: Error raised when the grade conversion fails.
    """
    try:
        input_grading = GradingSystem(grade_system)

    except ValueError:
        raise exceptions.GradeConversionError(
            f"Grade could not be converted: {grade_system} is not a recognized grading system."
        ) from None

    try:
        output_grading = GradingSystem(to)

    except ValueError:
        raise exceptions.GradeConversionError(
            f"Grade could not be converted: {to} is not a recognized grading system."
        ) from None

    conversion = get_conversion(
        from_system=input_grading.value, to_system=output_grading.value
    )

    try:
        return mapper[conversion][grade]

    except KeyError:
        raise exceptions.GradeConversionError(
            f"Grade could not be converted: {grade} not recognized."
        ) from None
