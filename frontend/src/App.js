// src/App.js

/* react imports */
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'; 

/* pages imports */
import LandingPage from './landing-page/LandingPage';
import AboutPage from './pages/AboutPage';
import Services from './pages/Services';

/* components imports */
import NavBar from './components/NavBar'; 

/* services imports */
import TaskDataService from './services/tasks';

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
    <div className="App">
      <div>
        <Router>
          <NavBar />
          <Routes>
            <Route path = "/" element={<LandingPage />} />

            <Route path="/about" element={<AboutPage />} />

            <Route path="/services" element={<Services />} />

          </Routes>
        </Router>
      </div>
    </div>

);

}

export default App;
