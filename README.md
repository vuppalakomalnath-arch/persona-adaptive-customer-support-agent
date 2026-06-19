# Persona-Adaptive Customer Support Agent

## Overview

The Persona-Adaptive Customer Support Agent is an AI-powered support system that automatically detects customer personas, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), generates persona-specific responses, and escalates unresolved or sensitive issues to a human support representative.

This project demonstrates practical applications of:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Prompt Engineering
* Human-in-the-Loop AI Systems
* Adaptive Customer Communication

---

# Features

## Persona Detection

The system automatically classifies customers into one of three personas:

### Technical Expert

* Uses technical terminology
* Requests logs, APIs, configurations
* Prefers detailed explanations

### Frustrated User

* Uses emotional language
* Reports repeated failures
* Requires empathetic responses

### Business Executive

* Focuses on business impact
* Prefers concise communication
* Interested in outcomes and timelines

---

## Retrieval-Augmented Generation (RAG)

The system:

* Loads support documents from the knowledge base
* Chunks documents into searchable segments
* Generates embeddings
* Stores embeddings in ChromaDB
* Retrieves top relevant documents for user queries

---

## Adaptive Response Generation

Responses are tailored according to the detected persona.

### Technical Expert

* Detailed explanations
* Root cause analysis
* Step-by-step troubleshooting

### Frustrated User

* Empathetic language
* Reassuring tone
* Action-oriented guidance

### Business Executive

* Concise responses
* Impact-focused communication
* Minimal technical jargon

---

## Escalation Logic

The system escalates conversations when:

* Legal issues are detected
* Billing disputes arise
* No relevant documentation is found
* Retrieval confidence is low
* Human intervention is recommended

---

## Human Handoff Summary

When escalation occurs, a structured summary is generated containing:

* Detected persona
* User issue
* Retrieved documents
* Attempted actions
* Recommendation
* Priority level

---

# System Architecture

```text
User Query
     │
     ▼
Rule-Based Persona Detection
     │
     ▼
RAG Retrieval (ChromaDB)
     │
     ▼
Gemini Response Generation
     │
     ▼
Escalation Logic
     │
     ├── No → Response
     │
     └── Yes → Human Handoff Summary
```


# Tech Stack

## Programming Language

* Python 3.13

## LLM

* Google Gemini 2.5 Flash

## Frameworks

* LangChain
* Streamlit

## Embedding Model

* all-MiniLM-L6-v2

## Vector Database

* ChromaDB

## Document Processing

* PyPDF
* TextLoader

## Environment Management

* python-dotenv

---

# Project Structure

```text
persona-support-agent/

│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│   ├── account_lockout.txt
│   ├── api_authentication.txt
│   ├── billing_policy.txt
│   ├── integration_setup.txt
│   ├── password_reset.txt
│   ├── refund_policy.txt
│   ├── security_policy.txt
│   ├── service_outage.txt
│   ├── subscription_upgrade.txt
│   ├── user_management.txt
│   └── troubleshooting_guide.pdf
│
├── chroma_db/
│
└── src/
    ├── persona_detector.py
    ├── rag_pipeline.py
    ├── response_generator.py
    ├── escalation.py
    └── handoff.py
```

---

# Persona Detection Strategy

The system uses a lightweight rule-based classifier to identify personas.

### Technical Expert Keywords

* API
* Token
* Authentication
* Server
* Error
* Logs

### Frustrated User Keywords

* Frustrated
* Nothing works
* Angry
* Urgent
* Terrible

### Business Executive Keywords

* Operations
* Revenue
* Business Impact
* Deadline

This approach reduces API costs and improves performance.

---

# RAG Pipeline Design

## Chunking Strategy

* RecursiveCharacterTextSplitter
* Chunk Size: 500
* Chunk Overlap: 50

## Embedding Model

* all-MiniLM-L6-v2

## Vector Database

* ChromaDB

## Retrieval Strategy

* Top-K Similarity Search
* K = 3

---

# Escalation Logic

Escalation is triggered when:

* Legal keywords are detected
* Billing disputes are detected
* Sensitive account issues arise
* No documents are retrieved
* Retrieval confidence is low

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>

cd persona-support-agent
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

## Run Application

```bash
streamlit run app.py
```

---

# Example Queries

## Technical Expert

```text
Can you explain API authentication failures?
```

## Frustrated User

```text
I've tried everything and nothing works!
```

## Business Executive

```text
How will the service outage affect operations?
```

## Escalation Scenario

```text
I want legal action regarding my billing dispute.
```

## Password Reset

```text
How do I reset my password?
```

---

# Bonus Features Implemented

* Conversation History
* Confidence-Based Retrieval
* Human Escalation Workflow
* Handoff Summary Generation
* Streamlit UI Dashboard

---

# Known Limitations

* Rule-based persona detection may miss complex language patterns.
* Knowledge base is limited to included support documents.
* Free Gemini API quotas may affect testing frequency.
* Multi-turn conversational memory is limited to session history.

---

# Future Improvements

* LangGraph Workflow Orchestration
* Sentiment Analysis
* Advanced Confidence Scoring
* Multi-Agent Architecture
* Human Approval Workflow
* Analytics Dashboard
* Feedback Collection System

---

# Demo Video Checklist

Demonstrate:

1. Project structure
2. Knowledge base documents
3. Persona detection
4. RAG retrieval
5. Technical Expert response
6. Frustrated User response
7. Business Executive response
8. Escalation workflow
9. Human handoff summary
10. Architecture explanation

---

# Author

Komalnath Vuppala

AI Engineering Internship Assignment
