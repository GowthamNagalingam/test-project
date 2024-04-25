import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_traceback = error_detail.exc_info()
    filename = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error in file [{0}] on line [{1}] error message [{3}]".format(
        filename, exc_traceback.tb_lineno, str(error)
        )
    return error_message
    

class CustomExeption(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message