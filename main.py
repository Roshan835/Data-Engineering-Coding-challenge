# Import all the necessary libraries
from fastapi import FastAPI
from src.routes import router

# Initialize FastAPI app instance and include the defined router
app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000)