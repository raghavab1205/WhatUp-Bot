// import { useState } from 'react'
import { Routes, Route } from "react-router-dom";
import HomePage from "./components/homepage.tsx";
import Diary from "./components/diary.tsx";
import ChatRoom from "./components/chatroom.tsx";
const App: React.FC = () => {
  // const [count, setCount] = useState(0)

  return (
    <Routes>
      <Route path="/" element={<HomePage/>}/>
      <Route path= "/diary" element = {<Diary/>}/>
      <Route path="/chatroom" element = {<ChatRoom/>}/>
    </Routes>
  )
}

export default App
