from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel


class DbNgrstock(Base):
    __tablename__ = "ngrstock"
    id = Column(Integer, primary_key=True, index=True)
    shelf_number = Column(String, unique=True)
    shelf_position = Column(String, unique=False)
    current_stock = Column(DECIMAL, unique=False)
    current_lotcount = Column(DECIMAL, unique=False)
    current_product = Column(String, unique=False)
    current_group = Column(String, unique=False)
    current_customer = Column(String, unique=False)
    shelf_limit = Column(DECIMAL, unique=False)
    last_move = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )


class NGRstockBase(BaseModel):
    shelf_number: str
    shelf_position: str
    current_stock: Decimal
    current_lotcount:Decimal
    current_product:str
    current_group:str
    current_customer:str
    shelf_limit: Decimal


class NGRstockDisplayBase(BaseModel):
    id: int
    shelf_number: str
    shelf_position: str
    current_stock: Decimal
    current_lotcount:Decimal
    current_product:str
    current_group:str
    current_customer:str
    shelf_limit: Decimal
    last_move: datetime

    class Config:
        orm_mode = True
