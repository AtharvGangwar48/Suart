import traceback
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class ErrorHandler:
    @staticmethod
    def handle_exception(e: Exception, context: str = ""):
        error_msg = f"Error in {context}: {str(e)}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        
        return {
            "error": True,
            "message": error_msg,
            "type": type(e).__name__
        }
    
    @staticmethod
    def log_warning(message: str, context: str = ""):
        warning_msg = f"Warning in {context}: {message}"
        logger.warning(warning_msg)
    
    @staticmethod
    def create_error_response(message: str, status_code: int = 500):
        return {
            "error": True,
            "message": message,
            "status_code": status_code
        }