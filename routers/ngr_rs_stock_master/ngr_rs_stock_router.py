from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.NGR_RS_STOCK_MASTER.ngr_rs_stock_master_module import InsStockMasterBase, InsStockMasterDisplayBase

from routers.ngr_rs_stock_master import ngr_rs_stock_controller

router = APIRouter(prefix="/ngrstockmaster", tags=["ngrstockmaster"])


@router.post("/")
def create_stock(request: InsStockMasterBase, db: Session = Depends(get_db)):
    return ngr_rs_stock_controller.create(db, request)


@router.get("/", response_model=List[InsStockMasterDisplayBase])
def get_all_stock(db: Session = Depends(get_db)):
    return ngr_rs_stock_controller.read_stockmaster(db)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return ngr_rs_stock_controller.delete(db, id)


@router.put("/{id}")
def put_api(id: int, request:InsStockMasterBase, db:Session=Depends(get_db)):
    return ngr_rs_stock_controller.update(db, id, request)