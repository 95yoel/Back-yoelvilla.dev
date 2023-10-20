from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router # IMPORT ROUTES
from cors_config import add_cors_middleware # IMPORT CORS CONFIG



app = FastAPI()

# CORS CONFIG
add_cors_middleware(app)

# ROUTES
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

