import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High resource usage detected!"
    usage_message = f"CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%"
    if message:
        usage_message += f", {message}"
    return usage_message

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')