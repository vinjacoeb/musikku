# musikku/views.py
from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

# Load data from datamusik.csv
df = pd.read_csv('musikku/datamusik.csv')

# Pemrosesan data
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Lirik'].fillna(''))

# Perhitungan matriks kesamaan (Cosine Similarity)
doc_sim_df = pd.DataFrame(cosine_similarity(tfidf_matrix, tfidf_matrix), index=df.index, columns=df.index)

def generate_ngrams(text, n):
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    return [' '.join(ngram) for ngram in ngrams]

def musik_recommender(musik_Judul, musik_df=df, doc_sims=doc_sim_df):
    musik_Judul_ngrams = generate_ngrams(musik_Judul, 1) + generate_ngrams(musik_Judul, 2) + generate_ngrams(musik_Judul, 3)
    dataset_Judul_ngrams = musik_df['Judul'].apply(lambda x: generate_ngrams(x, 1) + generate_ngrams(x, 2) + generate_ngrams(x, 3))

    # Calculate similarity using Jaccard similarity coefficient for title
    similarity_scores_Judul = dataset_Judul_ngrams.apply(lambda x: fuzz.partial_ratio(' '.join(musik_Judul_ngrams), ' '.join(x)))

    # Set a threshold for considering a match
    similarity_threshold_Judul = 50

    # Filter out results below the threshold
    filtered_results_Judul = similarity_scores_Judul[similarity_scores_Judul >= similarity_threshold_Judul]

    # If there are filtered results, proceed with recommending music
    if not filtered_results_Judul.empty:
        musik_idx = filtered_results_Judul.idxmax()
        musik_similarities = doc_sims[musik_idx]
        similar_musik_idxs = np.argsort(-musik_similarities)[1:6]
        similar_musik = musik_df.iloc[similar_musik_idxs]

        recommended_info = []
        for idx, row in similar_musik.iterrows():
            Penyanyi = row['Penyanyi']
            Judul_lagu = row['Judul']
            Lirik = row['Lirik']
            recommended_info.append({'Penyanyi': Penyanyi, 'Judul': Judul_lagu, 'Lirik': Lirik})

        return recommended_info

    # Handle case when no close match is found
    return []

def musik_list(request):
    musik_Judul = ''
    recommendations = []

    if request.method == 'POST':
        musik_Judul = request.POST.get('search_input', '')
        recommendations = musik_recommender(musik_Judul)

    return render(request, 'musikku/musik_list.html', {'musik_Judul': musik_Judul, 'recommendations': recommendations})
