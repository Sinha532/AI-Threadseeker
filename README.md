# ThreadSeeker - AI Social Content Explorer

## What is ThreadSeeker?

ThreadSeeker is a cool AI project that helps you find interesting social media threads (like tweets) based on what you type. Want to see posts about AI, health, or tech? Just type a query, and it shows you the best matching threads! It uses smart AI to understand your words and find relevant content.

This project is built using only Python, so it’s easy to understand and run. It’s perfect for showing off AI skills in internships or jobs.

---

## Why I Made This?

I wanted to build something useful with AI that can search social media posts smartly. ThreadSeeker finds threads on topics like AI ethics, humor, health, or even spirituality, and explains why they match your query. It’s like a search engine for tweets!

---

## Features

- Type any query (e.g., `"AI ethics"` or `"funny AI"`) and get matching threads.
- Shows thread content, summary, tags, vibe, and why it was picked.
- Uses AI to understand your query deeply, not just keywords.
- Simple to run on your computer with Python.

---

## Tech Used

- **Python**: Main language for everything.
- **SentenceTransformers**: For smart AI search (understands meaning of words).
- **FAISS**: For fast searching of threads.
- **FastAPI**: Backend to handle queries (optional, not in current version).
- **Streamlit**: For a simple web interface (optional, can add later).

---

## Files in This Project

- `data_loader.py`: Loads the thread data from `twitter_threads.json`.
- `search.py`: The main AI search engine code.
- `mock_data.json`: Sample data with 60 tweets (threads).
- `main.py`: Test file to try out the search.

---

## How to Set Up

1. **Get Python**: Make sure Python 3.8 or higher is installed.
2. **Create Virtual Environment** (optional but good):
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```
3. **Install Libraries**:
    ```bash
    pip install numpy faiss-cpu sentence-transformers nltk
    ```
4. **Download Data**: Make sure `mock_data.json` is in the project folder. It has 60 sample threads.
5. **Run Test**:
    ```bash
    python main.py
    ```

This will show results for sample queries like `"AI ethics"` or `"funny AI"`.

---

## How to Use

1. Open `test_search.py` and add your own queries:
    ```python
    queries = ["AI ethics concerns", "funny AI moments", "AI health tips"]
    ```
2. Run the script:
    ```bash
    python test_search.py
    ```
3. See results! For each query, it shows matching threads, why they were picked, and a score.

If you type something unrelated (like `"movie names"`), it says:

```json
"No relevant threads found."

```markdown
## Example Output

### Query: `"AI ethics concerns"```

```json
[
  {
    "content": "AI’s great at predicting behavior, but who’s watching the watcher? Data privacy needs to be priority #1. #AIEthics",
    "summary": "Calls for stronger data privacy in AI systems.",
    "tags": ["AI", "ethics", "privacy"],
    "vibe": "serious, urgent",
    "source_url": "https://twitter.com/AIEthicist/status/100000001",
    "why_this": "Semantic similarity score: 0.732; Matching tags: AI, ethics; Matching words: ethics",
    "similarity_score": 0.732
  }
]
```

### Query: `"hello guru ela vunav"`

```json
{
  "message": "No relevant threads found for the query. Try a query related to AI, tech, health, or spirituality."
}
```

---

## Future Ideas

- Add a web interface with Streamlit to type queries in a browser.
- Use FastAPI to make it a proper web app.
- Add more threads or connect to real Twitter data.
- Support Telugu or Hindi queries for Indian users.


---

## Contact

Made by **Lokesh Sinha N** 
Reach me at lokeshsinha746@gmail.com 
+9-8985042381

Enjoy searching threads, and happy coding! 🚀




