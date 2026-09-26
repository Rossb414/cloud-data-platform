from fastapi import FastAPI
# Creates the FastAPI application
app = FastAPI()

@app.get("/")
#When a GET request is sent, the function underneath will run
def root():
    return{"message": "Cloud Data Platform API"}