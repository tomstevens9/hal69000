import { useState, useEffect } from 'react'
import { uploadSound } from './api'

function SoundUploader(props) {
  const [commandName, setCommandName] = useState('')
  const [commandFile, setCommandFile] = useState(null)
  const [commandFilePath, setCommandFilePath] = useState('')

  const onSubmit = e => {
    e.preventDefault()
    uploadSound(commandName, commandFile)
    return false;
  }

  const updateCommandName = e => setCommandName(e.target.value)
  const updateCommandFile = e => {
    setCommandFile(e.target.files[0])
    setCommandFilePath(e.target.value)
  }

  return (
    <div className='sound-upload-container'>
      <form id='sound-upload-form' onSubmit={onSubmit}>
        <div className='upload-fields'>
          <div className="fieldWrapper">
            <label htmlFor="command-name">Command:</label>
            <input name="command-name" type="text" value={commandName} onChange={updateCommandName}/>
          </div>
          <div className="fieldWrapper">
            <label htmlFor="command-file">Filename:</label>
            <input name="command-file" type="file" value={commandFilePath} onChange={updateCommandFile}/>
          </div>      
        </div>
        <a className="my-link" onClick={onSubmit} href="#"><i className="fas fa-plus"></i></a>
      </form>
    </div>
  );
}

export default SoundUploader;
