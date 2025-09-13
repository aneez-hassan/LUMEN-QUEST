const mongoose = require("mongoose");

const recommendationSchema = new mongoose.Schema({
  user_id: { type: Number, required: true },
  current_plan: { type: String, required: true },
  avg_data_usage: { type: Number, required: true },
  recommended_plan: { type: String },
  timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model("Recommendation", recommendationSchema);
