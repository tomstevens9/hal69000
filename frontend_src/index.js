import _ from 'lodash';
import React from 'react';
import ReactDOM from 'react-dom/client';

import Base from './Base';
import store from './store';
import { Provider } from 'react-redux';

// Initialise React
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <Provider store={store}>
    <Base />
  </Provider>
  </React.StrictMode>
);
