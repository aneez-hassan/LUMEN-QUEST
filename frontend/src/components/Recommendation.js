import React, { useEffect, useState } from "react";

const Recommendation = ({ userId }) => {
    const [rec, setRec] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:5000/api/recommendations/${userId}`)
            .then(res => res.json())
            .then(data => setRec(data));
    }, [userId]);

    if (!rec) return <p>Loading recommendation...</p>;

    return (
        <div className="recommendation-card">
            <h3>Recommended Plan for You</h3>
            <p>Current Plan: {rec.current_plan}</p>
            <p>Average Usage: {rec.avg_data_usage} GB</p>
            <p><strong>Suggested Plan: {rec.recommended_plan}</strong></p>
            <button>Upgrade Now</button>
        </div>
    );
};

export default Recommendation;
