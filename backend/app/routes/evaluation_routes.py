from flask import Blueprint, request, jsonify
from app.services.evaluation_service import EvaluationService

evaluation_bp = Blueprint('evaluation_bp', __name__)

@evaluation_bp.route('/evaluations', methods=['GET'])
def get_evaluations():
    evaluations = EvaluationService.get_all_evaluations()
    return jsonify(evaluations)
