import sys

def error_message_detail(error, error_details: sys):
    """
    Capture detailed error information.

    Args:
        error (Exception): The exception instance.
        error_details (sys): The sys module to extract traceback.

    Returns:
        str: A formatted error message with the file name, line number, and error message.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        Custom exception class to capture and display detailed error messages.

        Args:
            error_message (str): The error message.
            error_details (sys): The sys module to extract traceback details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details=error_details)

    def __str__(self):
        """
        String representation of the custom exception.

        Returns:
            str: Detailed error message.
        """
        return self.error_message
