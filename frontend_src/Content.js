import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import SoundContainer from './SoundContainer.js'

import { getSounds } from './api'
import { update } from './soundsSlice'

// Attempt to get sounds every minute

function Content (props) {
  const sounds = useSelector(state => state.sounds.sounds)
  const dispatch = useDispatch()

  const updateSounds = () => {
    getSounds()
      .then(sounds => dispatch(update(sounds)))
  }

  useEffect(() => {
    // Get the sounds initially
    updateSounds()
  }, [])

  /*
  useEffect(() => {
    // Get sounds every 5 seconds
    const interval = setInterval(() => {
      updateSounds()
    }, 1000 * 5)

    return () => {
      clearInterval(interval)
    }
  })
  */

  return (
    <div className='sounds-container'>
      {sounds.map(sound => <SoundContainer sound={sound} key={sound.command} />)}
    </div>
  )
}

export default Content
