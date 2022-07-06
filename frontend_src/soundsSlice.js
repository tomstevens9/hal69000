import { createSlice } from '@reduxjs/toolkit'

export const soundsSlice = createSlice({
  name: 'sounds',
  initialState: {
    sounds: []
  },
  reducers: {
    update: (state, action) => {
      state.sounds = action.payload
    }
  }
})

export const { update } = soundsSlice.actions

export default soundsSlice.reducer
