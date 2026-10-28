import fastapi
import uvicorn

app = fastapi.FastAPI()
@app.get("/")
def read_root():
    return "it's working Mustafa you did it"
