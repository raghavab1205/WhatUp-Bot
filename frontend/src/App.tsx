// import { useState } from 'react'
import { Routes, Route } from "react-router-dom";
import HomePage from "./components/homepage.tsx";
import Diary from "./components/diary.tsx";
const App: React.FC = () => {
  // const [count, setCount] = useState(0)

  return (
    <Routes>
      <Route path="/" element={<HomePage/>}/>
      <Route path= "Diary" element = {<Diary/>}/>
    </Routes>
  )
}

export default App
