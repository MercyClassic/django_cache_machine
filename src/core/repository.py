from core.interfaces.repository import CoreRepositoryInterface
from core.models import Item


class CoreRepository(CoreRepositoryInterface):
    def get_items(self, ids: list[int]) -> list[Item]:
        return Item.objects.filter(id__in=ids)
