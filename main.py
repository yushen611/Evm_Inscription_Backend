from fastapi import FastAPI
from routers import Example, TokenInfo

app = FastAPI()

@app.get("/ping")
def read_root():
    return {"Hello": "World"}

app.include_router(Example.router)
app.include_router(TokenInfo.router)

if __name__ == '__main__':
    print('铭文，启动！')
