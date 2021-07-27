
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from employees import Roles
from service import get_ranked_data_with_requests_lib, get_ranked_data_with_aiohttp_lib


def main():
    app = FastAPI()

    origins = [
        "http://localhost:3000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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

    @app.get("/ranked-stats/{summoner_id}")
    def get_ranked_stats_by_summoner_id(summoner_id: str):
        """
        Endpoint to get Ranked Stats by Summoner ID
        """
        return get_ranked_data_with_requests_lib(summoner_id)

    @app.get("/ranked-stats-aiohttp/{summoner_id}")
    def get_ranked_stats_by_summoner_id(summoner_id: str):
        """
        Endpoint to get Ranked Stats by Summoner ID
        """
        return asyncio.run(get_ranked_data_with_aiohttp_lib(summoner_id))

    uvicorn.run(app, host="localhost", port=8080)


if __name__ == '__main__':
    main()
