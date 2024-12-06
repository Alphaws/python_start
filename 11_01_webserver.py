from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    with open("hello.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@app.get("/foltos")
def foltos():
    return {"message": "Nyugi van, foltos"}