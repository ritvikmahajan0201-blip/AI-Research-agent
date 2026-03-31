Python AI Research Agent

high-speed, autonomous research assistant built with **Langchain**, **Groq**, and **Rich**. This agent leverages the **Llama-3.3-70b-versatile** model to perform real-time internet searches and deep-dive Wikipedia lookups.


🚀 Features
Ultra-Fast Inference: Powered by Groq's LPU (Language Processing Unit) for near-instant responses.

Dual-Layer Research: Combines DuckDuckGo for current events/web search and Wikipedia for structured factual data.

Autonomous Logic: Uses LangChain's reasoning capabilities to decide which tool to use for a specific query.


🛠️ Tech Stack
**LLM MODEL** : llama-3.3-70b-versatile(via Groq)
**FrameWork** : LangChain
**Tools**: DuckDuckGo Search, Wikipedia API
**Environment**: Python 3.10+


📂 Project Structure
---> Main.py  # Core agent logic and LLM initialization
---> Tools.py  # Custom tool definitions (Search, Wiki, etc.)
---> .env # Environment variables (API Keys)
---> requirements.txt # Python dependencies


⚙️ Setup & Installation
1) Clone Repository
    Run the following command in the terminal: git clone https://github.com/your-username/ai-research-agent.git 
    cd ai-research-agent

2) Install Dependencies
    Run the following command: 
          pip install -r requirements.txt

3) Configure Environment Variables
    Create a .env file and add the api key for the Groq llm:
    GROQ_API_KEY=""
    you can retrive you own groq api key using the following link: https://console.groq.com/keys

4) Run the agent using the following command
   python .\main.py
   

🔧 Tools Included

--> DuckDuckGo:	Searches the live web for current news and articles.
--> Wikipedia:	Retrieves summarized factual data and history.










