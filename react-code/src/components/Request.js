import React, {useState} from 'react';

function Request(props){
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setInputValue('');
        console.log("Request Submitted.")
    };

    return(
        <div className= 'Request'>
            <h2>Enter summoner names to create team</h2>
            <input value = {inputValue} onChange = {handleInputChange}/>
            <div className= 'actions'>
                <button className= 'submit' onClick = {handleSubmit}>Submit</button>
            </div>
        </div>
    );
}

export default Request;