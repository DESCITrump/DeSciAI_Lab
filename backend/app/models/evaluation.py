from sqlalchemy import Column, Integer, ForeignKey, Float
from app.database.connection import Base

class Evaluation(Base):
    __tablename__ = 'evaluations'

    id = Column(Integer, primary_key=True)
    research_id = Column(Integer, ForeignKey('researches.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    score = Column(Float, nullable=False)

    def __repr__(self):
        return f'<Evaluation {self.id} with score {self.score}>'
