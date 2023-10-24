from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status

from classes.dependencies import get_services
from classes.enums import Status
from classes.interfaces import IRepository
from classes.validation import service_model
from settings import env

service_router = APIRouter(prefix="/service", tags=["service"])


@service_router.get("/", response_model=List[service_model])
async def get_service_list(db: IRepository = Depends(get_services)):
    return db.get()


@service_router.get("/{name}", response_model=service_model)
async def get_service_by_name(name: str, db: IRepository = Depends(get_services)):
    try:
        service = db.get(limit=1, service=name)
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=env.MSG_NOT_FOUND_ERROR)
    return service


@service_router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=service_model
)
async def create_service(content=Body(), db: IRepository = Depends(get_services)):
    service = {}

    try:
        service = service_model.create_as_dict(**content)
    except:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=env.MSG_ASSOCIATION_ERROR,
        )

    try:
        Status(service[env.PARAM_STATUS])
    except:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=env.MSG_INVALID_STATUS)

    try:
        service.update({env.PARAM_ID: db.add(element=service)})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=env.MSG_CREATING_ERROR,
        )

    return service
