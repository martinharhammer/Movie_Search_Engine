# **Movie Search Engine**  

As part of a Information Retrieval course I took we had to configure a search engine for movies. The objective is to enhance a **minimum viable search engine** to retrieve the correct documents for predefined queries using **Elasticsearch**.

## **Project Overview**
- The dataset consists of **~25,000 crawled Wikipedia pages** of English-speaking movies from 2000 onwards.
- The search engine is optimized using **tokenizers, filters, and analyzers** for improved text retrieval.
- The exercise is divided into a **pre-task** and **two milestones**, with tests determining progress and grading.

## **Key Steps**
### **1. Data Preprocessing**
- Parsed and cleaned **Wikipedia movie pages**.
- Extracted relevant fields such as **title, release year, genre, plot summary, and cast**.

### **2. Text Analysis Pipeline**
- Implemented **tokenizers** (e.g., whitespace, word-based) to break movie descriptions into searchable terms.
- Applied **filters** (e.g., stopword removal, stemming, lowercasing) to improve retrieval efficiency.
- Used **analyzers** (combining tokenization and filtering) to standardize queries and movie text.

### **3. Search Engine Configuration**
- Set up an **inverted index** for fast lookups.
- Experimented with different **ranking algorithms** (e.g., TF-IDF, BM25) to improve result relevance.
- Implemented **synonym expansion** and **fuzzy matching** to enhance query flexibility.

### **4. Query Execution & Evaluation**
- Evaluated **retrieval effectiveness** by testing various queries and adjusting indexing parameters.

## **Key Features**
- **Elasticsearch-powered search engine** for movie retrieval.
- **Automated testing** to evaluate query accuracy (`pytest`).
- **Kibana support** for Elasticsearch debugging.
- **Streamlit frontend** for interactive searches.
