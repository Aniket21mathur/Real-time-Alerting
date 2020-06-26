import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      server_id: 0,
      cpu: 0,
      memory: 0,
      disk: 0,
      alert: "",
      rules: [],
    };

    this.handleIdChange = this.handleIdChange.bind(this);
    this.handleCPUChange = this.handleCPUChange.bind(this);
    this.handleMEMChange = this.handleMEMChange.bind(this);
    this.handleDISKChange = this.handleDISKChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  handleIdChange(e) {
     this.setState({server_id: e.target.value});
  }

  handleCPUChange(e) {
     this.setState({cpu: e.target.value});
  }

  handleMEMChange(e) {
     this.setState({memory: e.target.value});
  }

  handleDISKChange(e) {
     this.setState({disk: e.target.value});
  }

  onSubmit(e) {
    e.preventDefault();

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({"SERVER_ID":this.state.server_id,
       "CPU_UTILIZATION":this.state.cpu, "MEMORY_UTILIZATION":this.state.memory,
       "DISK_UTILIZATION": this.state.disk})
    };

    fetch("/realtimeapp/", requestOptions)
      .then(response => {
        return response.json();
      })
      .then(parsedData => {
        this.setState({alert: parsedData.ALERT});
        this.setState({rules: parsedData.RULES_VIOLATED});
      })
 
  }

render() {
    return (
     <div className="App">
                <form id="main-login">
                    <h2>Real time Alerting</h2>
                    <label>
                        <span>SERVER_ID:</span>
                        <input type="number" name="id" value={this.state.server_id} onChange={this.handleIdChange}/><br/>
                    </label>
                    <br/>
                    <label>
                        <span>CPU_UTILIZATION:</span>
                        <input type="number" name="cpu" value={this.state.cpu} onChange={this.handleCPUChange} /><br/>
                    </label>
                    <br/>
                    <label>
                    <span>MEMORY_UTILIZATION:</span>
                    <input type="number" name="mem" value={this.state.memory} onChange={this.handleMEMChange}/><br/>
                    </label>
                    <br/>
                    <label>
                    <span>DISK_UTILIZATION:</span>
                    <input type="number" name="dsk" value={this.state.disk} onChange={this.handleDISKChange}/><br/>
                    </label>
                    <br/>
                    <div className="align-right">
                   <br/>
                   <button onClick={this.onSubmit}>Submit</button>
                  </div>
                </form>
                <div>
                  <p>{this.state.alert}</p>
                  <p>{this.state.server_id}</p>

                {this.state.rules && this.state.rules.map( (rule, index) => {
                    return <p key={ index }>{rule}</p>;
                  })}
                 </div>
            </div>
    );
  }
}


export default App;

const container = document.getElementById("app");
render(<App />, container);
