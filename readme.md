# Benefits of FastAPI

- automatically generates a Swagger Docs for all API Endpoints 
```sh
  // %baseurl%/docs
  http://localhost:8080/docs
```

# Tools

- FastAPI
- uvicorn -> to run API

# Step-by-step

## Prerequisites

- python + pip

## on windows: virtual environment

### install virtualenv

```sh
    pip install virtualenv
````

### start virtualenv

```sh
    env/Scripts/activate
```

### in case of "UnauthorizedAccess" or "PSSecurityException"

```sh
    Set-ExecutionPolicy Unrestricted -Scope Process
```

## start uvicorn server to run API

### change directory to where our app.py / entrypoint to app is

```sh
    cd "%root of our dir%"
```

### Method 1: start uvicorn server through shell

```sh
    // uvicorn %filename%:%name_of_fast_api_variable%
    uvicorn app:app
```

### Method 2: start uvicorn server through .py script

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}

uvicorn.run(app, host="0.0.0.0", port=8080)
```
