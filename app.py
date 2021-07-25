import uvicorn
from fastapi import FastAPI

from employees import Roles


def main():
    app = FastAPI()

    employeeDB = [
        {
            "first_name": "Jochen",
            "last_name": "Rui",
            "role": Roles.JUNIORDEV
        },
        {
            "first_name": "John",
            "last_name": "Wick",
            "role": Roles.CTO
        },
    ]

    @app.get("/")
    def home():
        return {"Data": "Test"}

    @app.get("/employees")
    def get_employees():
        """
        Endpoint to get all employees
        """
        return employeeDB

    @app.get("/employees/{role}")
    def get_employees_by_role(role: Roles):
        """
        Endpoint to get employees by role
        """
        return [employee for employee in employeeDB if employee["role"] == role]

    uvicorn.run(app, host="localhost", port=8080)


if __name__ == '__main__':
    main()
