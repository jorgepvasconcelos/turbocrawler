from abc import ABC, abstractmethod
from typing import Any

from turbocrawler.engine.base_queues.crawler_queue_base import CrawlerQueueABC
from turbocrawler.engine.data_types.crawler import CrawlerRequest, CrawlerResponse, ExtractRule
from turbocrawler.engine.data_types.info import ExecutionInfo


class Crawler(ABC):
    crawler_name: str
    allowed_domains: list[str]
    regex_extract_rules: list[ExtractRule] = []
    time_between_requests: int | float = 0

    crawler_queue: CrawlerQueueABC

    @classmethod
    @abstractmethod
    def start_crawler(cls) -> None:
        ...

    @classmethod
    @abstractmethod
    def crawler_first_request(cls) -> CrawlerResponse:
        ...

    @classmethod
    @abstractmethod
    def process_request(cls, crawler_request: CrawlerRequest) -> CrawlerResponse:
        ...

    @classmethod
    @abstractmethod
    def parse_crawler_response(cls, crawler_response: CrawlerResponse) -> Any:
        ...

    @classmethod
    @abstractmethod
    def stop_crawler(cls, execution_info: ExecutionInfo) -> None:
        ...
