from sqlalchemy import Column, Integer, String, Boolean, Date, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

from app.db.association.note_tag_association import note_tag

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    is_archived = Column(Boolean, nullable=False)
    last_edited = Column(Date, nullable=False)
    description = Column(Text)
    user_id = Column(String, nullable=False)

    tags = relationship("Tag", secondary=note_tag, back_populates="notes")
