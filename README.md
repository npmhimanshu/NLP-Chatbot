🤖 Intelligent NLP Chatbot with Dashboard
---

📄 Project Description
---
The Intelligent NLP Chatbot is a Python-based web application that understands and responds to user queries using Natural Language Processing (NLP). It leverages spaCy for text processing and pattern matching, providing an interactive chatbot experience.one

It also features a dynamic web dashboard built with FastAPI and Plotly, allowing visualization of user interactions and query trends for better analytics.

✨ Features
---
💬 Interactive Chatbot: Handles greetings, help requests, and other predefined intents.

🧠 NLP-Based Responses: Uses spaCy to process and understand user messages.

📊 Web Dashboard: Displays bar charts showing user queries by intent.

🌐 REST API: Built with FastAPI, easy to integrate with other platforms.

🔧 Extensible: Can be integrated with Telegram/Discord or upgraded with ML-based intent classification.

🛠️ Technologies Used
---
🐍 Python 3.x

⚡ FastAPI – Web framework for APIs and HTML pages

🧠 spaCy – Natural Language Processing library

📈 Plotly – Interactive charts and visualizations

📝 Jinja2 – HTML templating

🚀 Uvicorn – ASGI server to run FastAPI



📁 Project Structure
nlp_chatbot/
│
├── app/

│   ├── __init__.py        # Package marker

│   ├── main.py            # FastAPI app

│   ├── chatbot.py         # NLP chatbot logic

│   ├── intents.json       # Predefined intents

│   └── templates/

│       └── index.html     # Dashboard HTML page
│

├── requirements.txt

└── README.md



⚡ Setup Instructions
---
1️⃣ Clone the repository
git clone <your-repo-url>
cd nlp_chatbot

2️⃣ Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

3️⃣ Run the application
python -m uvicorn app.main:app --reload


4️⃣ Access the app
---
🌐 Dashboard/Home Page: http://127.0.0.1:8000/

💬 Chatbot API: POST request to http://127.0.0.1:8000/chat/
 with JSON body:

{
  "message": "Hello"
}

🧩 How It Works
---
User sends a message to /chat/.

chatbot.py processes the message using spaCy and matches it to predefined intents.

The bot returns a response from the matched intent.

The home page / displays a Plotly bar chart summarizing user queries by intent.

🚀 Future Enhancements
---
🧠 Machine learning-based intent classification for smarter responses.

📲 Real-time integration with Telegram/Discord.

💾 Store conversation history in a database for analytics.

📊 Advanced dashboards showing trends, sentiment, and response quality.


🔗 References
---
FastAPI Documentation

spaCy NLP Library

Plotly Python





