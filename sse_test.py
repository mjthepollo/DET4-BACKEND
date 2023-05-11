import base64
import os
import time

from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sse_test.html")

@app.route('/stream')
def stream():
    def generate():
        for _ in range(3):
            file_path = "tests/src/test_input.mp3"
            if os.path.exists(file_path):
                print("File exist!")
                with open(file_path, 'rb') as f:
                    filedata = f.read()
                    yield 'Content-Type: text\n'
                    yield 'Content-Length: {}\n'.format(len(filedata))
                    yield 'data: HelloWorld!\n'
                    yield 'X-File-Name: song1.mp3\n\n'
            else:
                print("No file!")
            time.sleep(1)

    response = Response(generate(), mimetype='text/event-stream')
    return response

app.run(debug=True, threaded=True)