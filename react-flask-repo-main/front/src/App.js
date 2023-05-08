import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [data, setData] = useState(null);

  const handleClick = async () => {
    const result = await axios.post('http://localhost:5002/external-api', { api_key: '12345' });
    setData(result.data.result);
  };

  return (
    <div className="container">
      <span style={{marginLeft: '10px',fontSize: "32px"}}>CALL API</span>
      <div className="container">
      <button className="btn btn-outline-secondary" onClick={handleClick}>Click me</button>
      {data && <p className="response-text">{data}</p>}
      </div>
    </div>

  );
}

export default App;
