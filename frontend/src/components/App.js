import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 40})
    };

    fetch("/realtimeapp/", requestOptions)
      .then(response => {
        return response.json();
      })
      .then(parsedData => {
        this.setState({data: parsedData});
      })
  }

render() {
  console.log(this.state.data);
    return (
      <div>
     <p> ALERT: {this.state.data.ALERT} </p>
     <p> SERVER_ID: {this.state.data.SERVER_ID} </p>
     </div>
    );
  }
}


export default App;

const container = document.getElementById("app");
render(<App />, container);
