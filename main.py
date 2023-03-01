from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.database import engine
from models.NGR_RS_STOCK_MASTER import ngr_rs_stock_master_module


from routers.ngr_rs_stock_master import ngr_rs_stock_router


app = FastAPI()

origins = [
    "*",
    "http://localhost:8005",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ngr_rs_stock_router.router)


@app.get("/")
def hello():
    return {"hellow": "Fast-API"}



ngr_rs_stock_master_module.Base.metadata.create_all(engine)