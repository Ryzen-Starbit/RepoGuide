# 🚀 RepoGuide – Code Documentation Navigator: 

RepoGuide is an intelligent repository exploration tool that helps developers quickly understand unfamiliar codebases. It allows users to load a GitHub repository and ask questions about the code, helping developers onboard faster, analyze logic, and navigate projects efficiently.

## 🎥 Demo

[![RepoGuide Demo](https://img.youtube.com/vi/knJW_YISkhw/maxresdefault.jpg)](https://youtu.be/knJW_YISkhw)

▶️ **[Watch the full demo on YouTube](https://youtu.be/knJW_YISkhw)**

## 📌 Problem:

Understanding a new codebase is difficult due to:
- Large project structures
- Lack of documentation
- Complex dependencies
= Unknown module interactions

RepoGuide solves this by enabling intelligent code querying and repository analysis.

## 🎯 Project Objective: 

To create a tool that:

- Automatically analyzes repositories
- Enables natural-language code queries
- Helps developers understand projects faster

## ✨ Features: 

- Load GitHub repositories directly
- Ask questions about project code
- Code complexity estimation
- Risk detection in complex files
- Dependency & change impact insights
- Intelligent code explanations
- Developer-friendly interface

## 🏗 System Architecture:

```
User Query
↓
Frontend UI (Streamlit)
↓
Backend API (FastAPI)
↓
Repository Loader & Parser
↓
Embedding Generation
↓
Vector Index (FAISS)
↓
Retriever + Answer Generator
↓
Response to User
```

## 🛠 Tech Stack:

### 1. Frontend
   - Streamlit
### 2. Backend
   - FastAPI
   - Uvicorn
### 3. AI / Processing
   - Sentence Transformers
   - FAISS vector search
### 4. Other Tools
   - Python
   - Git repository cloning utilities

## ⚙ Installation: 

1. Clone repository -
git clone <your-repository-url>
cd RepoGuide

2. Create virtual environment -
python -m venv venv

3. Activate:
- Windows: venv\Scripts\activate
- Linux/macOS: source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

## ▶ Running the Application:

1. Start backend server: uvicorn backend.main:app --reload
2. Start frontend: streamlit run frontend/app.py

The application will open in your browser.

## 📖 Usage:

- Launch backend and frontend.
- Enter repository URL.
- Load repository.
- Ask questions about the code.
  
## 📂 Project Structure:

```
RepoGuide/
│
├── backend/
│ ├── main.py
│ ├── retriever.py
│ ├── loader.py
│ └── utils.py
│
├── docs/
│ └── documetaion.md
│
├── frontend/
│ └── app.py
│
├── data/
├── requirements.txt
└── README.md
```

## 🤝 Contribution: 

Contributions and suggestions are welcome.
Steps:
- Fork repository
- Create feature branch
- Submit pull request
