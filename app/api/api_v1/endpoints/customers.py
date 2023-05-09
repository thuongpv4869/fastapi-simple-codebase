from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.services import crud_customer
from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(deps.get_db)):
    db_customer = crud_customer.create_customer(db, customer)
    return db_customer


@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(deps.get_db)):
    db_customer = crud_customer.read_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(deps.get_db)):
    db_customer = crud_customer.read_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud_customer.update_customer(db, customer, db_customer)
    return db_customer


@router.delete("/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(deps.get_db)):
    db_customer = crud_customer.read_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud_customer.delete_customer(db, db_customer)
    return db_customer


@router.get("/", response_model=list[schemas.Customer])
def list_customer(db: Session = Depends(deps.get_db)):
    customers = crud_customer.list_customer(db)
    return customers
