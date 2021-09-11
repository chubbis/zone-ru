import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from config import Debug

app = FastAPI()
templates = Jinja2Templates(directory="templates")
debug = Debug()


app = FastAPI(
    docs_url="/docs/" if debug.debug else None,
    openapi_url="/docs/openapi.json" if debug.debug else None,
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('/app_base.j2', {"request": request})


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")

if __name__ == '__main__':
    uvicorn.run("server:app",
                host="0.0.0.0",
                port=9091,
                reload=True,
                ssl_keyfile="./key.pem",
                ssl_certfile="./cert.pem"
                )
