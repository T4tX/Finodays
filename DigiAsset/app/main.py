import db
from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Products(BaseModel):
    name: str
    token: str
    category: str


class Order(BaseModel):
    from_user_id: int
    to_user_id: int
    price: int
    product_id: int
    create_date: str


@app.get("/")
async def index():
    """
    Главная страница.

    :return: словарь с приветственным сообщением
    """
    return {'hello': 'world'}


@app.get(("/products"))
async def get_products_list(category: Union[str, None] = None):
    """
    Получение списка ЦФА ( продуктов ).

    :param category: категория продуктов (опционально)
    :return: JSON-ответ со списком продуктов
    """
    records = db.query("select * from products")
    products_list = {'products': records}
    return JSONResponse(content=products_list)


@app.get(("/products/{id}"))
async def get_products_by_id(id: int):
    """
    Получение продукта по id.

    :param id: id продукта
    :return: JSON-ответ с продуктом
    """
    records = db.query(f"select * from products where id = {id}")
    products_list = {'product': records}
    return JSONResponse(content=products_list)


@app.get(("/orders/{user_id}"))
async def get_user_orders_by_id(user_id: int):
    """
    Получение заказов пользователя по id.

    :param user_id: id пользователя
    :return: JSON-ответ со списком заказов
    """
    records = db.query(f"select * from orders where from_user_id = {user_id}")
    products_list = {'orders': records}
    return JSONResponse(content=products_list)


@app.post(("/orders"))
async def make_order(order_list: List[Order]):
    """
    Создание заказа.

    :param order_list: список заказов
    :return: JSON-ответ с подтверждением создания заказа
    """
    for order in order_list:
        records = db.query(
            f"insert into orders values (default,{order.from_user_id},{order.to_user_id},{order.price},{order.product_id},'{order.create_date}')")
    return {"Confirmed"}


@app.get(("/orders/{id}"))
async def get_order_by_id(id: int):
    """
    Получение заказа по id.

    :param id: id заказа
    :return: JSON-ответ с заказом
    """
    records = db.query(f"select * from orders where id = {id}")
    products_list = {'order': records}
    return JSONResponse(content=products_list)


@app.put(("/orders/{id}/cancel"))
async def order_cansel(id: int):
    """
    Отмена заказа.

    :param id: id заказа
    :return: JSON-ответ с информацией об отмене заказа
    """
    return {"order_id": id, "order_status": "canseled"}


@app.put(("/orders/{id}/confirm_payment"))
async def order_confirm(id: int):
    """
    Подтверждение оплаты заказа.

    :param id: id заказа
    :return: JSON-ответ с информацией о подтверждении оплаты заказа
    """
    return {"order_id": id, "order_status": "confirmed"}
