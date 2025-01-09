import React, {useState} from "react";
import './gen-page.css';

const Login = props => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  
const onChangeUsername = (e) => {
  const username = e.target.value;
  setUsername(username);
}

const onChangePassword = (e) => {
  const password = e.target.value;
  setPassword(password);
}

const login = (e) => {
  props.login({username: username, password: password});
  props.history.push("/");
}

return (
  <div className="gen-page">
    <div className="signin-container">
      <h1>Welcome, Please Sign In</h1>
      <input type="text" placeholder="Username" value={username} onChange={onChangeUsername} />
      <br/>
      <input type="password" placeholder="Password" value={password} onChange={onChangePassword} />
      <br/>
      <button onClick={login}>Sign In</button>
      <p>{message}</p>
      <p>{error}</p>
    </div>
  </div>
);

}
export default Login;
