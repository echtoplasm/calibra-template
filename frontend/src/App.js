// src/App.js

import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import NavBar from './components/NavBar'; 
import LandingPage from './landing-page/LandingPage';
import Login from './components/login';
import AboutPage from './pages/AboutPage';
import Services from './pages/Services';
import SignUp from './components/signup';
import TaskDataService from './services/tasks';

function App() {
  const [user, setUser] = React.useState(null);
  const [error, setError] = React.useState(null); 

  async function login (user = null) {
    TaskDataService.login(user)
    .then(Response => {
      setUser(user.username);
      localStorage.setItem('user', user.username);
      setError('');
  })
    .catch( e => {
      console.log('login error', e);
      setError('e.toString()');
    });
  }
  return (
    <Router>
      <NavBar />
      <Routes> 
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/services" element={<Services />} />
      </Routes>
    </Router>
  );


}

export default App;
