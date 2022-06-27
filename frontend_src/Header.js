import Mario from './mario.webp';

function Header(props) {
  return (
    <div id="header">
      <div id="image-container">
        <img id="image-header" src={Mario}/>
      </div>
      <div id="header-title"></div>
    </div>
  )
}

export default Header
