import react from 'react';
import './styles.css';
import calibraLogo from '../branding/calibra-no-background.png';
import sqlLogo from '../branding/sql-logo-nb.png';


const LandingPage = () => {
  return (
    <div>
      <header className="landing-container">
        <h1>Welcome to EchoSec</h1>
        <img src={calibraLogo} alt="Calibra Logo." width="320" height="320" />
        <p>Next level cybersecurity and pentesting</p>
      </header>

      <section className="features">

        <h2>Features</h2>

        <div className="feature-item-container">
          <div className="feature-item">
            <h3>Natural Language SQL</h3>
            <p>Use natural language to generate SQL queries effortlessly with the help of our AI assistant.</p>
          </div>
          <div className="feature-item">
            <h3>Data Visualization</h3>
            <p>Generate beautiful visualizations of your data with the help of our AI assistant.</p>
          </div>
          <div className="feature-item">
            <h3>Enhance Work Flow</h3>
            <p>Use the assitant to seamlessly transcribe meeting details, draft and send emails, set reminders and much more, all without any interuption to the workflow.</p>
          </div>
        </div>
      </section>

      <section className="cta">
        <h2>Ready to get started?</h2>
        <button>Sign Up</button>
      </section>

      <footer className="footer">
        <small><p>Calibra &copy; 2025</p></small>
      </footer>


    </div>

  );
};

export default LandingPage;
