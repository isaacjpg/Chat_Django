
from typing import Iterable


def log_method(logger: "logging.Logger", method: str, message_action: str, log_args: Iterable[str]):
    def decorator(cls):
        original_method = getattr(cls, method)

        def wrapped_method(self, *args, **kwargs):
            try:
                logger.info(f"{message_action} initiated")

                # Log arguments
                log_values = [getattr(self, arg) if hasattr(self, arg) else arg for arg in log_args]
                logger.info(f"Arguments: {log_values}")

                # Execute the original method
                result = original_method(self, *args, **kwargs)

                # Log action completed
                logger.info(f"{message_action} completed")

                return result
            except Exception as e:
                # Log action failed
                logger.error(f"{message_action} failed")
                raise e

        setattr(cls, method, wrapped_method)
        return cls

    return decorator