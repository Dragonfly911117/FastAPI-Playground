from fastapi import FastAPI
from FakeCDN import upload, getFile
app = FastAPI()

app.include_router(upload.router)
app.include_router(getFile.router)

@app.get("/")
def index():
    return {"message": "Hello World"}
