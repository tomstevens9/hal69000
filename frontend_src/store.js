import { configureStore } from '@reduxjs/toolkit'
import authReducer from './authSlice'
import soundsSlice from './soundsSlice'
import tagsSlice from './tagsSlice'

export default configureStore({
  reducer: {
    auth: authReducer,
    sounds: soundsSlice,
    tags: tagsSlice,
  },
})

