import sys
# import logging

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()  # Get exception info from sys module
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))  # Initialize base class with error message
        self.error_message = error_message_detail(error)  # Call the detail function
    
    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:    
#         a = 1 / 0  # Trigger a divide by zero error
#     except Exception as e: 
#         logging.info("Divide by zero error")
#         raise CustomException(e)
