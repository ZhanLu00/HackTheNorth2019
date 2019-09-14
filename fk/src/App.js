import React from 'react';
import './App.css';
import 'firebase/firestore';
import {
  useFirestoreDoc,
  useFirebaseApp,
  SuspenseWithPerf
} from 'reactfire';
import Navbar from './Components/navbar.js';
import ChatContainer from './Components/chatcontainer.js';
import ChatInputField from './Components/chatinputfield.js';

function App(){
  return (
    <div className="App">
        <SuspenseWithPerf>
          <Navbar />
          <ChatContainer />
          <ChatInputField />
        </SuspenseWithPerf>
    </div>
  );
}

// function Burrito() {
//   // create a ref
//   const firebaseApp = useFirebaseApp();
//   const burritoRef = firebaseApp
//     .firestore()
//     .collection('tryreactfire')
//     .doc('burrito');

//   // subscribe to the doc. just one line!
//   const burritoDoc = useFirestoreDoc(burritoRef);

//   // get the value from the doc
//   const isYummy = burritoDoc.data().yummy;

//   return <p>The burrito is {isYummy ? 'good' : 'bad'}</p>;
// }
// function App() {
//   return (
//     <div className="App">
//       <SuspenseWithPerf
//         fallback={'loading burrito status...'}
//         traceId={'load-burrito-status'}
//       >
//         <Burrito />
//       </SuspenseWithPerf>
//     </div>
//   );
// }

export default App;
