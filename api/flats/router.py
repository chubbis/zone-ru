from typing import List
from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.flats import views
from app.flats import schemas


router = APIRouter(tags=["Flats"], prefix="/api/v1/flats")


router.add_api_route(
    "/",
    methods=["GET"],
    endpoint=views.get_flats,
    response_model=List[schemas.FlatBase],
    name="flats",
)

router.add_api_route(
    "/edit/{flat_id:int}",
    methods=["PUT"],
    endpoint=views.update_flat,
    response_class=JSONResponse
)

router.add_api_route(
    "/result/{flat_id:int}",
    methods=["GET"],
    endpoint=views.get_result,
    response_class=JSONResponse
)

router.add_api_route(
    "/{flat_id:int}",
    methods=["GET"],
    endpoint=views.get_flat,
    response_model=schemas.FlatItem,
    name="flat",
)