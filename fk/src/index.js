import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { FirebaseAppProvider } from 'reactfire';
import 'firebase/performance';

const firebaseConfig = {
    apiKey: "AIzaSyBRebJ4woEHzvPM0NeG2f49c7-atJQkdmM",
    authDomain: "sample-f4a88.firebaseapp.com",
    databaseURL: "https://sample-f4a88.firebaseio.com",
    projectId: "sample-f4a88",
    storageBucket: "sample-f4a88.appspot.com",
    messagingSenderId: "535786291215",
    appId: "1:535786291215:web:7fed87cb6d845a718f237a"
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
