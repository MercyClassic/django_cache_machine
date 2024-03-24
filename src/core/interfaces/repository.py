from abc import abstractmethod
from typing import Protocol

from core.models import Item


class CoreRepositoryInterface(Protocol):
    @abstractmethod
    def get_items(self, ids: list[int]) -> list[Item]:
        raise NotImplementedError
