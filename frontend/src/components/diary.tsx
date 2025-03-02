import React, { useState } from "react";
import { Box } from "@mui/material";
import "./diary.css";

const Diary = () => {
  const [text, setText] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  return (
    <div className="ruled-paper">
      <Box className="content">
        <textarea 
          className="diary-textarea" 
          value={text} 
          onChange={handleChange} 
          placeholder="Write your notes here..." 
        />
      </Box>
    </div>
  );
};

export default Diary;
