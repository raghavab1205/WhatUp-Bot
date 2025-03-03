import { Button } from "@mui/material";
import { Link } from "react-router-dom";
import "./HomePage.css";

function HomePage() {
  return (
    <div className="homepage-container">
      {/* Header section: title and subtitle at the top */}
      <div className="header">
        <h1 className="title">Whatup-Bot: Mental Health Assistant</h1>
        <h2 className="subtitle">HOME PAGE</h2>
      </div>

      {/* Buttons centered on the page */}
      <div className="buttons-container">
        <Button 
          variant="contained" 
          className="homepageButtons" 
          component={Link} 
          to="/diary"
        >
          Diary
        </Button>
        <Button 
          variant="contained" 
          className="homepageButtons" 
          component={Link} 
          to="/chatroom"
        >
          Start a Conversation
        </Button>
      </div>
    </div>
  );
}

export default HomePage;
