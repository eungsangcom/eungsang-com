from fastapi import FastAPI

try:
    from titanic.app.james import James
except ModuleNotFoundError:
    from apps.titanic.app.james import James

try:
    from doro.app.doro_director import Director
except ModuleNotFoundError:
    from apps.doro.app.doro_director import Director

app = FastAPI(title="Eungsang Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지 ", "docs": "/docs"}


@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data()

    return df.to_dict(orient="records")

@app.get("/titanic/count")
def read_titanic_count():
    james = James()
    count = james.get_count()
    return {"count": count}

@app.get("/titanic/tree")
def read_titanic_tree():
    james = James()
    tree = james.check_decision_tree_model()
    return {"tree": tree}

@app.get("/doro/data")
def read_doro_data():
    director = Director()
    df = director.get_data()

    return df.to_dict(orient="records")

@app.get("/titanic/count/survived")
def read_titanic_survived_count():
    james = James()
    return james.get_survived_count()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
