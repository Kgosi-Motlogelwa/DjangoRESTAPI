import { BrowserRouter as Router, Route ,Link, Routes} from "react-router-dom";

import './App.css';
import Header from './components/Header';
import NoteList from './pages/NoteList';
import NotePage from "./pages/NotePage";


function App() {
  return (
      <div className="container dark">
        <div className="app">
            <Header/>
            <Routes>
              <Route  path="/" element={<NoteList />} />
              <Route  path="/notes" element={<NotePage />} />
              <Route  path="/notes/:id" element={<NotePage />} />
              
            </Routes>
        </div>  
      </div>
      
  );
}

export default App;
