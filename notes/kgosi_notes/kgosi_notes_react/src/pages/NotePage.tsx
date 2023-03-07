import React, { useState, useEffect } from 'react'
import { useParams, Link, useNavigate } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg"


import axios from "axios"

const NotePage = () => {
  const {id} = useParams();
  const navigate = useNavigate()
  const [note, setNote] = useState<{id: number, body: string, updated: string, created: string}>()
  const [newNote, setNewNote] = useState<{body: string}>()

  useEffect(()=>{
    getNote()
    console.log("id: ", id)
  },[])


  const getNote = async() => {
    let response = undefined
    try{
        response = await axios.get(`/api/notes/${id}`)
        console.log("response: ", response)
    }catch (error){
        console.error(error)
    }

    if(response){
      setNote(response.data)
    }
  }

  // const updateNote = async() => {
  //   alert("UPDATE clicked")
  //   let response = undefined
  //   try{
  //     response = await axios.put(`http://127.0.0.1:8000/api/notes/${id}/update/`, {body: note});
  //     console.log(response)
  //   } catch(error){
  //     console.error(error)
  //   }
  // }

  const updateNote = async() => {
    // alert("UpdateNote Ran")
    fetch(`/api/notes/${id}/` , {
      method: "PUT",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(note)
    })
  } 

  const deleteNote = async() => {
    alert("DELETE")
    fetch(`/api/notes/${id}/` , {
      method: "DELETE",
      headers: {
        'Content-Type': 'application/json'
      }
    })
    navigate('/')
  } 

  const createNote = async() => {
    console.log("Note being created: ", newNote)
    fetch(`/api/notes/`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newNote)
    })
  }

  const updateState = (e: any) => {
    if(note){
      setNote({...note, body: e.target.value})
    }
    setNewNote({body: e.target.value})
  }

  let handleSubmit = () => {
    console.log("newNote: ", newNote)
    console.log("note: ", note)
    if(id && newNote){
      updateNote()
    }else if(!id && newNote?.body.length && newNote?.body.length > 0){
      createNote()
    }
    // Go back to home page
    navigate('/')
  }
  
    return (
    <div className="note">
        <div className="note-header">
            <h3>
              {((id && note?.body === "") || (id && newNote?.body === "")) ? <ArrowLeft onClick={ deleteNote }/>
                : <ArrowLeft onClick={handleSubmit}/>
             }
            </h3>
            {(id && !newNote) || (id && note?.body === "")? <button onClick={deleteNote}>Delete</button>
             : <button onClick={handleSubmit}>Done</button>
             }
        </div>
        <textarea onChange ={updateState} defaultValue = { note?.body }></textarea>
    </div>
  )
}

export default NotePage