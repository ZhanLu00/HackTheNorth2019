import React from 'react';
import { Z_FIXED } from 'zlib';

const ChatInputField = ({userName}) =>{
    const style1 = {
        overflow: 'hidden',
        position: 'fixed',
        bottom: 0,
        width:'100%'
    };
    const style2 = {
        width:'100%'
    };
    return (
        <div>
        <div class="uk-divider"></div>
        <div uk-grid class="uk-section-secondary uk-flex uk-padding-small uk-padding-remove-top uk-padding-remove-bottom" style={style1}>
                <div class="uk-container uk-width-1-6 uk-padding-small uk-padding-remove-right">
                    <p>@81e9df2a/{userName} $</p>
                </div>
                <div class="uk-container uk-width-5-6">
                    <form class="uk-container uk-padding-small uk-padding-remove-left">
                        <fieldset class="uk-container uk-fieldset">
                            <div >
                                <textarea class="uk-textarea" rows="1" placeholder="Enter your command here"></textarea>
                            </div>
                        </fieldset>
                    </form>
                </div>
        </div>
        </div>
    );
}

export default ChatInputField;