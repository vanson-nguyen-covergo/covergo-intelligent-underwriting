from fastapi import FastAPI

from covergo_rag_insure.routes.motor_insure import router as motor_insure_router

app = FastAPI(
    title="CoverGo Motor Insurance Risk Assessment",
    description="API for assessing motor insurance risk using RAG with OpenAI",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc", 
    openapi_url="/openapi.json"
)

# Register the motor insurance routes
app.include_router(motor_insure_router, prefix="/motor-insurances", tags=["Motor Insurance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Motor Insurance Risk Assessment Service"}
