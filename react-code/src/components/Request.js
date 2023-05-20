import React, {useState, useEffect} from 'react';
import { data_ } from './flask-server/server.py';

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

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/members").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    return(
        <div className= 'Request'>
            <h2>Enter summoner names to create team</h2>
            <input value = {inputValue} onChange = {handleInputChange}/>
            <div className= 'actions'>
                <button className= 'submit' onClick = {handleSubmit}>Submit</button>
            </div>
            <h2>Teams</h2>
            <h3>{data_}</h3>
        </div>
    );
}

export default Request;