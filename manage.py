from flask_script import Manager, Server
from apps import create_app
from flask_migrate import MigrateCommand

app = create_app()

manage = Manager(app)

manage.add_command('run', Server(host='127.0.0.1', port=8000, threaded=True))

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
