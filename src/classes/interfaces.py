from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union


class IRepository(ABC):
    @abstractmethod
    def get(self, **kwargs) -> List[Dict]:
        """
        Returns a list of querying objects.
        kwargs: if provided limit=1 return the first element
        kwargs: other parameters used to filter by the specified fields
        """
        pass

    @abstractmethod
    def add(self, element: dict) -> str:
        """
        Returns an ObjectID of inserted element as a string format
        element: dictionary representation of the inserted element
        """
        pass

    # @abstractmethod
    # def update(self, id: str, element: dict) -> dict:
    #     """
    #     Returns a dictionary representation of the old element
    #     id: ObjectID of updated element
    #     element: dictionary representation of the updated element
    #     """
    #     pass

    # @abstractmethod
    # def remove(self, **kwargs) -> int:
    #     """
    #     Returns the count of deleted elements
    #     kwargs: parameters used to filter by the special fields
    #     """
    #     pass
