const doNothing = () => {}

function SoundUploader(props) {
  return (
    <div className='sound-upload-container'>
      <form action="#" method="POST" encType="multipart/form-data">
        <div className='upload-fields'>
          <div className="fieldWrapper">
            <label htmlFor="something1">Command:</label>
            {/*{{ form.command }}*/}
            <input name="something1" type="text"/>
          </div>
          <div className="fieldWrapper">
            <label htmlFor="something2">Filename:</label>
            {/*{{ form.filename }}*/}
            <input name="something2" type="file"/>
          </div>      
        </div>
        <a className="my-link" onClick={doNothing} href="#"><i className="fas fa-plus"></i></a>
      </form>
    </div>
  );
}

export default SoundUploader;
