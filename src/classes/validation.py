from datetime import datetime

from pydantic import BaseModel

from settings import env


class service_model(BaseModel):
    id: str = None
    service: str
    status: str
    description: str = ""
    date_time: datetime = datetime.now()

    @staticmethod
    def create_as_dict(service: str, status: str, description: str = "") -> dict:
        representation = service_model(
            service=service, status=status, description=description
        ).model_dump()
        representation.pop(env.PARAM_ID)
        return representation
