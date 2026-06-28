from fastapi import APIRouter

from services.vision_service import VisionService

router = APIRouter(
    prefix="/vision",
    tags=["Vision"]
)

service = VisionService()


@router.get("/")
def vision():

    return service.process()
