from typing import Union

import uvicorn
from app.routes import movie_routes
from app.routes import flower_routes
from app.routes import cat_and_dog_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(movie_routes.router)
app.include_router(flower_routes.router)
app.include_router(cat_and_dog_routes.router)

if __name__ == "__main__":
    # uvicorn.run(app, host="localhost", port=8002)
    uvicorn.run(app, host="0.0.0.0", port=8002)