from abc import abstractmethod
from typing import Protocol


class PdfServiceInterface(Protocol):
    @abstractmethod
    def build_pdf_file(self, current_time: str, items_text: str, amount: float) -> str:
        pass
