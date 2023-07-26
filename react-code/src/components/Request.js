import React, { useState, useEffect } from "react";
// import { x } from "../flask-server/server.py";
import axios from 'axios';

function Request(props) {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setInputValue("");
    console.log("Request Submitted.");
  };

  const [profileData, setProfileData] = useState(null);

//   const [data, setData] = useState([{}]);

//   useEffect(() => {
//     fetch("/")
//       .then((res) => res.json())
//       .then((data) => {
//         setData(data);
//         console.log(data);
//       });
//   }, []);

function getData() {
    axios({
        method: "GET",
        url: "http://localhost:5000/profiles"
    })
    .then((response) => {
        const res =response.data
        setProfileData({
          profile_List: res.j.a,
          profile_Listb: res.k.b,
          profile_Listc: res.y.c
        })
          console.log(res)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
        })} 

  return (
    <div className="Request">
      <h2>Enter summoner names to create team</h2>
      <input value={inputValue} onChange={handleInputChange} />
      <div className="actions">
        <button className="submit" onClick={handleSubmit}>
          Submit
        </button>
      </div>
      <h2>Teams</h2>
      <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>{profileData.profile_List}</p>
              <p>{profileData.profile_Listb}</p>
              <p>{profileData.profile_Listc}</p>
              <p>{profileData.profile_Listd}</p>
            </div>
        }
        </div>
  );

}

export default Request;
