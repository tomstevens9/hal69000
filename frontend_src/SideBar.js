import Mario from './mario.webp';

import SoundUploader from './SoundUploader.js'
import PopularTags from './PopularTags.js'

function SideBar(props) {
    return (
      <div id="side-bar">
        <div id="side-bar-inner">
            <img src={Mario}/>
            <SoundUploader/>
            <PopularTags/> 
        </div>
      </div>
    )
}

export default SideBar;
