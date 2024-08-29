import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import json

def get_result(query):

    df = pd.read_json("games_apurado.json").T

    query = query.lower()

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['description'])
    Q = vectorizer.transform([query])

    R = X.dot(Q.T)

    relevance_scores = R.toarray().flatten()

    sorted_indices = np.argsort(relevance_scores)[::-1]

    num_results = 15
    relevant_indexes = sorted_indices[:num_results]
    results = []
    for index in relevant_indexes:
        game_id = df.index[index]
        game_name = df.iloc[index]["name"]
        full_description = df.iloc[index]["description"]
        # short_description = ' '.join(full_description.split()[:500])  # Limit to the first 500 words
        relevance = relevance_scores[index]
        
        results.append({
            "id": str(game_id),
            "game": game_name,
            "description": full_description,
            "relevance": str(relevance)
        })

    output = {
        "results": results,
        "message": "OK"
    }

    return output
    # with open('result.json', 'w', encoding='utf-8') as file:
    #     json.dump(output, file, ensure_ascii=False, indent=4)