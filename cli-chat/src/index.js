import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Navbar from './Components/Navbar';
import * as serviceWorker from './serviceWorker';
import * as firebase from 'firebase';
import { FirebaseAppProvider } from 'reactfire';
import 'firebase/performance';

const firebaseConfig = {
  /* add your config object from Firebase console */
};
ReactDOM.render(
  <FirebaseAppProvider firebaseConfig={firebaseConfig} initPerformance>
    <App />
  </FirebaseAppProvider>,
  document.getElementById('root')
);



// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
