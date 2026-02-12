from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/logs")
async def receive_logs(request : Request):
    data = await request.json()
    print("LOG", data)
    return {"status" : "ok"}

