from flask import jsonify, make_response, request, url_for, abort
from flask_httpauth import HTTPBasicAuth
import random

from start_flask import app
from start_flask.models import *


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'httptest':
		return 'httppwd'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

tasks = {
	1: {
		'id': 1,
		'title': u'Java',
		'description': u'Java is a general-purpose, class-based, object-oriented programming language designed for having lesser implementation dependencies', 
		'done': False
	},
	2: {
		'id': 2,
		'title': u'Python',
		'description': u'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.', 
		'done': True
	},
	3: {
		'id': 3,
		'title': u'JavaScript',
		'description': u"JavaScript (often shortened to JS) is a lightweight, interpreted, object-oriented language with first-class functions, and is best known as the scripting language for Web pages, but it's used in many non-browser environments as well",
		'done': True
	},
	4: {
		'id': 4,
		'title': u'MySQL',
		'description': u"MySQL is an Oracle-backed open source relational database management system (RDBMS) based on Structured Query Language (SQL).",
		'done': True
	}
}


def public_uri(task):
	new_task = {}
	for field in task:
		new_task[field] = task[field]

		if field == 'id':
			new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
	
	return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	# curl -i http://localhost:5000/todo/api/v1.0/tasks
	# curl -u httptest:httppwd -i http://localhost:5000/todo/api/v1.0/tasks
	return jsonify({'tasks': [public_uri(task) for task in tasks.values()]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	# curl -i http://localhost:5000/todo/api/v1.0/tasks/1
	task = tasks.get(task_id)
	print(task)
	if not task or len(task.keys()) == 0:
		abort(404)
	
	return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
	# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"HTML/CSS"}' http://localhost:5000/todo/api/v1.0/tasks
	if not request.json or not 'title' in request.json:
		abort(400)
	
	newID = random.getrandbits(32)
	task = {
		'id': newID,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'done': False
	}
	tasks.setdefault(newID, task)
	
	return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	# curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"HTML5/CSS"}' http://localhost:5000/todo/api/v1.0/tasks/taskID
	task = tasks.get(task_id)

	if not task or len(task.keys()) == 0 or \
		not request.json or \
		('title' in request.json and type(request.json['title']) is not str) or \
		('description' in request.json and type(request.json['description']) is not str) or \
		('done' in request.json and type(request.json['done']) is not bool):
		abort(404)
	
	task['title'] = request.json.get('title', task['title'])
	task['description'] = request.json.get('description', task['description'])
	task['done'] = request.json.get('done', task['done'])

	return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	# curl -i -X DELETE http://localhost:5000/todo/api/v1.0/tasks/3
	task = tasks.get(task_id)
	if not task or len(task.keys()) == 0:
		abort(404)
	tasks.pop(task_id)
	
	return jsonify({'result': True})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, threaded=True)