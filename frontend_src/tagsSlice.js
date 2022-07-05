import { createSlice } from '@reduxjs/toolkit'

export const tagsSlice = createSlice({
  name: 'tags',
  initialState: {
    tags: []
  },
  reducers: {
    update: (state, action) => {
      state.tags = action.payload 
    },
  }
})

export const { update } = tagsSlice.actions

export default tagsSlice.reducer
