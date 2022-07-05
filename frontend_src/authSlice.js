import { createSlice } from '@reduxjs/toolkit'
import { getCookie } from './util'

export const authSlice = createSlice({
  name: 'auth',
  initialState: {
    token: getCookie('logintoken'),
  },
  reducers: {
    login: (state, action) => {
      state.token = action.payload 
    },
    logout: (state) => {
      state.token = null
    }
  }
})

export const { login, logout } = authSlice.actions

export default authSlice.reducer
