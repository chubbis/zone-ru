import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from api.flats.router import router as flats_router
from config import Debug
from errors import UnicornException, ErrorsHash

app = FastAPI()
templates = Jinja2Templates(directory="templates")
debug = Debug()

origins = [
    "https://127.0.0.1:8080",
    "https://localhost:8080",
]
print(debug.debug)
app = FastAPI(
    docs_url="/docs/" if debug.debug else None,
    openapi_url="/docs/openapi.json" if debug.debug else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=JSONResponse)
def homepage():
    return "c-b-s"


@app.get("/robots.txt", response_class=HTMLResponse)
def robots(request: Request):
    return templates.TemplateResponse("/robots.j2", {"request": request})


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(exc: UnicornException):
    e = ErrorsHash()
    content = e.get_error(err=exc.name)
    return JSONResponse(
        status_code=200,
        content=content,
    )

app.include_router(flats_router)

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="localhost",
        port=9091,
        reload=True,
        debug=debug.debug,
        ssl_keyfile="./key.pem",
        ssl_certfile="./cert.pem",
    )
