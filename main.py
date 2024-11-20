import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    # 使用 JSONResponse 设置紧凑模式
    return JSONResponse(content={"Hello": "Wanyu Zhang"}, indent=None, separators=(",", ":"))

@app.get("/uni/wz2652")
def read_item(uni_id: str, q: Union[str, None] = None):
    # 使用 JSONResponse 设置紧凑模式
    return JSONResponse(content={"uni_id": uni_id, "q": q}, indent=None, separators=(",", ":"))
