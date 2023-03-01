from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from models.NGRStock.NGRStock_model import DbNgrstock, NGRstockBase


def create(db: Session, request: NGRstockBase):
    new_ngrstock = DbNgrstock(
    shelf_number=request.shelf_number,
    shelf_position=request.shelf_position,
    current_stock=request.current_stock,
    current_lotcount=request.current_lotcount,
    current_product=request.current_product,
    current_group=request.current_group,
    current_customer=request.current_customer,
    shelf_limit=request.shelf_limit,
    )
    db.add(new_ngrstock)
    db.commit()
    db.refresh(new_ngrstock)
    return new_ngrstock


def delete(db: Session, id: int):
    ngrstock = db.query(DbNgrstock).filter(DbNgrstock.id == id).first()
    db.delete(ngrstock)
    db.commit()
    return JSONResponse(content={"detail": f"ngrstock id {id} deleted"})


def update(db: Session, id: int, request: NGRstockBase):
    ngrstock = db.query(DbNgrstock).filter(DbNgrstock.id == id).first()
    ngrstock.shelf_number=request.shelf_number
    ngrstock.shelf_position=request.shelf_position
    ngrstock.current_stock=request.current_stock
    ngrstock.current_lotcount=request.current_lotcount
    ngrstock.current_product=request.current_product
    ngrstock.current_group=request.current_group
    ngrstock.current_customer=request.current_customer
    ngrstock.shelf_limit=request.shelf_limit
    db.commit()
    db.refresh(ngrstock)
    return ngrstock


def read_ngrstock(db: Session):
    return db.query(DbNgrstock).all()


def read_ngrstock_by_id(db: Session, id: int):
    return db.query(DbNgrstock).filter(DbNgrstock.id == id).first()
