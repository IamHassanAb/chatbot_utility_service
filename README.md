# Chatbot Utility Service
![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![LangChain](https://img.shields.io/badge/LangChain-Routing-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorStore-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-black)
![Status](https://img.shields.io/badge/Status-Demo%20Project-informational)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A modular **prompt-routing service** that routes queries to specialized prompts for clearer, more specific LLM responses.
Built to showcase a clean routing architecture using FastAPI + LangChain + FAISS.

---

## Overview

This service demonstrates how structured routing strategies can improve chatbot responses by directing user queries through specialized prompt chains. It is designed as a lightweight, modular backend that developers can extend or integrate into their own LLM systems.

**Primary goal:** demonstrate prompt routing architecture and modular LangChain chains.

---

## Features

* Modular prompt routing architecture
* FastAPI-based API service
* LangChain routing, chains, and output parsers
* FAISS vector store for retrieval
* Chat message history support
* Designed as a demo-ready, extensible backend

---

## Tech Stack

* FastAPI — API layer
* LangChain — routing + chains
* FAISS — embeddings / retrieval
* OpenAI — LLM provider (currently only supported)

---

## Requirements

* Python **3.10**
* FAISS installed (native dependency)
* OpenAI API key

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Available Endpoints

* `GET /check_status`
* `POST /generate_response`

> Some endpoints in the codebase are experimental or under development.

---

## Example Usage

```python
from utils.utils import faiss_embeddings
from entrypoint.mainChain import Chatbot

input_text = "What are the legal implications of breaking a contract?"

bot = Chatbot(vector_store=faiss_embeddings)
response = bot.chat(input_text)
print(response)
```

---

## Project Structure

```
chatbot_utility_service/
├── agents/
├── chains/                # Routing + modular chains
├── llms/                  # LLM integrations
├── pds/                   # Data orchestration layers
├── prompts/               # Prompt templates
├── utils/
│   ├── memory.py          # (experimental)
│   ├── tools.py           # (experimental)
├── main.py
├── mainChain.py
├── Procfile
└── requirements.txt
```

---

## Deployment

This project has been deployed using **Railway** (example setup via Procfile).
Other platforms should work with minimal changes.

---

## Limitations

* OpenAI-only support (for now)
* No automated tests
* FAISS requires native installation
* Some modules are experimental

---

## Future Improvements

* Async processing and background workers
* Redis / semantic caching for cost optimization
* Multi-LLM provider support

---

## Author

Built by **IamHassanAb** — open an issue for questions or feedback.
* Write a **short portfolio version** tailored for recruiters
* Generate a `.env.example` and polished repo metadata (description + tags)
