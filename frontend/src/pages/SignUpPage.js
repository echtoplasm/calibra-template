import React, {useState} from "react";
import './gen-page.css';

function SignUpPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const[error, setError] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/api/accounts/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    setMessage(data.message);
    setError(data.Error);
  }



return (
  <div>
    <div className="signup-container">
      <h1>Upgrade Your Workflow</h1>
      <h2>Sign up for our services!</h2>
      <form onSubmit={handleSignup}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Sign Up</button>
      </form>
    </div>
    <p>{message}</p>
    <p>{error}</p>
  </div>
);

};

export default SignUpPage;
