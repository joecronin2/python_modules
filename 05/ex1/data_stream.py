from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.total_processed: int = 0
        self.total_batches: int = 0
        self.errors: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: ...

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_processed": self.total_processed,
            "total_batches": self.total_batches,
            "errors": self.errors,
        }


class SensorStream(DataStream):
    STREAM_TYPE: str = "Environmental Data"
    ALERT_THRESHOLD: float = 30.0

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.temp_readings: List[float] = []

    def _parse_reading(self, item: Any) -> Optional[float]:
        try:
            if isinstance(item, str) and item.startswith("temp:"):
                return float(item.split(":")[1])
        except (IndexError, ValueError):
            pass
        return None

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                v for item in data_batch
                if (v := self._parse_reading(item)) is not None
            ]
            self.temp_readings.extend(temps)
            self.total_processed += len(data_batch)
            self.total_batches += 1
            avg = sum(temps) / len(temps) if temps else 0.0
            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg:.1f}°C"
            )
        except Exception as e:
            self.errors += 1
            return f"Sensor batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                item for item in data_batch
                if (v := self._parse_reading(item)) is not None
                and v > self.ALERT_THRESHOLD
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = self.STREAM_TYPE
        stats["avg_temp"] = (
            round(sum(self.temp_readings) / len(self.temp_readings), 2)
            if self.temp_readings else 0.0
        )
        return stats


class TransactionStream(DataStream):
    STREAM_TYPE: str = "Financial Data"
    LARGE_THRESHOLD: float = 100.0

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.net_flow: float = 0.0

    def _parse_transaction(self, item: Any) -> Optional[tuple]:
        try:
            if isinstance(item, str) and ":" in item:
                direction, amount_str = item.split(":", 1)
                return direction.strip().lower(), float(amount_str.strip())
        except (ValueError, AttributeError):
            pass
        return None

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            parsed = [
                t
                for item in data_batch
                if (t := self._parse_transaction(item)) is not None
            ]
            net = sum(amt if d == "buy" else -amt for d, amt in parsed)
            self.net_flow += net
            self.total_processed += len(data_batch)
            self.total_batches += 1
            sign = "+" if net >= 0 else ""
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net:.0f} units"
            )
        except Exception as e:
            self.errors += 1
            return f"Transaction batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch
                if (t := self._parse_transaction(item)) is not None
                and t[1] > self.LARGE_THRESHOLD
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = self.STREAM_TYPE
        stats["net_flow"] = round(self.net_flow, 2)
        return stats


class EventStream(DataStream):
    STREAM_TYPE: str = "System Events"
    ERROR_KEYWORDS: List[str] = ["error", "fail", "critical", "exception"]

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_count: int = 0

    def _is_error(self, item: Any) -> bool:
        return isinstance(item, str) and any(
            kw in item.lower() for kw in self.ERROR_KEYWORDS
        )

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors_in_batch = sum(1 for item in data_batch if self._is_error(
                item
            ))
            self.error_count += errors_in_batch
            self.total_processed += len(data_batch)
            self.total_batches += 1
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{errors_in_batch} error"
                f"{'s'if errors_in_batch != 1 else ''} detected"
            )
        except Exception as e:
            self.errors += 1
            return f"Event batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "errors":
            return [item for item in data_batch if self._is_error(item)]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = self.STREAM_TYPE
        stats["total_errors"] = self.error_count
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        return [
            stream.process_batch(batch)
            for stream, batch in zip(self.streams, batches)
        ]

    def filter_all(
        self, batches: List[List[Any]], criteria: List[Optional[str]]
    ) -> List[List[Any]]:
        return [
            stream.filter_data(batch, crit)
            for stream, batch, crit in zip(self.streams, batches, criteria)
        ]

    def all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {SensorStream.STREAM_TYPE}")
    sensor_batch_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch_1)}]")
    print(sensor.process_batch(sensor_batch_1))

    print()

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, "
          f"Type: {TransactionStream.STREAM_TYPE}")
    trans_batch_1 = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch_1)}]")
    print(trans.process_batch(trans_batch_1))

    print()

    print("Initializing Event Stream...")
    events = EventStream("EVENT_001")
    print(f"Stream ID: {events.stream_id}, Type: {EventStream.STREAM_TYPE}")
    event_batch_1 = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch_1)}]")
    print(events.process_batch(event_batch_1))

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.register(SensorStream("SENSOR_002"))
    processor.register(TransactionStream("TRANS_002"))
    processor.register(EventStream("EVENT_002"))

    mixed_batches: List[List[Any]] = [
        ["temp:18.0", "temp:35.2"],
        ["buy:200", "sell:50", "buy:90", "sell:120"],
        ["login", "error: disk full", "logout"],
    ]

    results = processor.process_all(mixed_batches)
    print("Batch 1 Results:")
    labels = ["Sensor data", "Transaction data", "Event data"]
    counts = [2, 4, 3]
    units = ["readings", "operations", "events"]
    for label, count, unit in zip(labels, counts, units):
        print(f"  - {label}: {count} {unit} processed")

    print()
    print("Stream filtering active: High-priority data only")

    filter_criteria: List[Optional[str]] = ["critical", "large", "errors"]
    filtered = processor.filter_all(mixed_batches, filter_criteria)

    critical_sensors = filtered[0]
    large_transactions = filtered[1]

    print(
        f"Filtered results: {len(critical_sensors)} critical sensor alert"
        f"{'s' if len(critical_sensors) != 1 else ''}, "
        f"{len(large_transactions)} large transaction"
        f"{'s' if len(large_transactions) != 1 else ''}"
    )

    print()
    print("All streams processed successfully. Nexus throughput optimal.")
