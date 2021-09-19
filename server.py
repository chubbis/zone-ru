import uvicorn


from database.mysql import engine
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from config import Debug
from api.flats.router import router as flats_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")
debug = Debug()

app = FastAPI(
    docs_url="/docs/" if debug.debug else None,
    openapi_url="/docs/openapi.json" if debug.debug else None,
)


# @app.get("/communal-payments", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("/index.j2", {"request": request})


# @app.get("/communal-payments", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "/communal_payments/communal_payments.j2", {"request": request}
#     )

app.include_router(flats_router)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")


if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=9091,
        reload=True,
        ssl_keyfile="./key.pem",
        ssl_certfile="./cert.pem",
    )
