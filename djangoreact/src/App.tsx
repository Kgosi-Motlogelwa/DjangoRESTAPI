import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {

  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000`)
      .then(res => {
        console.log("res.data: ", res.data)
      })
  },[])

  return (
    <div className="App">
      <p style={{fontSize: "50px"}}>Simple React RTK Query :)</p>
    </div>
  );
}

export default App;
