from flask import Flask, render_template, request, jsonify
import subprocess
import socket
import os
from datetime import datetime

app = Flask(__name__)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route("/")
def index():
    host = request.host
    local_ip = get_local_ip()
    return render_template("index.html", host=host, local_ip=local_ip)

@app.route("/run", methods=["POST"])
def run_command():
    data = request.get_json()
    cmd = data.get("command", "").strip()
    if not cmd:
        return jsonify({"output": "No command provided.", "error": True})

    # Basic safety: block some dangerous patterns (still not fully secure)
    dangerous = ["rm -rf /", "mkfs", ":(){ :|:& };:", "dd if="]
    for d in dangerous:
        if d in cmd:
            return jsonify({"output": "Command blocked for safety.", "error": True})

    try:
        # Run with shell=True for convenience (local use only!)
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr
        if not output.strip():
            output = f"[Command finished with exit code {result.returncode}]"
        return jsonify({
            "output": output,
            "error": result.returncode != 0,
            "code": result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Command timed out after 30 seconds.", "error": True})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}", "error": True})

if __name__ == "__main__":
    port = 5000
    local_ip = get_local_ip()
    print("=" * 50)
    print("  CYBER RED LOCALHOST TERMINAL")
    print("=" * 50)
    print(f"  Local:   http://127.0.0.1:{port}")
    print(f"  Network: http://{local_ip}:{port}")
    print("=" * 50)
    print("  Press Ctrl+C to stop")
    print("=" * 50)
    app.run(host="0.0.0.0", port=port, debug=False)
