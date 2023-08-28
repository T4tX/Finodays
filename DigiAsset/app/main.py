from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Union, List
from pydantic import BaseModel

app = FastAPI(
    title="My API",
    description="This is a simple API for managing products and orders.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "products",
            "description": "Operations related to products"
        },
        {
            "name": "orders",
            "description": "Operations related to orders"
        }
    ]
)


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


@app.get("/", tags=["root"])
async def index():
    """
    Root endpoint.

    Returns a dictionary with a welcome message.
    """
    return {'hello': 'world'}


@app.get("/products", tags=["products"])
async def get_products_list(category: Union[str, None] = None):
    """
    Get a list of products.

    :param category: category of products (optional)
    :return: JSON response with a list of products
    """
    records = db.query("select * from products")
    products_list = {'products': records}
    return JSONResponse(content=products_list)


@app.get("/products/{id}", tags=["products"])
async def get_products_by_id(id: int):
    """
    Get a product by ID.

    :param id: ID of the product
    :return: JSON response with the product
    """
    records = db.query(f"select * from products where id = {id}")
    products_list = {'product': records}
    return JSONResponse(content=products_list)


@app.get("/orders/{user_id}", tags=["orders"])
async def get_user_orders_by_id(user_id: int):
    """
    Get orders of a user by ID.

    :param user_id: ID of the user
    :return: JSON response with a list of orders
    """
    records = db.query(f"select * from orders where from_user_id = {user_id}")
    products_list = {'orders': records}
    return JSONResponse(content=products_list)


@app.post("/orders", tags=["orders"])
async def make_order(order_list: List[Order]):
    """
    Create an order.

    :param order_list: list of orders
    :return: JSON response confirming the creation of the order
    """
    for order in order_list:
        records = db.query(
            f"insert into orders values (default,{order.from_user_id},{order.to_user_id},{order.price},{order.product_id},'{order.create_date}')")
    return {"Confirmed"}


@app.get("/orders/{id}", tags=["orders"])
async def get_order_by_id(id: int):
    """
    Get an order by ID.

    :param id: ID of the order
    :return: JSON response with the order
    """
    records = db.query(f"select * from orders where id = {id}")
    products_list = {'order': records}
    return JSONResponse(content=products_list)


@app.put("/orders/{id}/cancel", tags=["orders"])
async def order_cancel(id: int):
    """
    Cancel an order.

    :param id: ID of the order
    :return: JSON response with information about the cancellation of the order
    """
    return {"order_id": id, "order_status": "cancelled"}


@app.put("/orders/{id}/confirm_payment", tags=["orders"])
async def order_confirm(id: int):
    """
    Confirm the payment of an order.

    :param id: ID of the order
    :return: JSON response with information about the confirmation of the payment of the order
    """
    return {"order_id": id, "order_status": "confirmed"}
