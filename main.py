from fastapi import FastAPI
from functions import konstantin
from functionInoyatov import inoyatov
from functionilyasik import ilyas
import function_soliyev as s
from pydantic import BaseModel

class TwoNumbers(BaseModel):
    x: float
    y: float

print(inoyatov(25,5))
print(konstantin(3,6))
print(ilyas(3,4))
print(s.function_soliyev(4,5))

app = FastAPI( title="UMFT320I", version="1.0.0",
description="Платформа для покупки и продажи",
docs_url="/docs",
redoc_url="/redoc",
#debug=settings.DEBUG, 
)

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result": inoyatov(x, y)}
@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": inoyatov(data.x, data.y)}