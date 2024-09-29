import React, { useState } from "react";
import axios from "../services/api";

const TipList = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [tips, setTips] = useState([]);

  const handleFetchTips = async () => {
    try {
      const token = localStorage.getItem("token");
      const res = await axios.get(
        `/tip?startDate=${startDate}&endDate=${endDate}`,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      setTips(res.data);
    } catch (err) {
      console.error(err);
      alert("Error fetching tips");
    }
  };

  return (
    <div>
      <h2>View Tip Records</h2>
      <input
        type="date"
        placeholder="Start Date"
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
        required
      />
      <input
        type="date"
        placeholder="End Date"
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
        required
      />
      <button onClick={handleFetchTips}>Get Tips</button>
      <ul>
        {tips.map((tip, index) => (
          <li key={index}>
            {tip.place}: ${tip.totalAmount} - Tip: ${tip.tipAmount}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TipList;
