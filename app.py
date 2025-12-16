from flask import Flask, render_template
from flask_cors import CORS
from models import db
from routes.tasks import task_bp
from components.sidebar import sidebar_navigation

import os

app = Flask(__name__)
CORS(app)

# Configure SQLite (you can replace with Postgres if needed)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Register routes
app.register_blueprint(task_bp)

# Simple homepage
@app.route("/")
def index():
    return render_template("assign.html")

if __name__ == "__main__":
    app.run(debug=True)
