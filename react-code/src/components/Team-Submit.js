import React, { useState } from "react";
import axios from "axios";

function Team_Submit() {
  const [data, setData] = useState({
    name: "",
    age: "",
  });

  const handleChange = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value,
    });
  };

  console.log(data);

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post("http://localhost:5000/add", data, {
        headers: {
          "Content-Type": "application/json"
        },
      })
      .then((response) => {
        console.log(response.data);
        // Handle the response from the server as needed
      })
      .catch((error) => {
        console.error("Error:", error);
        // Handle any errors
      });
  };

  return (
    <div>
      <h1>Send Data to Flask Backend</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={data.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Age:</label>
          <input
            type="number"
            name="age"
            value={data.age}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Team_Submit;
