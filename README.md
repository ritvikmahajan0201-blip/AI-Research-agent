# 🤖 AI Research Agent

A high-speed, autonomous research assistant built using **LangChain**, **Groq**, and **Python**.
This agent performs real-time web searches and structured knowledge retrieval.

---

## 🚀 Features

* ⚡ **Ultra-Fast Inference**
  Powered by Groq’s LPU for near-instant responses

* 🔍 **Dual-Layer Research**

  * DuckDuckGo → real-time web data
  * Wikipedia → structured knowledge

* 🧠 **Autonomous Tool Selection**
  Uses LangChain reasoning to decide which tool to use

---

## 🛠️ Tech Stack

* **LLM**: `llama-3.3-70b-versatile` (via Groq)
* **Framework**: LangChain
* **Tools**: DuckDuckGo, Wikipedia API
* **Language**: Python 3.10+

---

## 📂 Project Structure

```
.
├── main.py              # Core agent logic
├── Tools.py             # Tool definitions
├── .env                 # API keys (not committed)
├── requirements.txt     # Dependencies
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/ritvikmahajan0201-blip/AI-Research-agent.git
cd AI-Research-agent
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the agent

```bash
python main.py
```

---

## 🔧 Tools Included

* 🌐 **DuckDuckGo** → real-time web search
* 📚 **Wikipedia** → factual summaries

---

## ⚠️ Notes

* Do NOT expose your API keys
* Recommended Python version: **3.10 / 3.11**
* Ensure all dependencies are installed properly

---

## 📌 Future Improvements

* Streamlit UI integration
* Memory-enabled agent
* Multi-agent research system

---
