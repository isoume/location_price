from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
   return {
       "message": "Hello from FastAPI"
   }


@app.get("/hello")
def read_root():
   return {
       "message": "hello Routers"
   }
