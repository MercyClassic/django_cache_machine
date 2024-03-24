import io
from typing import Protocol


class CoreServiceInterface(Protocol):
    def build_pdf_file(self, ids: list[int]) -> str:
        raise NotImplementedError

    def get_qr_code_img(self, scheme: str, host: str, file_name: str) -> io.BytesIO:
        raise NotImplementedError
