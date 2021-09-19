from fastapi import APIRouter

from api.flats import views

router = APIRouter(tags=["Flats"], prefix="/flats")


router.add_api_route(
    "/",
    methods=["GET"],
    endpoint=views.get_flats,
)

router.add_api_route(
    "/{flat_id:int}",
    methods=["GET"],
    endpoint=views.get_flat,
)
