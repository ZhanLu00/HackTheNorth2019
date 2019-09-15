import React from 'react';

const ChatInputField = ({userName}) =>{
    return (
        <div uk-container class="uk-section-secondary">
            <div class="uk-flex">
                <div class="uk-width-1-6">
                    <p>@81e9df2a/{userName} $</p>
                </div>
                <div class="uk-width-1-2">
                    <form div uk-sticky="bottom: true">
                        <fieldset class="uk-fieldset">
                            <div class="uk-margin">
                                <textarea class="uk-textarea" rows="5" placeholder="Enter your command here"></textarea>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
            
        </div>
    );
}

export default ChatInputField;