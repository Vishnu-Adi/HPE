# Multi-Model Question Classifier

This project provides a command-line tool for classifying natural language questions into one or more of five categories: **Factual**, **Aggregate/Time-based**, **Global Sensing**, **Reasoning/Inference**, and **Multi-Part**. It supports multiple LLM backends, including Gemini, Mistral, LLaMA 3, and Phi-4.

## ✨ Features

- Interactive CLI interface for classification  
- Prompt designed for fine-grained multi-class question labeling  
- Easy switching between models via separate scripts  
- Uses APIs from Google, Azure, and Mistral  

## 🧠 Classification Categories

Each input is classified into one or more of the following:

- **Factual**  
- **Aggregate/Time-based**  
- **Global Sensing**  
- **Reasoning/Inference**  
- **Multi-Part**  

(See `prompt.py` for exact definitions.)

## 📁 File Structure

```plaintext
.
├── gemini.py         # Uses Google Gemini 2.0 Flash model
├── llama3.py         # Uses Meta’s LLaMA 3 via Azure Inference
├── mistral.py        # Uses Mistral via mistralai SDK
├── phi4.py           # Uses Phi-4 model via Azure Inference
├── prompt.py         # Shared classification prompt used by all models
├── requirements.txt  # Project dependencies
└── README.md         # Documentation
```

## 🧪 Requirements

- Python 3.8+
- API keys for each respective model provider:
  - `GOOGLE_API_KEY` for Gemini  
  - `MISTRAL_API_KEY` for Mistral  
  - `LLAMA_API_KEY` for LLaMA 3 (Azure)  
  - `PHI_API_KEY` for Phi-4 (Azure)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-model-classifier.git
cd multi-model-classifier
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a `.env` file in the project root and add your API keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
MISTRAL_API_KEY=your_mistral_api_key
LLAMA_API_KEY=your_azure_llama3_api_key
PHI_API_KEY=your_azure_phi4_api_key
```

---

## 🚀 Run the Classifier

Choose a model backend to run:

**Google Gemini**
```bash
python gemini.py
```

**Mistral**
```bash
python mistral.py
```

**Meta LLaMA 3 (Azure)**
```bash
python llama3.py
```

**Phi-4 (Azure)**
```bash
python phi4.py
```

### 🧾 Example Usage

```plaintext
Write the question: What was the highest revenue in fiscal year 2024?
Response: Aggregate/Time-based

Write the question: exit
```

---
