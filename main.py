from fastapi import FastAPI

app = FastAPI()

notes = [
  {"id": 1, "title": "Note 1", "description": "Description 1"},
  {"id": 2, "title": "Note 2", "description": "Description 2"},
  {"id": 3, "title": "Note 3", "description": "Description 3"},
]

@app.get("/notes")
def list_notes():
  return {"notes": notes}
