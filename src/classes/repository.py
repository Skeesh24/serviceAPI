from typing import Dict, List, Union

from pymongo.collection import Collection, ReturnDocument

from classes.helper import convert_to_service
from classes.interfaces import IRepository
from settings import env

class ServiceRepository(IRepository):
    def __init__(self, collection: Collection) -> None:
        self.db = collection

    def get(self, **kwargs) -> Union[List[Dict], Dict]:
        limit = kwargs.pop(env.PARAM_LIMIT, None)

        if limit and limit == 1:
            filter = kwargs
            doc = self.db.find_one(filter)
            return convert_to_service(doc)

        cursor = self.db.find(kwargs)
        return [convert_to_service(doc) for doc in cursor]

    def add(self, element: dict) -> str:
        result = self.db.insert_one(element)
        return str(result.inserted_id)

    # def update(self, id: str, element: dict) -> dict:
    #     filter = {env.PARAM_ID: id}
    #     update = {"$set": element}

    #     old_element = self.db.find_one_and_update(
    #         filter=filter, update=update, return_document=ReturnDocument.BEFORE
    #     )
    #     return old_element

    # def remove(self, **kwargs) -> int:
    #     result = self.db.delete_one(kwargs)
    #     return result.deleted_count
