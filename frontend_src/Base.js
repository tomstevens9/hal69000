import React from 'react'
import { useSelector } from 'react-redux'
// TODO look into React.lazy
import Login from './Login'
import App from './App'

import './common.scss'

function Base (props) {
  const token = useSelector(state => state.auth.token)

  return (token == null) ? <Login /> : <App />
}

export default Base
