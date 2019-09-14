import React from 'react';
import Link from "next/link";

const Navbar = () =>{
    return (
        <div id="navbar" uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky; bottom: #transparent-sticky-navbar">
                <nav class="uk-navbar-container" uk-navbar style="position: relative; z-index: 980;">
                    <div class="uk-navbar-left">
            
                        <ul class="uk-navbar-nav">
                            <li class="uk-active"><a href="index.html">Hack Chat</a></li>
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
                            <li><a href="#">Exit</a></li>
                        </ul>
            
                </div>
            </nav>
        </div>
    );
};

export default Navbar;