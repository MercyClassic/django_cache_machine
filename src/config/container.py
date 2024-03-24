from dependency_injector import containers, providers

from config import settings
from core.repository import CoreRepository
from core.services.core import CoreService
from core.services.pdf import PdfService


class CoreContainer(containers.DeclarativeContainer):
    core_repository = providers.Factory(CoreRepository)
    pdf_service = providers.Factory(
        PdfService,
        fonts_root=settings.FONTS_ROOT,
        media_root=settings.MEDIA_ROOT,
    )

    core_service = providers.Factory(
        CoreService,
        core_repo=core_repository,
        pdf_service=pdf_service,
    )


container = CoreContainer()
