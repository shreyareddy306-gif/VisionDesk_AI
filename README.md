🦺 VisionDesk AI – Workplace Safety Intelligence Platform

An AI-powered workplace safety platform designed to monitor PPE compliance, analyze safety documents, and provide intelligent safety insights through computer vision and AI.

📌 Project Overview

VisionDesk AI is a workplace safety intelligence application that helps organizations monitor safety compliance and manage workplace safety information.

The platform combines computer vision, document processing, and an AI-powered assistant to support safety monitoring, identify potential PPE violations, and provide context-aware safety recommendations.

🎯 Objectives

- Automate PPE detection using computer vision.
- Monitor workplace safety compliance.
- Identify and report potential safety violations.
- Extract useful information from safety documents.
- Provide intelligent answers using a Retrieval-Augmented Generation (RAG) system.
- Generate compliance reports and workplace safety insights.

✨ Key Features

🔐 User Authentication

- User registration and login.
- Authentication and account management.
- Password recovery functionality, where configured.

📊 Workplace Intelligence Dashboard

- View workplace safety information.
- Monitor PPE compliance and violations.
- Access safety analytics and alerts.

🦺 PPE Detection

- Upload workplace images and videos.
- Detect workers and personal protective equipment (PPE).
- Identify safety-related violations using a YOLO-based computer vision model.
- Generate safety analysis results.

📄 Document Processing

- Upload workplace safety documents.
- Extract text and relevant information.
- Organize safety knowledge for searching and question answering.

🤖 AI Safety Assistant

- Ask questions about workplace safety.
- Retrieve relevant information from the knowledge base.
- Generate context-aware answers and safety recommendations.

📈 Compliance Reports

- Review workplace safety findings.
- Generate PDF compliance reports.
- Access safety information for further analysis.

🛠️ Technologies Used

Technology| Purpose
Python| Backend development
Flask| Web application framework
HTML, CSS, JavaScript| Frontend development
YOLOv8| PPE detection
OpenCV| Image and video processing
MongoDB| Data storage, where configured
RAG| Document-based knowledge retrieval
LangGraph| AI agent workflow, where configured
PyPDF2| PDF text extraction
python-docx| Word document processing

🏗️ System Workflow

1. User logs in or registers.
2. User accesses the workplace intelligence dashboard.
3. Workplace images or videos are uploaded for PPE detection.
4. The computer vision model analyzes the media and identifies PPE-related findings.
5. Safety documents are uploaded and processed into searchable knowledge.
6. The AI assistant retrieves relevant information to answer workplace safety questions.
7. Safety findings and analytics can be reviewed through the dashboard and reports.

📂 Project Structure

VisionDesk_AI/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── live_detection.html
│   ├── upload.html
│   ├── upload_document.html
│   ├── rag_chat.html
│   ├── knowledge_search.html
│   ├── documents.html
│   └── settings.html
│
├── uploads/
│
├── app.py
├── config.py
├── forms.py
├── security.py
├── check_model.py
├── rag_system.py
├── agent_workflows.py
├── agent_workflows_llm.py
├── setup_mongodb.py
├── requirements.txt
└── README.md

Note: The structure above highlights key files. Your repository may contain additional files, models, and folders.

⚙️ Installation and Setup

Prerequisites

- Python 3.10 or a compatible version supported by the project dependencies.
- Git.
- Visual Studio Code (recommended).
- MongoDB, if required by your configuration.
- Required AI service credentials, if your enabled features use external APIs.

1.  Activate the virtual environment
 Windows:
venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Configure environment variables

Create a ".env" file in the project root if required by your configuration.

Add the environment variables needed by your application, such as database connection details and API credentials.

# Example placeholders – use the variables required by your code
MONGODB_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key

Do not commit real passwords, API keys, or other secrets to GitHub.

4. Run the application

python app.py

Open the local URL displayed in the terminal, commonly:

http://127.0.0.1:5000

Follow the project's configuration and terminal output if it uses a different port or startup command.

🧪 Testing

Test the main application workflows:

- User registration and login.
- Dashboard loading and navigation.
- Image and video upload.
- PPE detection and result display.
- Document upload and text extraction.
- Knowledge search and AI assistant responses.
- Compliance report generation.

🚀 Future Enhancements

- Real-time workplace safety monitoring.
- Improved PPE detection accuracy.
- Advanced safety analytics and visualizations.
- More document formats and knowledge sources.
- Enhanced alerting and notification functionality.
- Cloud deployment and scalable data storage.

