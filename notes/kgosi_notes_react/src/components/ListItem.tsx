import React, {FC} from 'react'
import { Link } from 'react-router-dom'

interface Props {
    note: {
        id: number,
        body: string,
        updated: string,
        created: string 
    }
}

let getTime = (note: {id: number, body: string, updated: string, created: string}) => {
  return new Date(note.updated).toLocaleDateString()
}

let getTitle = (note: string) => {

  let title = note.split('\n')[0]
  if(title.length > 45){
    return title.slice(0, 45) + " ..."
  }
  return title
}

const ListItem: FC<Props> = ({note}: Props) => {
  return (
    <Link to={`/notes/${note.id}`}>
        <div className="notes-list-item">
           <h3>{getTitle(note?.body)}</h3> 
           <p><span>{getTime(note)}</span></p>
        </div>
    </Link>
  )
}

export default ListItem