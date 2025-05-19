from flask import Flask, jsonify

app = Flask(__name__)

# 軽量化されたポリシーデータ（コード内に定義）
POLICY_DATA = {
    "policy": {
        "SNS利用": {
            "基本方針": "適切な使い方を指導する",
            "対応例": [
                {"ケース": "軽い言い争い", "対応": "話し合いを促す"},
                {"ケース": "悪口投稿", "対応": "担任が指導し保護者に連絡"},
                {"ケース": "脅迫行為", "対応": "管理職・警察と連携"}
            ]
        }
    }
}

@app.route("/school-policy", methods=["GET"])
def get_policy():
    return jsonify(POLICY_DATA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)