
### 1. Install Required Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

Also, download the required spaCy model:

```bash
python -m spacy download en_core_web_sm
```

### 2. Load the Model and Label Encoder


- `HPE_multiclass_query_classifier.pkl` – The trained scikit-learn model
- `label_encoder.pkl` – The fitted label encoder used during training

These are loaded automatically inside the demo script:

```python
model = joblib.load("HPE_multiclass_query_classifier.pkl")
label_encoder = joblib.load("label_encoder.pkl")
```

### 4. Run the Demo

To test the classifier on a sample query, run:

```bash
python DemoFile.ipynb
```

Inside `DemoFile.ipynb`, you can modify the input query like so:

```python
query = "how could HPE’s focus on sustainability have influenced its 2025 profitability?"
```

The output will include:
- Predicted class(es)
- Class probability distribution
- Entropy-based uncertainty warning
- A pie chart visualization (if enabled)

### HOW IT WORKS
This project categorizes financial or business-related questions into several predefined categories based on a hybrid feature approach that integrates:

1. Sentence Embeddings
The all-MiniLM-L6-v2 SentenceTransformer model is employed to produce semantic vector representations of the input query. This captures the contextual meaning of the sentence, allowing the model to comprehend literal and implicit intentions behind the words
2. Auxiliary Feature Extraction
Aside from embeddings, the system calculates a collection of manually designed auxiliary features with spaCy and nltk. These auxiliary features are designed to extract structural, grammatical, and domain-related patterns from the query text, including:

Entity Counts: Counts of named entities in the text (e.g., MONEY, DATE)

Part-of-Speech Tags: Counts of nouns, verbs, conjunctions, and past tense verbs

Semantic Flags: Whether the sentence begins with a question word or contains temporal references such as "Q1", "FY2023", etc.

Keyword-Based Features: Whether there are phrases involving financial metrics (e.g., ARR, EPS), HPE business segments (e.g., hybrid cloud), or reasoning/comparison indicators

Custom Matching: PhraseMatcher from spaCy is utilized to identify HPE-specific terms that normal NER may overlook

These features are output as a fixed-length list and added to the sentence embedding

3. Classification Model
The merged feature vector is input to a model that provides class probabilities.
