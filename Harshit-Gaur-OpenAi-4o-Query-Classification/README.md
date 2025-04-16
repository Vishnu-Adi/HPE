# Question Classification Using GPT-4o

This project uses OpenAI's GPT-4o model to classify business-related questions into one or more of five categories based on structure, intent, and reasoning depth.

## Categories

The model classifies questions into the following categories:

1. **Factual**  
   Questions with direct, verifiable answers (e.g., "What was HPE’s profit in Q4 2024?").

2. **Aggregate/Time-Based**  
   Questions requiring trend analysis, aggregation, or comparisons over time (e.g., "Compare HPE’s ARR from Q1 2023 to Q4 2024").

3. **Global Sensing**  
   Questions that analyze high-level interactions and strategic context (e.g., "How did the Juniper Networks acquisition impact HPE’s 2024 outlook?").

4. **Reasoning/Inference**  
   Questions needing predictions, causal reasoning, or extrapolation (e.g., "Why did HPE increase EPS guidance in Q3 2024?").

5. **Multi-Part**  
   Questions with multiple connected sub-questions (e.g., "What were HPE’s revenue and EPS in Q3 2024, and how did they compare to Q2 2024?").

> ⚠️ A question can belong to multiple categories. The model will return both, indicating the preferred one.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/question-classifier.git
cd question-classifier
```
---


### 2. Install dependencies

```bash
pip install
```
---

### 3. Set your OpenAI API Key

```bash
set OPENAI_API_KEY=your-api-key-here
```

---

### 4. How to Use

```bash
python classify_question.py
```
---

### 5. Example

```bash
Write the question: What were HPE’s net earnings in Q2 2024?
Factual
```

---

