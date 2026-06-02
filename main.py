from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date, time
from typing import Optional

from app.database import Base, engine, SessionLocal
from app.auth import create_token
from app.models import Employee, Attendance, Leave, Payroll
from app.schemas import (
    EmployeeCreate, EmployeeResponse,
    AttendanceCreate, AttendanceResponse,
    LeaveCreate, LeaveResponse,
    PayrollResponse
)

# CREATE TABLES
Base.metadata.create_all(bind=engine)

# CREATE APP
app = FastAPI(title="Employee Management System")

# DB DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- TEST ENDPOINT ----------------
@app.get("/test-attendance")
def test_attendance():
    return {"message": "Attendance route loaded successfully"}

# ---------------- AUTH ----------------
@app.post("/login")
def login():
    token = create_token({"user": "admin"})
    return {"access_token": token}

# ---------------- EMPLOYEE ----------------
@app.post("/employee", response_model=EmployeeResponse)
def add_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    employee = Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

# ---------------- ATTENDANCE ----------------
@app.post("/attendance", response_model=AttendanceResponse)
def mark_attendance(att: AttendanceCreate, db: Session = Depends(get_db)):
    record = Attendance(
        employee_id=att.employee_id,
        check_in=att.check_in,
        check_out=att.check_out
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@app.get("/attendance")
def view_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()

# ---------------- LEAVE ----------------
@app.post("/leave", response_model=LeaveResponse)
def apply_leave(leave: LeaveCreate, db: Session = Depends(get_db)):
    new_leave = Leave(
        employee_id=leave.employee_id,
        leave_type=leave.leave_type,
        days=leave.days
    )
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return new_leave

@app.get("/leaves")
def view_leaves(db: Session = Depends(get_db)):
    return db.query(Leave).all()

# ---------------- PAYROLL ----------------
@app.post("/payroll/{employee_id}", response_model=PayrollResponse)
def generate_payroll(employee_id: int, month: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return {"error": "Employee not found"}

    leaves = db.query(Leave).filter(Leave.employee_id == employee_id).all()
    leave_days = sum(l.days for l in leaves)

    deduction = leave_days * 500
    net_salary = employee.salary - deduction

    payroll = Payroll(
        employee_id=employee_id,
        month=month,
        net_salary=net_salary
    )
    db.add(payroll)
    db.commit()
    db.refresh(payroll)
    return payroll
