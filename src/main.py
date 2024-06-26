from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.v1.routers import router as api_router_v1


# Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Упрощённый аналог форумников",
    summary="Forums&Threads + Notifications of CRUD operations!",
    version="0.0.1",
)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    server_urn = f"{request.scope.get('server')[0]}:{request.scope.get('server')[1]}"
    return templates.TemplateResponse("index.html", {"request": request, "server_urn": server_urn})


@app.get("/1", response_class=HTMLResponse)
async def read_root(request: Request):
    server_urn = f"{request.scope.get('server')[0]}:{request.scope.get('server')[1]}"
    return templates.TemplateResponse("index.html", {"request": request, "server_urn": server_urn})


# Подключаем созданные роутеры в приложение
app.include_router(api_router_v1, prefix='/api')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
