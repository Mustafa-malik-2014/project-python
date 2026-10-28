import fastapi
import googlesearch as gs

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return "its working Mustafa you did it"


@app.get("/search")
def search(query: str):
    # Using advanced=True parses full result objects (titles, descriptions, URLs)
    # which often bypasses the plain-text blank HTML trap
    results = []
    try:
        for url in gs.search(query, num_results=5, advanced=False):
            results.append(str(url))
    except Exception as e:
        return {"error": str(e)}

    return {"query": query, "results": results}