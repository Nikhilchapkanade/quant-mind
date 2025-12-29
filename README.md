# QuantMind AI

This repository contains the code for a local AI agent that combines **Deep Learning** (for numbers) and **RAG** (for text) to analyze stocks. It runs on your computer and connects to the Claude Desktop App.

## Table of Contents
1. Project Description
2. How It Works
3. Prerequisites
4. Installation
5. Connecting to Claude
6. Usage (Making Predictions)

## 1. Project Description
This project aims to build a "Financial Analyst" that lives on your laptop. Most AI just reads text, but QuantMind actually does math. It uses a **Long Short-Term Memory (LSTM)** neural network to predict if a stock price will go up or down based on its history. At the same time, it uses **RAG (Retrieval Augmented Generation)** to read analyst notes and explain the *why* behind the move.

The goal is to show how Agentic AI can use tools to do complex jobs that a normal chatbot can't do.

## 2. How It Works
The system has two main parts:
* **The Quantitative Brain (`brain_dl.py`):** Fetches live data from Yahoo Finance and trains a TensorFlow model in real-time to predict the next day's closing price.
* **The Qualitative Brain (`brain_rag.py`):** specific financial reports to find context (like "delayed product launch") using Vector Search.

## 3. Prerequisites
Before you begin, ensure you have the following installed:
* Python 3.10 or higher
* Claude Desktop App (installed and logged in)
* A curiosity to see AI do math!

## 4. Installation

**1. Clone the repository**
git clone  [https://github.com/Nikhilchapkanade/quant-mind.git](https://github.com/Nikhilchapkanade/quant-mind.git)

2. Set up the environment (Windows)
Bash
python -m venv venv
venv\Scripts\activate
(If you are on Mac/Linux, use source venv/bin/activate instead)

3. Install Requirements
Bash
pip install -r requirements.txt
Note: This might take a minute because it is installing TensorFlow and other heavy AI libraries.

4. Connecting to Claude
To let Claude talk to this code, you need to add it to the config file.

Open your Claude config file. On Windows, it is located at: %APPDATA%\Claude\claude_desktop_config.json

Add this entry to the file:
JSON

{
  "mcpServers": {
    "quant-mind": {
      "command": "C:\\Users\\nikhi\\quant-mind\\venv\\Scripts\\python.exe",
      "args": [
          "C:\\Users\\nikhi\\quant-mind\\server.py"
         ]
    }
  }
}


5. Usage (Making Predictions)
Once the server is configured, simply open the Claude Desktop App. You don't need to run any extra commands;
Claude starts the server automatically.

Example Prompt:

"Consult analyst notes for Tesla (TSLA) and predict its stock trend."

What happens next:

The agent downloads the last 2 years of Tesla data.

It trains a neural network on your graphics card (or CPU).

It reads the internal notes.

It gives you a final report: "Prediction: DOWNWARD TREND 📉"
