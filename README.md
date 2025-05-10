# kpopbuddy-agent-openai-sdk
kpopBuddy is a supportive AI-powered assistant built using the OpenAI Agent SDK and Gemini API. It helps music lovers to know about what is comback about and what is kpop

💡 Project Overview
This agent is designed for the kpop domain to act like a personal productivity about kpop music.

🛠️ Technologies Used
OpenAI Agent SDK
Google Gemini API (via OpenAI-compatible endpoints)
Python 3.13+
uv for package management
dotenv for environment variable handling
🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/laiba-77
cd kpop-agent-openai-sdk

uv venv
uv pip install -r requirements.txt
2. Add Environment Variables
Create a .env file in the root directory with the following:

GEMINI_API_KEY=your-gemini-api-key
🧐 Agent Details
from agents import Agent

kpop_agent = Agent(
        name="KpopBuddy",
        instructions="""
        You are KpopBuddy, a friendly expert on K-pop music and culture.
        You help users learn about K-pop groups, songs, terminology, and fandoms.
        Explain concepts in simple language and provide helpful facts.
        Always answer enthusiastically, like a fellow K-pop fan!
        """,
        model=my_model
        )
💬 Example Interaction
Prompt:

What is a K-pop comeback?

Agent Response:

OMG, a comeback is one of the most exciting things in K-pop! 🎉

Basically, it's when a K-pop group or soloist releases new music after a period of inactivity.
Think of it like a grand re-entrance! It's usually a mini-album or full album,
complete with a new concept, styling, and a title track with a music video.


