import logging

# Set up logging configuration to write logs to a file
logging.basicConfig(filename='app.log',  # Specify the log file name
                    level=logging.DEBUG,  # Set the log level to DEBUG (captures all log levels)
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Define the log message format


# Example log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')