from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.shared.utils.logger import init_logger

# Configure logging once at the entry point
log = init_logger()


app = FastAPI(
    title="{service_name}",
    description="",
    version="0.0.1",
)

# CORS configuration - must specify exact origins when using credentials
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)