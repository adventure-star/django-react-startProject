import React, { Component } from "react";
import ReactDOM from "react-dom";
 
 
class App extends Component {
 
  state = {
      data: ''
  };
 
  componentDidMount() {
      fetch("/api")
        .then(response => response.json())
        .then(data => this.setState({ data: JSON.stringify(data)}))
  }
 
  render(){
      const users = this.state.data;
     
      return (
        <div>
          <div>{users}</div>
        </div>
  )
 } 
} 

const wrapper = document.getElementById("app"); 
wrapper ? ReactDOM.render(<App />,wrapper) : null;