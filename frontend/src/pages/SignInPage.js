import React, {useState} from "react";
import './gen-page.css';

function SignInPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const[error, setError] = useState("");
  
  const handleLogin = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/api/accounts/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    if (data.error) {
      setError(data.error);
      setMessage("");
    } else {
      setMessage(data.message);
      setError("");
    }
  };

  return (
    <div>
      <div className="signin-container">
        <h1>Welcome Back to Calibra</h1>
        <h2>Sign In</h2>
        <form onSubmit={handleLogin}>
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
          <button type="submit">Sign In</button>
        </form>
      </div>
      <p>{message}</p>
      <p>{error}</p>
    </div>
  );
}

export default SignInPage;
