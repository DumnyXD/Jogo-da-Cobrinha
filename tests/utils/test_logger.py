import pytest
import logging
from unittest.mock import patch, MagicMock, call
import importlib

# from src.utils.logger import Logger # Will import it inside the test function

class TestLogger:
    @pytest.fixture(autouse=True)
    def setup_logger_mocks(self):
        # Aggressively reset logging state
        logging.shutdown()
        # Re-initialize logging to a clean state
        importlib.reload(logging)

        with (patch('logging.StreamHandler') as mock_stream_handler_class,
              patch('logging.FileHandler') as mock_file_handler_class,
              patch('logging.getLogger') as mock_get_logger):

            # Create a fresh mock logger instance for each test
            self.mock_logger_instance = MagicMock()
            mock_get_logger.return_value = self.mock_logger_instance
            # Ensure the mock logger starts with no handlers
            self.mock_logger_instance.handlers = []
            self.mock_logger_instance.reset_mock() # Reset mock calls for each test
            self.mock_logger_instance.addHandler.reset_mock() # Explicitly reset addHandler

            # Configure mock handler instances
            self.mock_stream_handler = MagicMock()
            self.mock_file_handler = MagicMock()
            mock_stream_handler_class.return_value = self.mock_stream_handler
            mock_file_handler_class.return_value = self.mock_file_handler
            self.mock_stream_handler.reset_mock() # Reset before the test runs
            self.mock_file_handler.reset_mock() # Reset before the test runs

            # Import Logger here to ensure it uses the patched logging functions
            from src.utils.logger import Logger
            self.LoggerClass = Logger # Store it for use in tests

            yield

    def test_logger_initialization(self, setup_logger_mocks):
        logger_instance = self.LoggerClass() # Use the imported Logger class

        self.mock_logger_instance.setLevel.assert_called_once_with(logging.INFO)
        self.mock_stream_handler.setFormatter.assert_called_once()
        self.mock_file_handler.setFormatter.assert_called_once()
        self.mock_logger_instance.addHandler.assert_any_call(self.mock_stream_handler)
        self.mock_logger_instance.addHandler.assert_any_call(self.mock_file_handler)
        self.mock_logger_instance.addHandler.assert_has_calls([call(self.mock_stream_handler), call(self.mock_file_handler)], any_order=True)

    def test_info_method(self, setup_logger_mocks):
        logger_instance = self.LoggerClass()
        logger_instance.info("Test info message")
        self.mock_logger_instance.info.assert_called_once_with("Test info message")

    def test_warning_method(self, setup_logger_mocks):
        logger_instance = self.LoggerClass()
        logger_instance.warning("Test warning message")
        self.mock_logger_instance.warning.assert_called_once_with("Test warning message")

    def test_error_method(self, setup_logger_mocks):
        logger_instance = self.LoggerClass()
        logger_instance.error("Test error message")
        self.mock_logger_instance.error.assert_called_once_with("Test error message")

    def test_debug_method(self, setup_logger_mocks):
        logger_instance = self.LoggerClass()
        logger_instance.debug("Test debug message")
        self.mock_logger_instance.debug.assert_called_once_with("Test debug message")
