from classes.repository import ServiceRepository
from database.core import collection, db


async def get_db():
    try:
        yield db
    finally:
        db.client.close


async def get_collection():
    try:
        yield collection
    finally:
        collection.database.client.close()


async def get_services():
    service = ServiceRepository(collection=collection)
    try:
        yield service
    finally:
            service.db.database.client.close()
