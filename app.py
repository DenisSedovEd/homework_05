import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from routers.car_routers import router as car_routers
from routers.api_routers import router as api_router


app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.include_router(car_routers, prefix='/car', tags=['car'])
app.include_router(api_router, prefix='/api', tags = ['api'])


@app.get("/")
async def index(request: Request):
    context = {"request": request,
               'title': 'Главная страница'}
    return templates.TemplateResponse('index.html', context=context)
#
# @app.get("/about")
# async def about(request: Request):
#     context = {"request": request,
#                'title': 'О сайте'
#                }
#     return templates.TemplateResponse('about.html', context=context)


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=0, reload=True)
