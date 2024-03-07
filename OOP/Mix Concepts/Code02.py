"""Decorator Pattern for Logging:
Create a Logger interface with methods like logInfo, logWarning, and logError.
Implement concrete classes for different logging mechanisms (e.g., ConsoleLogger, FileLogger, DatabaseLogger).
Use decorator pattern to add additional functionality to the loggers (e.g., timestamp, severity level).
Demonstrate how you can dynamically add or remove decorators to customize logging behavior."""

from abc import ABC, abstractmethod

# Step 1: Logger Interface
class Logger(ABC):
    @abstractmethod
    def log_info(self, message: str):
        pass

    @abstractmethod
    def log_warning(self, message: str):
        pass

    @abstractmethod
    def log_error(self, message: str):
        pass

# Step 2: Concrete Logger Classes
class ConsoleLogger(Logger):
    def log_info(self, message: str):
        print(f"[INFO] {message}")

    def log_warning(self, message: str):
        print(f"[WARNING] {message}")

    def log_error(self, message: str):
        print(f"[ERROR] {message}")

# Step 3: Decorator Pattern
class TimestampLoggerDecorator(Logger):
    def __init__(self, logger: Logger):
        self.logger = logger

    def log_info(self, message: str):
        timestamped_message = f"{self._get_timestamp()} [INFO] {message}"
        self.logger.log_info(timestamped_message)

    def log_warning(self, message: str):
        timestamped_message = f"{self._get_timestamp()} [WARNING] {message}"
        self.logger.log_warning(timestamped_message)

    def log_error(self, message: str):
        timestamped_message = f"{self._get_timestamp()} [ERROR] {message}"
        self.logger.log_error(timestamped_message)

    def _get_timestamp(self):
        # Implement timestamp logic (e.g., datetime.now())
        pass

# Step 4: Demonstration
if __name__ == "__main__":
    console_logger = ConsoleLogger()
    timestamped_console_logger = TimestampLoggerDecorator(console_logger)

    # Log messages
    timestamped_console_logger.log_info("Application started")
    timestamped_console_logger.log_warning("Memory usage high")
    timestamped_console_logger.log_error("Critical error occurred")
