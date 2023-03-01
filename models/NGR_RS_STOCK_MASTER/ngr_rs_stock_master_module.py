from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT, VARCHAR
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbInsStock(Base):
    __tablename__ = "NGR_RS_STOCK_MASTER"
    id = Column(Integer, primary_key=True, index=True)
    locker =  Column(VARCHAR(10), unique=True)
    product_name =  Column(String, unique=False)
    type =  Column(String, unique=False)
    qlimit =  Column(Integer, unique=False)

class InsStockMasterBase(BaseModel):
    locker : str
    product_name : str
    type : str
    qlimit : int


class InsStockMasterDisplayBase(BaseModel):
    id: int
    locker : str
    product_name : str
    type : str
    qlimit : int

    class Config:
        orm_mode = True

