import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignUp from "./components/SignUp";
import Login from "./components/Login";
import TipCalculator from "./components/TipCalculator";
import TipList from "./components/TipList";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" component={<SignUp />} />
        <Route path="/login" component={<Login />} />
        <Route path="/calculate-tip" component={<TipCalculator />} />
        <Route path="/tips" component={<TipList />} />
      </Routes>
    </Router>
  );
}

export default App;
