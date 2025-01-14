from app.models.evaluation import Evaluation
from app.database.connection import get_db_session

class EvaluationService:
    @staticmethod
    def get_all_evaluations():
        session = get_db_session()
        evaluations = session.query(Evaluation).all()
        return [{'id': evaluation.id, 'research_id': evaluation.research_id, 'user_id': evaluation.user_id, 'score': evaluation.score} for evaluation in evaluations]
