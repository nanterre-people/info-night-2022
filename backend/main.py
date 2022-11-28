import uvicorn

from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List

from backend.config import app, get_db
from backend.models import Student, StudentSchema, Promotion, PromotionSchema


@app.get('/students', response_model=List[StudentSchema])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get('/promotions', response_model=List[PromotionSchema])
def get_promotions(db: Session = Depends(get_db)):
    promotions = db.query(Promotion).all()
    return promotions


def main():
    uvicorn.run('backend.main:app', host='localhost', port=8000, reload=True)

if __name__ == '__main__':
    main()