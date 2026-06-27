🏢 Smart Employee Management System

A backend REST API built with FastAPI for managing employee records, attendance, leave, and payroll — with JWT authentication and SQLite database.

🚀 Features

🔐 JWT Authentication — Secure token-based login
👤 Employee Management — Add and view employee records
🕐 Attendance Tracking — Mark and view check-in/check-out times
🗓️ Leave Management — Apply and track employee leaves
💰 Payroll Generation — Auto-calculate net salary with leave deductions
📄 Swagger UI — Interactive API docs at /docs


🛠️ Tech Stack
LayerTechnologyFrameworkFastAPIDatabaseSQLiteORMSQLAlchemyAuthJWT (python-jose)ValidationPydanticLanguagePython 3.10+

📁 Project Structure
ems/
├── main.py          # All API routes
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic request/response schemas
├── database.py      # DB connection and session setup
├── auth.py          # JWT token creation
├── ems.db           # SQLite database (auto-created)
└── __init__.py

⚙️ Setup & Installation
1. Clone the repository
bashgit clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system
2. Create virtual environment
bashpython -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
3. Install dependencies
bashpip install fastapi uvicorn sqlalchemy python-jose[cryptography] pydantic
4. Run the server
bashuvicorn main:app --reload
5. Open API docs
http://127.0.0.1:8000/docs

📡 API Endpoints
🔐 Auth
MethodEndpointDescriptionPOST/loginGet JWT access token
👤 Employee
MethodEndpointDescriptionPOST/employeeAdd new employeeGET/employeesGet all employees
🕐 Attendance
MethodEndpointDescriptionPOST/attendanceMark attendanceGET/attendanceView all attendance records
🗓️ Leave
MethodEndpointDescriptionPOST/leaveApply for leaveGET/leavesView all leave requests
💰 Payroll
MethodEndpointDescriptionPOST/payroll/{employee_id}Generate payroll for employee

📊 Payroll Logic
Net salary is calculated as:
Net Salary = Base Salary - (Total Leave Days × ₹500)

📬 Sample Request
Add Employee
jsonPOST /employee
{
  "name": "Bharat Kumar",
  "email": "bharat@example.com",
  "role": "Backend Developer",
  "salary": 50000
}
Mark Attendance
jsonPOST /attendance
{
  "employee_id": 1,
  "check_in": "09:00:00",
  "check_out": "18:00:00"
}
