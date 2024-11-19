from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dp_dependency = Depends(get_db)


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = dp_dependency):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/delete")

@app.get("/blog")
def all(db:Session = dp_dependency):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}",status_code=200)
def show(id, response: Response, db: Session = dp_dependency):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    return blog