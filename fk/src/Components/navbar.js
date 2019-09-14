import React from 'react';
import '../App.css';
import 'firebase/firestore';
import {
  useFirestoreDoc,
  useFirebaseApp,
  SuspenseWithPerf
} from 'reactfire';

const Navbar = () => {
    return (
        <div class="uk-section-secondary">

            <div uk-sticky="animation: uk-animation-slide-top; sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky; cls-inactive: uk-navbar-transparent uk-dark; top: 0">

                <nav class="uk-navbar-container">
                    <div class="uk-container uk-container-expand">
                        <div uk-navbar>

                            <ul class="uk-navbar-nav">
                                <li class="uk-active"><a href="#">CLI CHAT</a></li>
                                <li>
                                    <a href="#">User</a>
                                    <div class="uk-navbar-dropdown">
                                        <ul class="uk-nav uk-navbar-dropdown-nav">
                                            <li class="uk-active"><a href="#">Active</a></li>
                                            <li><a href="#">Item</a></li>
                                            <li><a href="#">Item</a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li><a href="index.html">Exit</a></li>
                            </ul>

                        </div>
                    </div>
                </nav>
            </div>
        </div>
    );
}

export default Navbar;