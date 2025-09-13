const express = require("express");
const router = express.Router();
const Recommendation = require("../models/Recommendation");

router.get("/:userId", async (req, res) => {
    const userId = req.params.userId;
    const userUsage = await Recommendation.findOne({ user_id: userId });
    if (!userUsage) return res.status(404).json({ message: "User not found" });

    // Simple AI-like rule-based recommendation
    let recommendedPlan = "Standard";
    if(userUsage.avg_data_usage > 500) recommendedPlan = "UltraMax";
    else if(userUsage.avg_data_usage > 300) recommendedPlan = "ProStream";

    userUsage.recommended_plan = recommendedPlan;
    await userUsage.save();

    res.json({
        user_id: userUsage.user_id,
        current_plan: userUsage.current_plan,
        avg_data_usage: userUsage.avg_data_usage,
        recommended_plan: userUsage.recommended_plan
    });
});

module.exports = router;
