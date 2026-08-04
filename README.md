<<<<<<< HEAD
Project title
OmniInsight-AI

An intelligent OmiInsight-AI that combines a Large Language Model (LLM) with external tools to answer questions about employee data. Instead of hardcoding every query, the agent reasons about the user's request, decides whether a tool is needed, executes the appropriate tool, and generates a natural language response.

This project demonstrates the fundamentals of AI Agents, tool calling, memory, and local LLM inference using Ollama.

Features
- AI Agent architecture
- Local LLM using Ollama (Qwen2.5)
- Automatic tool selection
- HR dataset analytics
- Conversation memory
- Follow-up question handling
- Modular code structure
- Easy to extend with new tools
- Project Architecture

OmniInsight-AI/
│
├── agent.py                 # Main AI Agent logic
├── app.py                   # Command line interface
├── memory.py                # Conversation memory
│
├── dataset/
│   └── data.json            # Employee dataset
│
├── tools/
│   ├── loader.py            # Dataset loader
│   ├── query.py             # HR analytics tool
│   ├── classifier.py        # Document classifier
│   ├── validator.py         # Output validator
│   └── tool.py              # Abstract Tool class
│
├── requirements.txt
├── README.md

Project Description

The AI HR Analytics Agent allows users to ask HR-related questions in natural language.

Instead of writing SQL queries or Python code, users can ask questions such as:

Q. Which employee has the highest salary?
Q. What is the average salary?
Q. How many employees left the company?
Q. Which department does that employee belong to?

The agent first reasons whether it needs external data. If required, it calls a dataset query tool, retrieves the necessary information, and then generates a final response using the LLM.

The project follows a simple ReAct (Reasoning + Acting) workflow.

User Question
      │
      ▼
LLM decides whether tool is needed
      │
      ▼
Query Dataset Tool
      │
      ▼
Observation
      │
      ▼
LLM generates final answer
      │
      ▼
Conversation stored in memory

Technologies Used
- Python 3.10+
- Ollama
- Qwen2.5:3B
- JSON Dataset
- Object-Oriented Programming
- AI Agent Design Pattern

Setup Instructions
1. Clone Repository
git clone https://github.com/yourusername/OmniInsight-AI.git

cd OnmiInsight-AI
2. Create Virtual Environment

Windows

python -m venv venv

venv\Scripts\activate

Mac/Linux

python3 -m venv venv

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

5. Install Ollama

Download Ollama from

https://ollama.com

Install according to your operating system.

Verify installation

ollama --version

5. Download the Model
ollama pull qwen2.5:3b

You may replace the model with any Ollama-supported LLM.

Examples:

llama3

mistral

gemma3

phi4
Running the Project

Start the Ollama server.

ollama serve

Open another terminal.

Run the application.

python app.py

You should see

AI HR Analytics Agent

Ask a question:

Example questions

Q. Who has the highest salary?

Q. What is the average salary?

Q. How many employees left the company?

Q. Which department does that employee work in?

Q. What role does that person have?

Exit using

exit

Agent Workflow
Step 1

Receive user question.

↓

Step 2

LLM determines whether a tool is required.

↓

Step 3

If needed, execute query_dataset().

↓

Step 4

Collect observation.

↓

Step 5

Generate final answer using observation.

↓

Step 6

Store conversation in memory.

Dataset Information

The project uses an employee HR dataset stored as:

dataset/data.json

Each employee record contains information such as:

{
    "Age": 41,
    "Department": "Sales",
    "JobRole": "Sales Executive",
    "MonthlyIncome": 5993,
    "Attrition": "Yes"
}

Current fields used by the project:

Age
Department
JobRole
MonthlyIncome
Attrition

Additional fields can be added without changing the agent architecture.

Current Supported Queries

The dataset tool currently supports:

Highest Salary
Example
Who has the highest salary?

Lowest Salary
Example
Who has the lowest income?

Average Salary
Example
What is the average salary?



The conversation memory allows the agent to understand references like:

that employee
that person
what role
which department
Document Classifier

The project also includes a basic document classifier.

Supported document types:

Document	Detection
Invoice	invoice, total amount
Resume	experience, education
Receipt	receipt
Unknown	otherwise

This module can be extended to OCR or PDF processing in future versions.

Memory System
The memory module stores previous conversations.
Example
conversation_history = [
    {
        "user": "...",
        "assistant": "..."
    }
]

This enables follow-up questions without repeating context.

Requirements
Create a file named requirements.txt
ollama>=0.5.0
Python standard libraries used:
json

No additional libraries are currently required.

Future Improvements

Some planned enhancements include:

PDF document processing
OCR using Tesseract or EasyOCR
Resume analysis
Invoice extraction
Retrieval-Augmented Generation (RAG)
Vector database integration (FAISS or ChromaDB)
Multi-tool agent architecture
Web interface using Streamlit or FastAPI
Employee search by name
Natural language to SQL
Visualization dashboard
REST API support
Example Session
AI HR Analytics Agent

Ask a question:
Who has the highest salary?

Thought:
Analyze user request and decide if a tool is needed.

Action:
query_dataset

Observation:
{
  "employee": {
      "department": "Research & Development",
      "role": "Research Director",
      "monthly_income": 19999
  }
}

Answer:
The employee with the highest monthly salary earns $19,999 and works as a Research Director in the Research & Development department.

Ask a question:
Which department does that employee belong to?
Answer:
The employee works in the Research & Development department.

Author

Prajakta Khare
Boston University – Computer Science
=======


#todo
# OmniInsight-AI
An Agentic RAG-Powered Analytics Assistant for Enterprise Documents
>>>>>>> 
