import './index.css';

import Header from './Header.js';
import Body from './Body.js';

function Base(props) {
    return (
      <div id="container">
        <Header/>
        <Body/>
      </div>
    )
}

export default Base
