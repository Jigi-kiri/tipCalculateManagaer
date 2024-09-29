import React, { useState } from "react";
import axios from "../services/api";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const history = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/user/login", formData);
      console.log(res.data);
      localStorage.setItem("token", res.data.token);
      alert("Login successful!");
      history.push("/calculate-tip"); // Redirect to calculate tip page after login
    } catch (err) {
      console.error(err);
      alert("Invalid credentials, please try again.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="email"
        type="email"
        placeholder="Email"
        onChange={handleChange}
        required
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        onChange={handleChange}
        required
      />
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;
