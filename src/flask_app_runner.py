# flask_app_runner.py

from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

# Update this path if needed
PYTHON_SCRIPT_PATH = "/home/node/.n8n/train_and_generate_reports.py"

@app.route('/run-python', methods=['GET'])
def run_python_script():
    if not os.path.exists(PYTHON_SCRIPT_PATH):
        return jsonify({"error": f"Python script not found at {PYTHON_SCRIPT_PATH}"}), 404

    try:
        # Run the python script
        result = subprocess.run(["python3", PYTHON_SCRIPT_PATH], capture_output=True, text=True)

        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"message": "Python script executed successfully", "output": result.stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
