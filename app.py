from flask import Flask, request, jsonify
from model.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    global task_id_control
    new_task = Task(id=task_id_control, title=data["title"], description=data["description"], completed=False)
    task_id_control+=1
    tasks.append(new_task)
    return jsonify({"message": "Task created"})

debugando = __name__ == '__main__'
app.run(debug=debugando)

