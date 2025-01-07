// src/App.js

import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import NavBar from './components/NavBar'; 
import LandingPage from './landing-page/LandingPage';
import SignInPage from './pages/SignInPage';
import AboutPage from './pages/AboutPage';
import Services from './pages/Services';

function App() {
  return (
    <Router>
      <NavBar /> {/* NavBar will be on top of every page */}
      <Routes> {/* Replace Switch with Routes */}
        <Route path="/" element={<LandingPage />} />
        <Route path="/signin" element={<SignInPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/services" element={<Services />} />
      </Routes>
    </Router>
  );
}

export default App;
