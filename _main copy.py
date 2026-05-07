from fastapi import FastAPI

try:
    from doro.app.doro_dircetor import Director
except ModuleNotFoundError:
    from apps.doro.app.doro_dircetor import Director

app = FastAPI(title="Eungsang Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지 ", "docs": "/docs"}


@app.get("/doro/data")
def read_doro_data():
    director = Director()
    df = director.get_data()

    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)