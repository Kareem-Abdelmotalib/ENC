from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def run_python_file():
    try:
        output = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        return f"<pre>{output.stdout}</pre>"
    except Exception as e:
        return f"<pre>Error: {str(e)}</pre>"

if __name__ == "__main__":
    app.run()
