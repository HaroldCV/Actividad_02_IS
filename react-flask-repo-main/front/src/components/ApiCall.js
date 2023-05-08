import bcrypt from 'bcrypt';
import React from 'react';

class ApiCall extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      response: null,
      error: null
    };
  }

  handleClick = () => {
    const API_KEY = '12345';
    const salt = bcrypt.genSaltSync(10);
    const encryptedApiKey = bcrypt.hashSync(API_KEY, salt);

    fetch('http://localhost:5002/external-api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ api_key: encryptedApiKey })
    })
      .then(res => res.json())
      .then(data => this.setState({ response: data.result }))
      .catch(err => this.setState({ error: err.message }));
  };

  render() {
    return (
      <div>
        <h2>API Call Example</h2>
        <button onClick={this.handleClick}>Make API Call</button>
        {this.state.response && <p>Response: {this.state.response}</p>}
        {this.state.error && <p>Error: {this.state.error}</p>}
      </div>
    );
  }
}

export default ApiCall;
