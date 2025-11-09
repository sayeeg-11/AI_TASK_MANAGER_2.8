from flask import Blueprint, jsonify, request
from models import db, Task, User
from datetime import datetime

task_bp = Blueprint("task_bp", __name__)

# -----------------------------
# CREATE TASK
# -----------------------------
@task_bp.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    deadline = data.get("deadline")
    
    task = Task(title=title, description=description, deadline=deadline)
    db.session.add(task)
    db.session.commit()
    
    return jsonify({"message": "Task created", "task": task.to_dict()}), 201


# -----------------------------
# GET ALL TASKS
# -----------------------------
@task_bp.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200


# -----------------------------
# ASSIGN TASK TO USER
# -----------------------------
@task_bp.route("/api/tasks/<int:task_id>/assign", methods=["POST"])
def assign_task(task_id):
    data = request.get_json()
    user_id = data.get("user_id")
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if user_id is None:
        task.assigned_user = None
    else:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        task.assigned_user = user

    db.session.commit()
    return jsonify({"message": "Assignment updated", "task": task.to_dict()}), 200


# -----------------------------
# GET TASKS FOR SPECIFIC USER
# -----------------------------
@task_bp.route("/api/tasks/user/<int:user_id>", methods=["GET"])
def get_user_tasks(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    tasks = Task.query.filter_by(assigned_to_user_id=user_id).all()
    return jsonify([t.to_dict() for t in tasks]), 200


# -----------------------------
# GET UNASSIGNED TASKS
# -----------------------------
@task_bp.route("/api/tasks/unassigned", methods=["GET"])
def get_unassigned_tasks():
    tasks = Task.query.filter_by(assigned_to_user_id=None).all()
    return jsonify([t.to_dict() for t in tasks]), 200


# -----------------------------
# GET ALL USERS
# -----------------------------
@task_bp.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200


# -----------------------------
# CREATE USER (simple)
# -----------------------------
@task_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    role = data.get("role", "Member")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    user = User(username=username, email=email, role=role)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "user": user.to_dict()}), 201


# -----------------------------
# GET SINGLE TASK
# -----------------------------
@task_bp.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200


# -----------------------------
# UPDATE TASK
# -----------------------------
@task_bp.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json() or {}
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    deadline = data.get("deadline")  # YYYY-MM-DD

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    if deadline is not None:
        try:
            task.deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid deadline format. Use YYYY-MM-DD"}), 400

    db.session.commit()
    return jsonify({"message": "Task updated", "task": task.to_dict()}), 200


# -----------------------------
# DELETE TASK
# -----------------------------
@task_bp.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
