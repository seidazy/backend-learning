from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

notes = [
  {"id": 1, "title": "Note 1", "description": "Description 1"},
  {"id": 2, "title": "Note 2", "description": "Description 2"},
  {"id": 3, "title": "Note 3", "description": "Description 3"},
]

class NoteIn(BaseModel):
  title: str
  description: str

@app.get("/notes")
def list_notes():
  return {"notes": notes}


@app.get("/notes/{note_id}")
def get_note(note_id: int):
  note = next((note for note in notes if note["id"] == note_id), None)
  if note:
    return {"note": note}
  else:
    raise HTTPException(status_code=404, detail="Note not found")


@app.post("/notes")
def create_note(note: NoteIn):
  new_id = max((n["id"] for n in notes), default=0) + 1
  new_note = {
    "id": new_id,
    "title": note.title,
    "description": note.description,
  }
  notes.append(new_note)
  return {"note": new_note}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
  note = next((note for note in notes if note["id"] == note_id), None)
  if note:
    notes.remove(note)
    return {"message": "Note deleted"}
  else:
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn):
  note = next((note for note in notes if note["id"] == note_id), None)
  if note:
    note["title"] = note.title
    note["description"] = note.description
    return {"note": note}
  else:
    raise HTTPException(status_code=404, detail="Note not found")