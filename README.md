# AI-Virtual-Career-Counsellor
AI Virtual Career Counsellor is an NLP-based chatbot built using Python, NLTK, Rasa, and Streamlit. It analyzes user interests and recommends suitable career paths in fields like Technology, Arts, and Commerce. The project includes intent training, text preprocessing, chatbot logic, and a user-friendly web interface.

---

## 🚀 Project Overview

AI Virtual Career Counsellor is an intelligent chatbot that analyzes user input and suggests career paths in domains such as:

- 💻 Technology
- 🎨 Arts
- 💼 Commerce

The chatbot uses Natural Language Processing (NLP) techniques to understand user intent and provide relevant recommendations through a simple and interactive web interface.

---

## 🛠️ Tech Stack

- **Python**
- **Rasa** – Intent classification & dialogue management
- **NLTK** – Text preprocessing
- **Streamlit** – Frontend web interface
- **Scikit-learn** – NLP utilities

---

## 📂 Project Structure

```txt
AI-Virtual-Career-Counsellor/
│
├── actions/ # Custom Rasa actions
├── data/ # Training data (intents & stories)
├── models/ # Trained Rasa models (auto-generated)
├── career_logic.py # Career recommendation logic
├── app.py # Streamlit frontend
├── domain.yml # Rasa domain file
├── config.yml # Rasa pipeline configuration
├── endpoints.yml # Rasa endpoints config
├── requirements.txt # Dependencies
└── README.md
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ADITI-VERMA05/AI-Virtual-Career-Counsellor.git
cd AI-Virtual-Career-Counsellor
```
### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK Data

```bash
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 🧠 Train Rasa Model

```bas
rasa train
```
Run chatbot in terminal:
```bash
rasa shell
```

### 🌐 Run Streamlit Frontend
```bash
streamlit run app.py
```
Open in browser:
```
http://localhost:8501
```

### 🎯 Features

```txt
Intent recognition using Rasa
Text preprocessing using NLTK
Keyword-based career recommendation logic
Interactive web UI using Streamlit
Expandable to include ML-based classification
```

### 📦 Deployment

```txt
The application can be deployed using:

Streamlit Cloud
Render
Hugging Face Spaces
```

### 🎥 Sample Interaction

```txt
User: I love coding and computers
Bot: Suggested Careers: Software Developer, AI Engineer, Data Scientist
```
### 🔮 Future Improvements

```txt
Personality-based career assessment
ML-based recommendation system
Career database integration
User profile tracking
PDF career report generation
```
### 📦 requirements.txt

Create a file:
requirements.txt

Add this:

```txt
rasa==3.6.21
streamlit==1.32.0
nltk==3.8.1
scikit-learn==1.3.2
numpy==1.24.4
pandas==2.0.3
matplotlib==3.7.2
```
If deployment gives dependency issues, use simplified version:

```txt
rasa
streamlit
nltk
scikit-learn
pandas
numpy
matplotlib
```
