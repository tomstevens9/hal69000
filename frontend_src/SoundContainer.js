import { getSound, sendCommand } from './api'

const doNothing = () => {}

function SoundContainer(props) {
  const sound = props.sound

  const playSound = () => {
    const audio = new Audio(`sound/${encodeURIComponent(sound.command)}/`)
    audio.play()
  }

  const sendSound = () => {
    sendCommand(sound.command)
  }

  return (
    <div className='sound-container'>
      <div className="sound-name">{sound.command}</div>
      <div className="sound-action">
        <div className="my-link" onClick={playSound} title="Play in browser"><i className="fas fa-play-circle"></i></div>
      </div>
      <div className="sound-action">
        <a className="discord-link" onClick={sendSound}  href="#" title="Play in Discord"><i className="fab fa-discord"></i></a>
      </div>
    </div>
  )
}

export default SoundContainer
