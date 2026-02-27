from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    """
    Creates task scheduling table.
    Tracks automation lifecycle state.
    """
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Initialize DB on app start
init_db()


@app.route("/schedule", methods=["POST"])
def schedule_task():
    """
    Schedules a robotic command.
    Default state: PENDING
    """
    data = request.json
    command = data["command"]

    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (command, status) VALUES (?, ?)",
        (command, "PENDING")
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task Scheduled Successfully"})


@app.route("/execute/<int:task_id>", methods=["POST"])
def execute_task(task_id):
    """
    Simulates execution of robotic task.
    Updates status to COMPLETED.
    """
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status='COMPLETED' WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task Executed Successfully"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    Returns all scheduled tasks.
    Used for monitoring automation pipeline.
    """
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)