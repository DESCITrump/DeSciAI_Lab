from app.models.research import Research
from app.database.connection import get_db_session

class ResearchService:
    @staticmethod
    def get_all_researches():
        session = get_db_session()
        researches = session.query(Research).all()
        return [{'id': research.id, 'title': research.title, 'description': research.description} for research in researches]
