const doNothing = () => {}

function Content(props) {
  return (
    <div className="sounds-container">
      <h3>List of current sounds</h3>
      <div className='sound-container'>
        <div className="sound-name">Sound name</div>
        <div className="sound-action">
          <div className="my-link" onClick={doNothing} title="Play in browser"><i className="fas fa-play-circle"></i></div>
        </div>
        <div className="sound-action">
          <a className="discord-link" onClick={doNothing}  href="#" title="Play in Discord"><i className="fab fa-discord"></i></a>
        </div>
      </div>
    </div>
  )
}

export default Content
