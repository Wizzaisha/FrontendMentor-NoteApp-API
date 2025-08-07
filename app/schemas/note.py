from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    isArchived: bool