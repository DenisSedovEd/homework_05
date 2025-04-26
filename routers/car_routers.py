from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel, Field



from random import randint


router = APIRouter()

class CarUpdate(BaseModel):
    mark: str = Field(..., title='Mark', min_length=1, max_length=20)
    model: str = Field(..., title='Model', min_length=1, max_length=20)
    year: int = Field(..., title='Year', ge=1990, le=2025)


class Car(CarUpdate):
    pk: int


cars = []

for i in range(10):
    cars.append(Car(
        pk=i,
        mark=f'Марка {i}',
        model=f'Модель {i}',
        year=randint(1990, 2025),
    ))


@router.get('/{car_id}')
async def read_cars(car_id: int):
    for car in cars:
        if car.pk == car_id:
            return {'car': car}
    return {'msg': 'Not found'}


@router.get('/')
async def cars_list():
    return {'cars': cars}


@router.post('/')
async def create_car(car: Car):
    cars.append(car)
    return {'car': car}
