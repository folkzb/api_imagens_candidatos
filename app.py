from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get('/')
async def init():
  return FileResponse("vota_ai!.png")

@app.get('/{candidato}')
async def main(candidato):
  candidato = candidato.lower()
  return FileResponse(f"{candidato}.png")


uvicorn.run(app, host="0.0.0.0", port="8000")
