
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

if __name__ == "__main__":
    if config.app['debug']:
        app.run(debug = True, threaded = True, host = config.app['host'], port = config.app['port'])
    else:
        app.run(debug = False, threaded = True)
