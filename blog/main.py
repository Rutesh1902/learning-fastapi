from fastapi import FastAPI
from . import models, schemas
from database import engine
app = FastAPI()

models.Base.metadeta.create_all(engine)

@app.post("/blog")
def create(request: schemas.Blog):
    return request

