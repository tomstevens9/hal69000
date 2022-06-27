import SideBar from './SideBar.js';
import Content from './Content.js'

function Body(props) {
  return (
      <div id="body">
        <SideBar/>
        <Content/>
      </div>
  )
}

export default Body;
