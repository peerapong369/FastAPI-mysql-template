import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.16.140", port=8000, log_level="info")
    print("Server Classed")
