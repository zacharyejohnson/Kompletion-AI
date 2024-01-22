from flask import Flask, request, jsonify
from .controllers.Interview_controller import InterviewController

app = Flask(__name__)
interview_controller = InterviewController()

@app.route('/interviews', methods=['GET'])
def get_all_interviews():
    """
    Endpoint to get all interviews.
    """
    interviews = interview_controller.get_all_interviews()
    return jsonify(interviews)

@app.route('/interview', methods=['POST'])
def create_interview():
    """
    Endpoint to create a new interview.
    """
    data = request.json
    new_interview = interview_controller.create_interview(data)
    return jsonify(new_interview), 201

@app.route('/interview/<interview_id>', methods=['GET'])
def get_interview(interview_id):
    """
    Endpoint to get a specific interview.
    """
    interview = interview_controller.get_interview(interview_id)
    if interview:
        return jsonify(interview)
    else:
        return jsonify({'message': 'Interview not found'}), 404

@app.route('/interview/<interview_id>', methods=['PUT'])
def update_interview(interview_id):
    """
    Endpoint to update an existing interview.
    """
    data = request.json
    updated_interview = interview_controller.update_interview(interview_id, data)
    if updated_interview:
        return jsonify(updated_interview)
    else:
        return jsonify({'message': 'Interview not found'}), 404

@app.route('/interview/<interview_id>', methods=['DELETE'])
def delete_interview(interview_id):
    """
    Endpoint to delete an interview.
    """
    success = interview_controller.delete_interview(interview_id)
    if success:
        return jsonify({'message': 'Interview deleted successfully'}), 200
    else:
        return jsonify({'message': 'Interview not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
