from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

from models.NGR_RS_STOCK_MASTER.ngr_rs_stock_master_module import DbInsStock, InsStockMasterBase


def create(db: Session, request: InsStockMasterBase):
    new_stockdata = DbInsStock(
        locker=request.locker,
        product_name=request.product_name,
        type=request.type,
        qlimit=request.qlimit,
    )
    db.add(new_stockdata)
    db.commit()
    db.refresh(new_stockdata)
    return new_stockdata


def delete(db: Session, id: int):
    stock = db.query(DbInsStock).filter(DbInsStock.id == id).first()
    db.delete(stock)
    db.commit()
    return JSONResponse(content={"detail": f"stock id {id} deleted"})


def read_stockmaster(db: Session):
    return db.query(DbInsStock).all()


def update(db: Session, id: int, request: InsStockMasterBase):
    stock = db.query(DbInsStock).filter(DbInsStock.id == id).first()
    stock.locker = request.locker
    stock.product_name = request.product_name
    stock.type = request.type
    stock.qlimit = request.qlimit
    db.commit()
    db.refresh(stock)
    return stock