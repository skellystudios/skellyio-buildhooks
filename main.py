from flask import Flask
from flask import abort
from subprocess import call

app = Flask(__name__)

@app.route('/update_jekyll', methods=['POST'])
def update_jekyll():
	try:
		skelly_io_dir = "/var/www/skelly-io/skellyio-jekyll"
		call(["git", "pull"], cwd=skelly_io_dir)
		call(["jekyll", "build"], cwd=skelly_io_dir)
	except:
	        abort(500)
	return 'ok'


@app.route('/status', methods=['POST'])
def status():
	return "success"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
