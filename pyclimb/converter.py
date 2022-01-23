from pyclimb import exceptions, mappers
from pyclimb.grading_systems import GradingSystem


def convert(grade: str, to: str) -> str:
    """Converts a climbing grade to a specified grading system.

    Example:
        >>> pyclimb.convert(grade='6a+', to='YDS')
        >>> pyclimb.convert(grade='5.12a', to='French')

    Args:
        grade: The grade to be converted.
        to: The grading system onto which the grade will be converted.

    Returns:
        The converted grade.

    Raises:
        GradeConversionError: Error raised when the grade conversion fails.
    """
    try:
        grad_system = GradingSystem(to)

    except ValueError:
        raise exceptions.GradeConversionError(
            "Grade could not be converted: `to` is not a recognized grading system."
        )

    try:
        return mappers.french2yds[grade]

    except KeyError:
        raise exceptions.GradeConversionError(
            "Grade could not be converted: `grade` not recognized."
        )
