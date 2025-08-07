from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.association.note_tag_association import note_tag
from app.db.session import Base

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    notes = relationship("Note", secondary=note_tag, back_populates="Tags")