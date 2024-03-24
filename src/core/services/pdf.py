from uuid import uuid4

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from core.interfaces.services.pdf import PdfServiceInterface

HTML_TEMPLATE = """
ООО "КОМПАНИЯ К"
Добро пожаловать
ККМ 00075411       #3969
ИНН 1087746942040
      ЭКЛЗ 3851495566
%s СИС.
 АДМИ
%s

Итог
            %.2f
НАЛИЧНЫМИ           =%.2f
*************************************
                     00003751# 05970
"""


class PdfService(PdfServiceInterface):
    def __init__(self, fonts_root: str, media_root: str) -> None:
        self.fonts_root = fonts_root
        self.media_root = media_root

    def build_pdf_file(self, current_time: str, items_text: str, amount: float) -> str:
        template = HTML_TEMPLATE % (current_time, items_text, amount, amount)
        file_name = str(uuid4())

        pdfmetrics.registerFont(TTFont('FreeSans', f'{self.fonts_root}/FreeSans.ttf'))
        cnvs = canvas.Canvas(f'{self.media_root}/{file_name}.pdf', pagesize=letter)
        cnvs.setFont('FreeSans', 16)

        text = cnvs.beginText(200, 650)
        text.textLines(template, trim=0)
        cnvs.drawText(text)
        cnvs.save()
        return file_name
