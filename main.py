from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/user/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def polzovatel(user_id: Annotated[int, Path(maximum=100, minimum=1, description='Enter User ID', example='1')]) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get('/user/{username}/{age}')
async def ctranizi(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(maximum=120, minimum=18, description='Enter age', example='24')]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@app.get('/')
async def welcome() -> dict:
    return {"message": "Главная страница"}