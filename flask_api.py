# -*- coding: utf-8 -*-
"""
Flask API for AI-Based Subscription Plan Recommendations

Supports:
1. Collaborative Filtering (mock data)
2. Content-Based Filtering (mock data)

Plans:
- Standard (Lumen Standard+)
- Pro (Lumen ProStream)
- Premium (Lumen UltraMax)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------
# Mock Recommendation Data
# -------------------------

# Collaborative Filtering Recommendations (user_id → suggested plans)
collab_recommendations = {
    1: ['Pro', 'Premium'],       # Example: User 1 likes Standard → Recommend Pro/Premium
    2: ['Standard', 'Premium'],  # Example: User 2 tried Pro → Recommend others
    3: ['Pro'],                  # Example: User 3 prefers upgrades
}

# Content-Based Recommendations (plan → similar plans)
content_recommendations = {
    'Standard': ['Pro'],
    'Pro': ['Standard', 'Premium'],
    'Premium': ['Pro'],
}


# -------------------------
# API Endpoints
# -------------------------

@app.route('/recommend', methods=['GET'])
def recommend():
    """
    Usage:
    - /recommend?user_id=1   → collaborative filtering recommendations
    - /recommend?plan=Pro    → content-based recommendations
    """

    user_id = request.args.get('user_id', type=int)
    plan = request.args.get('plan', type=str)

    # Collaborative Filtering Recommendations
    if user_id:
        recommendations = collab_recommendations.get(user_id, [])
        return jsonify({
            "user_id": user_id,
            "recommendations": recommendations
        })

    # Content-Based Recommendations
    elif plan:
        recommendations = content_recommendations.get(plan, [])
        return jsonify({
            "plan": plan,
            "recommendations": recommendations
        })

    return jsonify({"error": "Provide user_id or plan"}), 400


# -------------------------
# Run Flask App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
