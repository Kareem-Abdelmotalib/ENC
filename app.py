from flask import Flask
import subprocess

app = Flask(name)

@app.route("/")
def home():
    return "Welcome! Visit /run to execute the encryption script."

@app.route("/run")
def run_script():
    try:
        # تشغيل ملف التشفير
        result = subprocess.run(['python', 'encryptor.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>"
    except Exception as e:
        return f"<pre>Error: {str(e)}</pre>"

if name == "main":
    app.run(host="0.0.0.0", port=5000)  # اجعل التطبيق يستمع على جميع العناوين
