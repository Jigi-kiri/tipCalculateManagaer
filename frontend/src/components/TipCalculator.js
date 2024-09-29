import React, { useState } from "react";
import axios from "../services/api";

const CalculateTip = () => {
  const [formData, setFormData] = useState({
    place: "",
    totalAmount: 0,
    tipPercentage: 0,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      const res = await axios.post(
        "/tip/calculate",
        {
          place: formData.place,
          totalAmount: formData.totalAmount,
          tipPercentage: formData.tipPercentage,
        },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      console.log(res.data);
      alert(`Tip Calculated: ${res.data.tip}`);
    } catch (err) {
      console.error(err);
      alert("Error calculating tip");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="place"
        placeholder="Place"
        onChange={handleChange}
        required
      />
      <input
        name="totalAmount"
        type="number"
        placeholder="Total Amount"
        onChange={handleChange}
        required
      />
      <input
        name="tipPercentage"
        type="number"
        placeholder="Tip Percentage"
        onChange={handleChange}
        required
      />
      <button type="submit">Calculate Tip</button>
    </form>
  );
};

export default CalculateTip;
