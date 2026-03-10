from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str: ...

    @abstractmethod
    def validate(self, data: Any) -> bool: ...

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            validation = self.validate(data)
            if not validation:
                return "Error: Invalid numeric data"
            total = sum(data)
            avg = total / len(data)
            return f"Processed {len(data)} numeric values, " \
                f"sum={total}, avg={avg}"
        except Exception as e:
            return f"Error processing numeric data: {e}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            print("Invalid: data must be a list")
            return False
        if not all(isinstance(x, (int, float)) for x in data):
            print("Invalid: all elements must be numeric")
            return False
        print("Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(
        self,
        data: Any,
    ) -> str:
        try:
            validation = self.validate(data)
            if not validation:
                return "Error: Invalid text data"
            char_count = len(data)
            word_count = len(data.split())
            return f"Processed text: {char_count} characters, " \
                f"{word_count} words"
        except Exception as e:
            return f"Error processing text data: {e}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            print("Invalid: data must be a string")
            return False
        if len(data.strip()) == 0:
            print("Invalid: text cannot be empty")
            return False
        print("Text data verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    LOG_LEVELS: List[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def process(self, data: Any) -> str:
        try:
            validation = self.validate(data)
            if not validation:
                return "Error: Invalid log entry"
            parts = data.split(":", 1)
            level = parts[0].strip()
            message = parts[1].strip() if len(parts) > 1 else data
            if level in ["ERROR", "CRITICAL"]:
                return f"[ALERT] {level} level detected: {message}"
            elif level == "WARNING":
                return f"[WARN] {level} level detected: {message}"
            else:
                return f"[INFO] {level} level detected: {message}"
        except Exception as e:
            return f"Error processing log data: {e}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            print("Invalid: log entry must be a string")
            return False
        has_level = any(data.startswith(level) for level in self.LOG_LEVELS)
        if not has_level:
            print("Invalid: log entry must start with a valid log level")
            return False
        print("Log entry verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print("Validation: ", end="")
    np_proc: NumericProcessor = NumericProcessor()
    result = np_proc.process(numeric_data)
    print(np_proc.format_output(result))

    print()

    print("Initializing Text Processor...")
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print("Validation: ", end="")
    tp: TextProcessor = TextProcessor()
    result = tp.process(text_data)
    print(tp.format_output(result))

    print()

    print("Initializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print("Validation: ", end="")
    lp: LogProcessor = LogProcessor()
    result = lp.process(log_data)
    print(lp.format_output(result))

    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    processors: List[Union[NumericProcessor, TextProcessor, LogProcessor]] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    datasets: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "WARNING: Low memory",
    ]

    for i, (processor, data) in enumerate(zip(processors, datasets), start=1):
        result = processor.process(data)
        print(f"Result {i}: {result}")
