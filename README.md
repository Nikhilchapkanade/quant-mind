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
```bash
git clone [https://github.com/YOUR_USERNAME/quant-mind.git](https://github.com/YOUR_USERNAME/quant-mind.git)
cd quant-mind
