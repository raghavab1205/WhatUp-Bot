import React, { useState } from "react";
import { Box } from "@mui/material";
import "./diary.css";

const Diary = () => {
  // paragraphs stores each entered paragraph
  const [paragraphs, setParagraphs] = useState<string[]>([]);
  // currentText holds the value of the current textarea
  const [currentText, setCurrentText] = useState("");

  // Update the current text as the user types
  const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCurrentText(event.target.value);
  };

  // When Enter is pressed without Shift, store the paragraph and clear the textarea.
  // Shift+Enter will allow a new line within the same paragraph.
  const handleKeyDown = (event: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault(); // prevent newline insertion
      if (currentText.trim() !== "") {
        setParagraphs([...paragraphs, currentText]);
        setCurrentText("");
      }
    }
  };

  return (
    <div className="ruled-paper">
      <Box className="content">
        {/* Render stored paragraphs */}
        {paragraphs.map((para, index) => (
          <p key={index} className="paragraph">{para}</p>
        ))}
        {/* Textarea for new input */}
        <textarea
          className="diary-textarea"
          value={currentText}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder="Write your notes here..."
        />
      </Box>
    </div>
  );
};

export default Diary;
