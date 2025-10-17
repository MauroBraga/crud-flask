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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_dict = [task.to_dict() for task in tasks]
    output = jsonify({"tasks": tasks_dict,"total": len(tasks_dict)})
    return output

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict())
    return jsonify({"message": "Task not found"}), 404

debugando = __name__ == '__main__'
app.run(debug=debugando)

