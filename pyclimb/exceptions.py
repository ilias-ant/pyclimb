class PyClimbError(Exception):
    """Base class for pyclimb exceptions."""


class GradeConversionError(PyClimbError):
    """Error raised when the pyclimb grade conversion fails."""
