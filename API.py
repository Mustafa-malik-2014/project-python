import fastapi
import googlesearch as gs

app = fastapi.FastAPI()
@app.get("/")
def read_root():
    return "its working Mustafa you did it"

@app.get("/search")
def search(query: str):
    results = gs.search(query)
    return results