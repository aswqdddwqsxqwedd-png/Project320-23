from functions import konstantin
from functionInoyatov import inoyatov
from functionilyasik import ilyas
import function_soliyev as s

print(inoyatov(25,5))
print(konstantin(3,6))
print(ilyas(3,4))
print(s.function_soliyev(4,5))

@app.get("/c2")
def get_ilyas(x: float, y: float):
    return {"result": ilyas(x, y)}
@app.post("/c2")
def post_ilyas(data: TwoNumbers):
    return {"result": ilyas(data.x, data.y)}
