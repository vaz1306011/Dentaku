import logging
import sys
import traceback

PROJECT_ROOT = "0G02019_dentaku/"
LOG_FILE_NAME = "dentaku.log"
PACKAGE_NAME = "dentaku"


class TraceStyleFormatter(logging.Formatter):
    def format(self, record) -> str:
        level = f"[{record.levelname}]"
        time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")

        header = f"{level} - {time}:"
        message = record.getMessage()

        if record.levelno >= logging.ERROR or record.levelno == logging.DEBUG:
            stack = self.__filter_stack()
            return f"{header}\n{stack}{message}\n"
        else:
            location = (
                f'File "{record.pathname}", line {record.lineno}, in {record.funcName}'
            )
            return f"{header}\n{self.__add_space(location, 2)}\n{self.__add_space(message, 4)}\n"

    def __filter_stack(self) -> str:
        stack = []
        for line in traceback.format_stack():
            stack.append(line)
            if PROJECT_ROOT in line and "logger." not in line:
                continue
            elif PROJECT_ROOT not in line:
                break
        filtered = [s for s in stack if "logging" not in s]
        return "".join(filtered)

    def __add_space(self, text: str, num_spaces: int) -> str:
        spaces = " " * num_spaces
        return spaces + text.replace("\n", "\n" + spaces)


def setup_logging() -> None:
    formatter = TraceStyleFormatter()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = None
    if not getattr(sys, "frozen", False):
        file_handler = logging.FileHandler(f"{LOG_FILE_NAME}.log", encoding="utf-8")
        file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.addHandler(console_handler)

    logger = logging.getLogger(PACKAGE_NAME)
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    file_handler and logger.addHandler(
        file_handler
    )  # pyright: ignore[reportUnusedExpression]
    logger.propagate = False
