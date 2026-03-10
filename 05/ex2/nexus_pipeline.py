from typing import Protocol, Any, List, Union, Dict
from abc import ABC, abstractmethod
from collections import deque
import json
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def process(self, data: Any) -> Any:
        print("Input:", data)
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Transform:", "processing")
        if isinstance(data, dict):
            data["processed"] = True
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Output:", data)
        return data


class ProcessingPipeline(ABC):
    __stages: List[ProcessingStage]
    __pipeline_id: str
    __stats: Dict[str, Any]

    def __init__(self, pipeline_id: str):
        self.__stages = []
        self.__pipeline_id = pipeline_id
        self.__stats = {"runs": 0, "errors": 0, "time": 0.0}

    def add_stage(self, stage: ProcessingStage) -> None:
        self.__stages.append(stage)

    def _run_stages(self, data: Any) -> Any:
        start = time.time()
        try:
            for stage in self.__stages:
                data = stage.process(data)
            self.__stats["runs"] += 1
        except Exception:
            self.__stats["errors"] += 1
            print("Recovery: stage failure handled")
        self.__stats["time"] += time.time() - start
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]: ...

    def get_id(self) -> str:
        return self.__pipeline_id

    def stats(self) -> Dict[str, Any]:
        return {
            k: v
            for k, v in self.__stats.items()
        }


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            parsed = json.loads(data) if isinstance(data, str) else data
        except Exception:
            parsed = {"raw": data}
        result = self._run_stages(parsed)
        return json.dumps(result)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            parts = [x.strip() for x in str(data).split(",")]
            structured = {
                i: v
                for i, v in enumerate(parts)
            }
        except Exception:
            structured = {"raw": data}
        result = self._run_stages(structured)
        return ",".join([str(v) for v in result.values()])


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)
        self.buffer = deque()

    def process(self, data: Any) -> Union[str, Any]:
        self.buffer.append(data)
        structured = {"count": len(self.buffer), "last": data}
        result = self._run_stages(structured)
        return result


class NexusManager:
    __pipelines: List[ProcessingPipeline]

    def __init__(self) -> None:
        self.__pipelines = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.__pipelines.append(pipeline)

    def run_all(self, data: Any) -> List[Any]:
        return [p.process(data) for p in self.__pipelines]

    def chain(self, data: Any) -> Any:
        for p in self.__pipelines:
            data = p.process(data)
        return data


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()

    json_pipeline = JSONAdapter("JSON_PIPE")
    csv_pipeline = CSVAdapter("CSV_PIPE")
    stream_pipeline = StreamAdapter("STREAM_PIPE")

    for p in [json_pipeline, csv_pipeline, stream_pipeline]:
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("=== Multi Format Processing ===")

    json_data = '{"sensor":"temp","value":23.5,"unit":"C"}'
    csv_data = "user,action,timestamp"
    stream_data = "sensor_reading"

    print("JSON result:", json_pipeline.process(json_data))
    print("CSV result:", csv_pipeline.process(csv_data))
    print("Stream result:", stream_pipeline.process(stream_data))

    print("\n=== Pipeline Chaining ===")
    result = manager.chain(json_data)
    print("Chain result:", result)

    print("\n=== Stats ===")
    stats = {
        p.get_id(): p.stats() for p in [
            json_pipeline,
            csv_pipeline,
            stream_pipeline,
        ]
    }
    print(stats)
