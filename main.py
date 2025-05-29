from fastapi import FastAPI, HTTPException
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def Bienvenue():
    try:
        return {"message": "Bienvenue dans l'API de l'application !"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

