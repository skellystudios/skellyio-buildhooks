from flask import Flask
from subprocess import call

app = Flask(__name__)

@app.route('/update_jekyll', methods=['POST']):
def update_jekyll():
	try:
		skelly_io_dir = "/var/www/skelly-io"
		call(["git", "pull"], cwd=skelly_io_dir)
		call(["jekyll", "build"], cwd=skelly_io_dir)
	except:
		pass
	return 'ok'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
