class InvalidPDFException(Exception):

    def __init__(
        self,
        message="Only PDF files are allowed."
    ):
        self.message = message


class FileTooLargeException(Exception):

    def __init__(
        self,
        message="File size exceeds the allowed limit."
    ):
        self.message = message


class ResumeNotFoundException(Exception):

    def __init__(
        self,
        message="Resume not found."
    ):
        self.message = message


class ResumeAnalysisNotFoundException(Exception):

    def __init__(
        self,
        message="Resume analysis not found."
    ):
        self.message = message