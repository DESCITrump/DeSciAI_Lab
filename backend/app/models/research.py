from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database.connection import Base

class Research(Base):
    __tablename__ = 'researches'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Research {self.title}>'
