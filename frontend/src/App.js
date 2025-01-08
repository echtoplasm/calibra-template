// src/App.js

import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import NavBar from './components/NavBar'; 
import LandingPage from './landing-page/LandingPage';
import SignInPage from './pages/SignInPage';
import AboutPage from './pages/AboutPage';
import Services from './pages/Services';
import SignUpPage from './pages/SignUpPage';

function App() {
  const [user, setUser] = React.useState(null); 
  const [token, setToken] = React.useState(null); 
  const [error, setError] = React.useState(null); 

  async function login (user = null) {
    setUser(user);
  }

  async function logout () {
    setUser(null);
  }

  async function signup (user = null) {
    setUser(user);
  }
 
  return (
    <Router>
      <NavBar />
      <Routes> 
        <Route path="/" element={<LandingPage />} />
        <Route path="/signin" element={<SignInPage />} />
        <Route path="/signup" element={<SignUpPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/services" element={<Services />} />
      </Routes>
    </Router>
  );
}

export default App;
