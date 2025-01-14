from flask import Blueprint, request, jsonify
from app.services.research_service import ResearchService

research_bp = Blueprint('research_bp', __name__)

@research_bp.route('/researches', methods=['GET'])
def get_researches():
    researches = ResearchService.get_all_researches()
    return jsonify(researches)
