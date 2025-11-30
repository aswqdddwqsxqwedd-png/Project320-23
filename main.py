from functions import konstantin, inoyatov, c2, func_soliyev
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

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

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html at root
@app.get("/")
async def serve_root():
    return FileResponse("index.html", media_type="text/html")

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