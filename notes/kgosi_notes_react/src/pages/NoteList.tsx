import React, {useState, useEffect} from 'react'
import axios from 'axios'
import ListItem from '../components/ListItem'
import AddButton from '../components/AddButton'


const NoteList = () => {    
    const [notes, setNotes] = useState([])
    useEffect(()=>{
        getNotes()
    },[])

    const getNotes = async() => {
        let response = undefined
        try {
            response = await axios.get('/api/notes/');
            console.log(response);
            
          } catch (error) {
            console.error(error);
          }
          
          if(response){
            setNotes(response.data)
          }
    }

  return (
    <div className="notes">
        <div className="notes-header">
          <h2 className="notes-title">&#9782; Notes</h2>
          <p className="notes-count">{notes.length}</p>
        </div>
        <div className="notes-list">
        {notes.map((val: any, index: any)=>{
            return <ListItem key={index} note = {val}/>
        })}
        </div>
        <AddButton/>
    </div>
  )
}

export default NoteList