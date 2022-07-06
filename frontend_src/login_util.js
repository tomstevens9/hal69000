import axios from 'axios'

import { getCookie } from './util.js'

const setTokenCookie = token => {
  // Expire cookie in a year
  const date = new Date()
  date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000))
  const expires = `expires=${date.toUTCString()}`
  const cookieString = `logintoken=${token}; ${expires}; path=/`
  document.cookie = cookieString
}

const removeTokenCookie = () => {
  // Set cookie creation date in past to remove it
  const date = new Date()
  date.setTime(0)
  const expires = `expires=${date.toUTCString()}`
  const cookieString = `logintoken=; ${expires}; path=/`
  document.cookie = cookieString
}

const login = (username, password) => {
  return axios({
    method: 'post',
    url: 'auth/login/',
    auth: {
      username,
      password
    },
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  })
    .then(response => {
      const token = response.data.token
      setTokenCookie(token)
      return token
    })
    .catch(err => {
      // TODO handle better
      console.log(err)
      return null
    })
}

const logout = () => {
  return axios({
    method: 'post',
    url: 'auth/logout/',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      Authorization: `Token ${getCookie('logintoken')}`
    }
  })
    .then(response => {
      removeTokenCookie()
      return true
    })
    .catch(err => {
      console.log(err)
      return false
    })
}

export { login, logout }
