import React from 'react'
import { useDispatch } from 'react-redux'
import { logout as logoutAction } from './authSlice'
import { logout } from './login_util.js'

function Header (props) {
  const dispatch = useDispatch()

  const logoutHandler = e => {
    e.preventDefault()
    logout()
      .then(success => {
        if (success) { dispatch(logoutAction()) }
      })
    return false
  }

  return (
    <div id='header'>
      <div id='logout-link'><a onClick={logoutHandler}>Log out</a></div>
    </div>
  )
}

export default Header
