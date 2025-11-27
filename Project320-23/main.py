from functions import konstantin
from functionInoyatov import inoyatov
from functionilyasik import c2
from function_soliyev import func_soliyev
from fastapi import FastAPI
from pydantic import BaseModel

class TwoNumbers(BaseModel):
    x: float
    y: float

print(inoyatov(25,5))
print(konstantin(3,6))
print(c2(3,4))
print(func_soliyev(4,5))

app = FastAPI( title="EEEA", version="1.0.0",
description="BOBA",
docs_url="/docs",
redoc_url="/redoc",
#debug=settings.DEBUG, 
)

@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x, y)}
@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}

@app.get("/konstantin")
def get_konstantin(x: float, y: float):
    return {"result": konstantin(x, y)}
@app.post("/konstantin")
def post_konstantin(data: TwoNumbers):
    return {"result": konstantin(data.x, data.y)}