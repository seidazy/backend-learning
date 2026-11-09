from fastapi import FastAPI, HTTPException

app = FastAPI()

notes = [
  {"id": 1, "title": "Note 1", "description": "Description 1"},
  {"id": 2, "title": "Note 2", "description": "Description 2"},
  {"id": 3, "title": "Note 3", "description": "Description 3"},
]

@app.get("/notes")
def list_notes():
  return {"notes": notes}


@app.get("/note/{note_id}")
def get_note(note_id: int):
  note = next((note for note in notes if note["id"] == note_id), None)
  if note:
    return {"note": note}
  else:
    raise HTTPException(status_code=404, detail="Note not found")
