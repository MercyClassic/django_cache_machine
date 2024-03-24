import io

import qrcode
from django.utils import timezone

from core.interfaces.repository import CoreRepositoryInterface
from core.interfaces.services.core import CoreServiceInterface
from core.interfaces.services.pdf import PdfServiceInterface


class CoreService(CoreServiceInterface):
    def __init__(
        self,
        core_repo: CoreRepositoryInterface,
        pdf_service: PdfServiceInterface,
    ) -> None:
        self.core_repo = core_repo
        self.pdf_service = pdf_service

    def build_pdf_file(self, ids: list[int]) -> str:
        counts = {}
        for _id in ids:
            counts[_id] = counts.get(_id, 0) + 1

        amount = 0
        items_text = ''
        items = self.core_repo.get_items(ids)
        for item in items:
            count = counts[item.pk]
            amount += count * item.price
            items_text += f'{item.title}\n    {count}       ={count * item.price}\n'

        current_time = timezone.localtime().strftime('%d.%m.%Y %H:%M')
        file_name = self.pdf_service.build_pdf_file(
            current_time=current_time,
            items_text=items_text,
            amount=amount,
        )
        return file_name

    def get_qr_code_img(self, scheme: str, host: str, file_name: str) -> io.BytesIO:
        qr_code = qrcode.make(f'{scheme}://{host}/media/{file_name}.pdf')
        img = io.BytesIO()
        img.name = f'{file_name}.jpg'
        qr_code.save(img, 'jpeg')
        img.seek(0)
        return img
