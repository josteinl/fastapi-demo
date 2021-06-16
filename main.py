# file: main.py
from fastapi import FastAPI

app = FastAPI(title="Small API", version='0.1.3')


@app.get("/")
async def root_is_the_best():
    """
    This is the root end point.
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
