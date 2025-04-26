from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/')
async def index(request: Request):
    context = {"request": request,
               'title': 'Главная страница'}
    return templates.TemplateResponse('index.html', context=context)

@router.get("/about")
async def about(request: Request):
    context = {"request": request,
               'title': 'О сайте'
               }
    return templates.TemplateResponse('about.html', context=context)