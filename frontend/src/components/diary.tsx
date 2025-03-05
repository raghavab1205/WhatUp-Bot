import React, { useState } from "react";
import axios from "axios";
import { Box } from "@mui/material";
import "./diary.css";

const Diary: React.FC = () => {
  const [paragraphs, setParagraphs] = useState<string[]>([]);
  const [currentText, setCurrentText] = useState<string>("");
  const [prediction, setPrediction] = useState<string | null>(null);

  const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCurrentText(event.target.value);
  };

  // When Enter is pressed without Shift, store the paragraph, clear the textarea,
  // and send the text to the Flask API for prediction.
  const handleKeyDown = async (event: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      if (currentText.trim() !== "") {
        // Optionally update the UI immediately with the new paragraph
        setParagraphs([...paragraphs, currentText]);

        try {
          // POST the text to the Flask /predict endpoint
          const response = await axios.post("http://127.0.0.1:5000/predict", { text: currentText });
          setPrediction(response.data.prediction);
        } catch (error) {
          console.error("Error during prediction:", error);
        }
        setCurrentText("");
      }
    }
  };

  return (
    <div className="ruled-paper">
      <Box className="content">
        {paragraphs.map((para, index) => (
          <p key={index} className="paragraph">
            {para}
          </p>
        ))}
        <textarea
          className="diary-textarea"
          value={currentText}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder="Write your notes here..."
        />
        {prediction !== null && (
          <div className="prediction">Prediction: {prediction}</div>
        )}
      </Box>
    </div>
  );
};

export default Diary;
