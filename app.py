from flask import Flask, jsonify, Response
import requests
import csv
import io

app = Flask(__name__)

# ファイルIDとAPIキー（今回は共有設定で誰でも見れるのでAPIキー不要）
JSON_FILE_ID = "1a4vJQpCzftfG3Ue1O3AUrA0b0pOdQVtt"
CSV_FILE_ID = "1dgMm81RHbSjnZzkLz69uK1tudpw6zbyq"

def get_drive_file_content(file_id):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

@app.route("/school-policy", methods=["GET"])
def get_school_policy():
    content = get_drive_file_content(JSON_FILE_ID)
    if content:
        try:
            return jsonify(eval(content))  # 注意：JSONで構造化されていること前提
        except Exception:
            return jsonify({"error": "JSONデータの読み込みに失敗"}), 500
    return jsonify({"error": "Google Driveから取得できませんでした"}), 500

@app.route("/student-guidance", methods=["GET"])
def get_student_guidance():
    content = get_drive_file_content(CSV_FILE_ID)
    if content:
        # CSV文字列 → JSON形式に変換
        csvfile = io.StringIO(content)
        reader = csv.DictReader(csvfile)
        return jsonify([row for row in reader])
    return jsonify({"error": "CSVの取得に失敗"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import send_from_directory
import os

@app.route("/openapi.yaml", methods=["GET"])
def serve_openapi():
    return send_from_directory(directory=os.path.dirname(__file__), path="openapi.yaml", mimetype="text/yaml")
