import fastapi
import googlesearch as gs

app = fastapi.FastAPI()
@app.get("/")
def read_root():
    return "its working Mustafa you did it"

@app.get("/search")
def search(query: str):
    headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    results = list(gs.search(query , num_results=5 , user_agent=headers))
    return results
