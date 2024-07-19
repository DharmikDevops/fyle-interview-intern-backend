from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
assignments = [
    {"id": 1, "content": "Math Homework", "student_id": 1, "teacher_id": 1, "grade": "A", "state": "GRADED", "created_at": "2023-01-01T12:00:00Z", "updated_at": "2023-01-01T12:00:00Z"},
    {"id": 2, "content": "Science Project", "student_id": 2, "teacher_id": 2, "grade": "B", "state": "GRADED", "created_at": "2023-01-02T12:00:00Z", "updated_at": "2023-01-02T12:00:00Z"}
]
teachers = [
    {"id": 1, "user_id": 3, "created_at": "2024-01-08T07:58:53.131970", "updated_at": "2024-01-08T07:58:53.131972"},
    {"id": 2, "user_id": 4, "created_at": "2024-01-08T07:58:53.131970", "updated_at": "2024-01-08T07:58:53.131972"}
]

# Principal APIs

# API 1: GET /principal/assignments - List all submitted and graded assignments
@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    principal_header = request.headers.get('X-Principal')
    if principal_header is None or "principal_id" not in principal_header:
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify({"data": assignments}), 200

# API 2: GET /principal/teachers - List all teachers
@app.route('/principal/teachers', methods=['GET'])
def get_principal_teachers():
    principal_header = request.headers.get('X-Principal')
    if principal_header is None or "principal_id" not in principal_header:
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify({"data": teachers}), 200

# API 3: POST /principal/assignments/grade - Re-grade an assignment
@app.route('/principal/assignments/grade', methods=['POST'])
def regrade_assignment():
    principal_header = request.headers.get('X-Principal')
    if principal_header is None or "principal_id" not in principal_header:
        return jsonify({"error": "Unauthorized"}), 403

    assignment_id = request.json.get('id')
    new_grade = request.json.get('grade')

    for assignment in assignments:
        if assignment['id'] == assignment_id:
            assignment['grade'] = new_grade
            assignment['state'] = "GRADED"
            assignment['updated_at'] = "2023-01-03T12:00:00Z"
            return jsonify({"data": assignment}), 200

    return jsonify({"error": "Assignment not found"}), 404

if _name_ == '__main__':
    app.run(debug=True)



