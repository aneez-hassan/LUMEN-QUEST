# LUMEN-QUEST
# 📡 AI-Based Personalized Recommendation System (MERN)

This project is a **Subscription Management MVP** built using the **MERN stack** with an **AI-based personalized recommendation engine**.  
It allows users to subscribe, manage plans, and receive **personalized plan recommendations** based on their usage patterns.

---

## 🚀 Features
- User can **subscribe, upgrade, downgrade, and cancel** plans.
- Admin can **create, update, delete, and view** subscription plans and pricing.
- Admin dashboard shows **top subscription plans** (recent, monthly, yearly).
- Users can **view and manage subscriptions, discounts, and plans**.
- 🔥 **AI-based personalized recommendations** powered by user usage data.

---

## 🛠️ Tech Stack
- **Frontend:** React.js, Axios, TailwindCSS
- **Backend:** Node.js, Express.js
- **Database:** MongoDB (Mongoose ODM)
- **AI/ML:** Simple recommendation logic (rule-based + usage analysis)

---

## 📂 Project Structure
backend/
├── server.js
├── models/
│ └── recommendations.js
├── routes/
│ └── recommendations.js
└── .env
frontend/
└── src/
└── components/
└── Recommendation.js

---

## ⚡ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-recommendation-mvp.git
   cd ai-recommendation-mvp
Install backend dependencies:

cd backend
npm install


Install frontend dependencies:

cd frontend
npm install


Create .env in backend:

MONGO_URI=your_mongo_connection_string
PORT=5000


Run backend:

cd backend
npm start


Run frontend:

cd frontend
npm start

🎯 Usage

Users can log in (simulated).

Based on previous usage & plan type, the AI will recommend a better plan.

Admins can view top-performing plans and manage plans.

🤝 Contribution

Pull requests are welcome. Please fork the repo and open a PR.

📜 License

MIT License © 2025

