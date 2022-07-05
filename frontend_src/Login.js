import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux'
import { login as login_action } from './authSlice'
import { login } from './login_util.js';
import './login.css'
import Mario from './mario.webp';

function Login(props) {
  // Used to manage auth state.
  const dispatch = useDispatch()
  // Used to handle component's input fields
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const loginHandler = e => {
    e.preventDefault()
    login(username, password)
      .then(token => dispatch(login_action(token)))
    return false;  // Prevent form from being submit
  }

  const updateInput = callback => (e => callback(e.target.value))

  return (
    <div id="login-container">
      <div id="login-box">
        <img src={Mario} alt="Tom in Mario hat" />
        <div>
          <form onSubmit={loginHandler}>
            <div className="input-field">
              <label htmlFor="username">username</label>
              <br/>
              <input name="username" type="text" value={username} onChange={updateInput(setUsername)}/>
            </div>
            <div className="input-field">
              <label htmlFor="password">password</label>
              <br/>
              <input name="password" type="password" value={password} onChange={updateInput(setPassword)} />
            </div>
            <input type="submit" value="Log in" />
          </form>
        </div>
      </div>
    </div>
  )
}
  
export default Login