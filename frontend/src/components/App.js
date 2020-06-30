import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  // initalize states
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

  /*
    Handle state change from input form
  */

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

    // make a POST request to fetch data from the server
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

// render input form and output container
render() {
    return (
     <div className="container">
                <form className="form-inline">
                    <h2>Real time Alerting</h2>
                    <div className="form-group">
                        <label>SERVER_ID:</label><br/>
                        <input type="number" name="id" value={this.state.server_id} onChange={this.handleIdChange}/><br/>
                    </div>
            
                    <div className="form-group">
                        <label>CPU_UTILIZATION:</label><br/>
                        <input type="number" name="cpu" value={this.state.cpu} onChange={this.handleCPUChange} /><br/>
                    </div>
                   
                    <div className="form-group">
                    <label>MEMORY_UTILIZATION:</label><br/>
                    <input type="number" name="mem" value={this.state.memory} onChange={this.handleMEMChange}/><br/>
                    </div>
                
                    <div className="form-group">
                    <label>DISK_UTILIZATION:</label><br/>
                    <input type="number" name="dsk" value={this.state.disk} onChange={this.handleDISKChange}/><br/>
                    </div>
                    
                    <br/>
                   <button onClick={this.onSubmit} className="btn btn-default">Submit</button>
       
                </form>

                <div className= "container">
                  <h3>Results</h3>

                  <div class="panel panel-default">
                  <div class="panel-heading">ALERT</div>
                  <div class="panel-body">{this.state.alert}</div>
                  </div>

                  <div class="panel panel-default">
                  <div class="panel-heading">SERVER_ID</div>
                  <div class="panel-body">{this.state.server_id}</div>
                  </div>

                  <div class="panel panel-default">
                  <div class="panel-heading">RULES VIOLATED</div>
                {this.state.rules && this.state.rules.map( (rule, index) => {
                    return <div class="panel-body">{rule}</div>;
                  })}
                  </div>

                 </div>
            </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
