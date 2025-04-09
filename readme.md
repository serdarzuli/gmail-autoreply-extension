# Gmail Auto Reply Extension (with AI-Powered Backend)

This project is a combination of a **Chrome Extension** and a **Python FastAPI backend** that automatically generates email replies using GPT. Users can paste the content of received emails into the extension popup, and the AI service will return a professionally written reply.

---

## Features

- ✅ Chrome extension popup with a text input for manual email pasting
- 🤖 Automatic AI-generated replies using GPT
- 🧠 Multilingual support (Turkish and English)
- 🖥️ FastAPI backend
- 🔄 JSON validation and CORS enabled
- 💬 Reply format preserved for direct copy-paste
- 🧪 Easy to test with Postman or directly from the extension

---

## Project Structure

```
gmail-autoreply-extension/
├── backend/
│   ├── app/
│   │   ├── main.py
|   |   ├── config.py
│   │   ├── schemas.py
│   │   └── service.py
│   └── requirements.txt
├── chrome-extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   ├── style.css
│   └── icon.png
└── README.md
```

---

## Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Chrome Extension Setup

1. Open `chrome://extensions/` in Chrome
2. Enable **Developer Mode** (top right corner)
3. Click on **Load unpacked**
4. Select the `chrome-extension/` directory

---

## Usage

- Paste the received email content into the textbox in the popup
- Click the **Reply** button
- View the generated reply formatted as an email
- Copy and paste it directly into your email response

---


## Technologies Used

- Python (FastAPI)
- JavaScript (Chrome Extension)
- HTML/CSS
- OpenAI API (GPT)
- Postman (for backend testing)

---

## License

This project is licensed under the MIT License.
