from pydantic import BaseModel
from datetime import date, time
from typing import Optional

# ---------------- Employee ----------------
class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str
    salary: int

class EmployeeResponse(EmployeeCreate):
    id: int

# ---------------- Attendance ----------------
class AttendanceCreate(BaseModel):
    employee_id: int
    check_in: Optional[time] = None
    check_out: Optional[time] = None

class AttendanceResponse(AttendanceCreate):
    id: int
    date: date

# ---------------- Leave ----------------
class LeaveCreate(BaseModel):
    employee_id: int
    leave_type: str
    days: int

class LeaveResponse(LeaveCreate):
    id: int
    status: str

# ---------------- Payroll ----------------
class PayrollResponse(BaseModel):
    employee_id: int
    month: str
    net_salary: int
