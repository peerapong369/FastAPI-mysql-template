from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.NGRStock.NGRStock_model import NGRstockBase, NGRstockDisplayBase

from routers.NGRStock import NGRStock_controller
#from utils.oauth2 import access_user_token

router = APIRouter(prefix="/ngrstock", tags=["ngrstock"])


@router.get("/", response_model=List[NGRstockDisplayBase])
def get_all_ngrstock(db: Session = Depends(get_db)):
    return NGRStock_controller.read_ngrstock(db)


@router.get("/{id}")
def ngrstock_by_id(id: int, db:Session=Depends(get_db)):
    return NGRStock_controller.read_ngrstock_by_id(db, id)


@router.post("/")
def create_ngrstock(request: NGRstockBase, db: Session = Depends(get_db)):
    return NGRStock_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request:NGRstockBase, db:Session=Depends(get_db)):
    return NGRStock_controller.update(db, id, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return NGRStock_controller.delete(db, id)
