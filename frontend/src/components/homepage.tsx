import { Button } from "@mui/material";
import { Link } from "react-router-dom";

function HomePage() {
    return (
      <div className = "buttons-container">
        <h1 className="title">Whatup-Bot: Mental Health assistant</h1>
        <h2 className = "subtitle">HOME PAGE</h2>
        <Button 
          variant="contained" 
        //   className="homepageButtons" 
          component={Link} 
          to="/diary"
        >
          Diary
        </Button>
      </div>
    );
  }
  
  export default HomePage;  