from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import db



app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Products(BaseModel):
    name: str
    token: str
    #is_sale: Union[bool, None] = None
    category: str

class Order(BaseModel):
    product_id: int
    price: int
    payment_method: int

@app.get("/")
async def index():
    return {'hello':'world'}

@app.get(("/products"))
async def get_products_list(category: Union[str, None] = None):
    records = db.query("select * from products")
    products_list = {'products': records}
    return JSONResponse(content=products_list)

@app.get(("/products/{id}"))
async def get_products_by_id(id: int):
    records = db.query(f"select * from products where id = {id}")
    products_list = {'product': records}
    return JSONResponse(content=products_list)


@app.get(("/orders/{user_id}"))
async def get_user_orders_by_id(user_id: int):
    records = db.query(f"select * from orders where from_user_id = {user_id}")
    products_list = {'orders': records}
    return JSONResponse(content=products_list)


@app.post(("/orders"))
async def make_order(order_list: List[Order]):
    return {"Confirmed"}

@app.get(("/orders/{id}"))
async def get_order_by_id(id: int):
    records = db.query(f"select * from orders where id = {id}")
    products_list = {'order': records}
    return JSONResponse(content=products_list)

@app.put(("/orders/{id}/cancel"))
async def order_cansel(id: int):
    return {"order_id": id, "order_status": "canseled"}

@app.put(("/orders/{id}/confirm_payment"))
async def order_confirm(id: int):
    return {"order_id": id, "order_status": "confirmed"}

'''@app.get(("/products"))
async def get_products_list(oproduct_list: List[Products], category: Union[str, None] = None):
    return oproduct_list'''
