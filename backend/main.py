from fastapi import FastAPI

app = FastAPI(title="Container Planner API")

@app.get("/")
def read_root():
    return {"Hello": "This is Container Planner API"}