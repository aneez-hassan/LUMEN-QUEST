# -*- coding: utf-8 -*-
"""
AI-Based Recommendation System for Subscription Plans

Includes:
1. Collaborative Filtering (using Surprise library)
2. Content-Based Filtering (using TF-IDF + Cosine Similarity)

Plans:
- Standard (Lumen Standard+)
- Pro (Lumen ProStream)
- Premium (Lumen UltraMax)

Author: Hackathon MVP
"""

# !pip install scikit-surprise

import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# Collaborative Filtering Section
# -------------------------------

def collaborative_filtering_demo():
    """
    Example: Users rating subscription plans based on satisfaction
    """

    # Sample User-Plan Ratings (1–5 scale)
    data = {
        'user_id': [1, 1, 2, 2, 3, 3, 4],
        'plan': [
            "Standard", "Pro",
            "Standard", "Premium",
            "Pro", "Premium",
            "Standard"
        ],
        'rating': [4, 5, 3, 5, 4, 5, 3],
    }
    df = pd.DataFrame(data)

    # Prepare Data for Surprise
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'plan', 'rating']], reader)

    # Train Collaborative Filtering Model
    algo = SVD()
    cross_validate(algo, data, cv=3, verbose=True)

    # Train on Full Dataset
    trainset = data.build_full_trainset()
    algo.fit(trainset)

    # Predict for a specific user-plan pair
    prediction = algo.predict(uid=2, iid="Pro")  # Example: User 2 → Pro Plan
    print("Predicted Rating (User 2 → Pro Plan):", prediction.est)


# ----------------------------
# Content-Based Filtering Demo
# ----------------------------

def content_based_demo():
    """
    Recommend subscription plans based on plan metadata similarity
    """

    # Subscription Plans Metadata
    data = {
        'plan': ["Standard", "Pro", "Premium"],
        'metadata': [
            "150 Mbps 300GB Basic support Occasional discounts",
            "250 Mbps 600GB Priority support Seasonal discounts",
            "500 Mbps 1TB VIP support Exclusive offers AI recommendations"
        ],
    }
    df = pd.DataFrame(data)

    # Convert Metadata to Feature Vectors
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['metadata'])

    # Calculate Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Recommendation function
    def get_recommendations(plan, cosine_sim=cosine_sim):
        idx = df[df['plan'] == plan].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:]  # exclude itself
        plan_indices = [i[0] for i in sim_scores]
        return df['plan'].iloc[plan_indices]

    # Example usage
    print("Recommended Plans for 'Standard':", list(get_recommendations("Standard")))
    print("Recommended Plans for 'Pro':", list(get_recommendations("Pro")))


# ---------------------
# Run Demo Functions
# ---------------------
if __name__ == "__main__":
    print("=== Collaborative Filtering Demo ===")
    collaborative_filtering_demo()

    print("\n=== Content-Based Filtering Demo ===")
    content_based_demo()
