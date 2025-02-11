import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';
import calibraNavBar from '../branding/logo_white_no_background.png';



const NavBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <img src={calibraNavBar} alt="Calibra Logo." width="100" height="100" />
        </Link>
        <ul className="navbar-menu">
          <li className="navbar-item">
            <Link to="/" className="navbar-link">Home</Link>
          </li>
          <li className="navbar-item">
            <Link to="/about" className="navbar-link">About</Link>
          </li>
          <li className="navbar-item">
            <Link to="/services" className="navbar-link">Services</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;

