from fastapi import FastAPI

app = FastAPI()

@app.get("/SeeYouLater")

def goodbay():
    return{
    
        "message":"goodbay"
    }