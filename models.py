from sqlalchemy import Column, Integer, String, Date, Time
from datetime import date
from app.database import Base

# ---------------- Employee ----------------
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)
    salary = Column(Integer)

# ---------------- Attendance ----------------
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(Date, default=date.today)
    check_in = Column(Time, nullable=True)
    check_out = Column(Time, nullable=True)

# ---------------- Leave ----------------
class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    leave_type = Column(String)
    days = Column(Integer)
    status = Column(String, default="Pending")

# ---------------- Payroll ----------------
class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    month = Column(String)
    net_salary = Column(Integer)
