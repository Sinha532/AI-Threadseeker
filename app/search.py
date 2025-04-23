import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class ThreadSearchEngine:
    def __init__(self, threads):
        self.threads = threads
        self.model = SentenceTransformer("all-mpnet-base-v2")
        self.index, self.embeddings = self.build_index()

    def build_index(self):
        corpus = [t["content"] for t in self.threads]
        embeddings = self.model.encode(corpus).astype("float32")
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        return index, embeddings

    def search(self, query, top_k=3, similarity_threshold=0.5):
        query_emb = self.model.encode([query])[0].astype("float32")
        D, I = self.index.search(np.array([query_emb]), top_k)
        results = []

        for score, idx in zip(D[0], I[0]):
            if score < similarity_threshold:
                continue  # skip irrelevant results

            thread = self.threads[idx]
            explanation = self.get_why_this(query, thread)
            results.append({
                "content": thread["content"],
                "summary": thread["summary"],
                "tags": thread["tags"],
                "vibe": thread["vibe"],
                "source_url": thread["source_url"],
                "why_this": explanation + f" (Similarity: {score:.2f})"
            })

        return results


    def get_why_this(self, query, thread):
        matching_tags = [t for t in thread["tags"] if t.lower() in query.lower()]
        return f"Matched tags: {', '.join(matching_tags)}" if matching_tags else "High semantic similarity"
