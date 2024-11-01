from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"status": {"code": 200, "message": "Success fetching the API"}}


if __name__ == "__main__":
    import granian

    granian.Granian(
        "main:app",
        port=8000,
        interface="asgi",
        reload=True,
        log_level="info",
        workers=4,
        threads=4,
    ).serve()
