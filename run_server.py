import uvicorn

def main():
    """Main function to run the FastAPI server."""
    uvicorn.run("covergo_rag_insure.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
