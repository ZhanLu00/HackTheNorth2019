import React from 'react';

const ChatInputField = () =>{
    return (
        <div>
            <form div uk-sticky="bottom: true" class="uk-section-secondary">
                <fieldset class="uk-fieldset">
                    <div class="uk-margin">
                        <textarea class="uk-textarea" rows="5" placeholder="Textarea"></textarea>
                    </div>

                </fieldset>
            </form>
        </div>
    );
}

export default ChatInputField;