from app.models.user import User
from app.database.connection import get_db_session

class UserService:
    @staticmethod
    def get_all_users():
        session = get_db_session()
        users = session.query(User).all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
