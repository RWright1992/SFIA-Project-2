#importing app object from __init__.py
from application import app
# if the file is being run directly, and not imported, then start the application.
if __name__ == '__main__':
	app.run(host='0.0.0.0')
