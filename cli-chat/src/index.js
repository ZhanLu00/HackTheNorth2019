import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Navbar from './Components/Navbar';
import * as serviceWorker from './serviceWorker';
import * as firebase from 'firebase';

const firebaseConfig = {
    apiKey: "AIzaSyBRebJ4woEHzvPM0NeG2f49c7-atJQkdmM",
    authDomain: "sample-f4a88.firebaseapp.com",
    databaseURL: "https://sample-f4a88.firebaseio.com",
    projectId: "sample-f4a88",
    storageBucket: "",
    messagingSenderId: "535786291215",
    appId: "1:535786291215:web:2990311dc6f3f9f38f237a"
  };

firebase.initializeApp(firebaseConfig);

ReactDOM.render(<Navbar />, document.getElementById('navbar'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
