# School Policy API (Lightweight Version)

This is a lightweight Flask-based API designed to serve static JSON data representing a school's guidance policy. It is intended for use with GPTs via Actions integration and is optimized for deployment on Render with uptime stability maintained via UptimeRobot.

---

## ✨ Features
- Returns predefined school policy in JSON format
- Optimized for fast startup and minimal resource usage
- Can be deployed for free using Render
- Works well with GPTs (GPT-3.5 or GPT-4) using Actions

---

## 📚 JSON Response Format
**GET /school-policy**
```json
{
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
```

---

## ⚖️ Requirements
```
Flask==2.3.2
gunicorn==21.2.0
```

---

## 🚀 Deployment on Render

1. Fork or clone this repository to your GitHub account.
2. Go to [https://dashboard.render.com/](https://dashboard.render.com/).
3. Click "New Web Service".
4. Connect your GitHub repository.
5. Set the following values:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: `Python`
   - **Plan**: `Free`
6. Deploy and get your endpoint URL, e.g. `https://school-policy-api.onrender.com/school-policy`

---

## ⏰ Keep It Awake with UptimeRobot

1. Go to [https://uptimerobot.com/](https://uptimerobot.com/) and create an account.
2. Click "Add New Monitor"
3. Set:
   - Type: `HTTP(s)`
   - URL: Your Render deployment URL
   - Interval: `Every 5 minutes`
4. Save. Your API will now stay awake.

---

## 🧑‍🏫 Usage with GPTs (Actions)

- Create an OpenAPI spec with a `GET /school-policy` endpoint
- Add it to your custom GPT's Actions section
- Prompt GPT like:
  > "SNSで悪口を書かれた場合、学校としてどう指導すべきか？"

GPT will call your API, read the policy, and respond accordingly.

---

## ✅ License
MIT

---

Happy instructing! 🚀
