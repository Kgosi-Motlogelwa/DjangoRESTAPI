import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const [users, setUsers] = useState<[{age: number, name: string}]>()
  const [details, setDetails] = useState<{age: number, name: string}>()

  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000`)
      .then(res => {
        console.log("res.data: ", res.data)
        setDetails(res.data)
      })
  },[])

  const createNewUser = () => {
    if(details){
      alert("About to post with axios")
      axios.post('/', {
      name: details.name,
      age: details.age
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
    
  }

  return (
    <div className="App">
      <p style={{fontSize: "50px"}}>Simple React RTK Query :)</p>
      <br></br>
      {details ? <>
      <p style={{fontSize: "50px"}}>Name:  {details.name}</p>
      <p style={{fontSize: "50px"}}>Age: {details.age}</p>
      
      <form onSubmit={createNewUser}>
        <label>
          Name:
          <input type="text" name="name" value={details.name} onChange={(e) => setDetails({...details, name: e.target.value})}/>
        </label>
        <label>
          Age:
          <input type="number" name="age" value={details.age} onChange={(e) => setDetails({...details, age: Number(e.target.value)})}/>
        </label>
        <button type="submit">Submit</button>
      </form>
      </> : null}

      <ol>
        {users?.map(user =>{
          return <li key={user.name}>Name: {user.name}, Age: {user.age}</li>
        })}
      </ol>
    </div>
  );
}

export default App;
