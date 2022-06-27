import SoundUploader from './SoundUploader.js'
import PopularTags from './PopularTags.js'

function SideBar(props) {
    return (
      <div id="side-bar">
        <SoundUploader/>
        <PopularTags/>
      </div>
    )
}

export default SideBar;
