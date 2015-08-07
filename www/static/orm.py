from orm import Model, StringField, IntergerField

class User(Model):
	__table__ = 'users'

	id = IntergerField(primary_key=True)
	name = StringField()

	#创建实例:
	user = User