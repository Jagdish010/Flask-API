from datetime import datetime
from start_flask import *


class Tasks(db.Model):
	__tablename__ = 'flask_Tasks'

	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('created', db.String(120))
	description = db.Column('qty', db.Text, default='')
	done = db.Column('amount', db.Boolean, default='')

	def __repr__(self):
		return "Tasks ({}, {})".format(self.id, self.title)