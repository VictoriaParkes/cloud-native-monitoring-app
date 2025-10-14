import psutil
from flask import Flask, render_template

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
    return render_template(
        "index.html",
        cpu_metric=cpu_percent,
        mem_metric=mem_percent,
        message=usage_message
    )

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
