import "./App.css";
import "./styles/jobDescription.css";
import { useState } from "react";
import ChatComponent from "./components/chatcomponent";
import JobDescription from "./components/jobDescription";

function App() {
  const [suggestedQuestions, setSuggestedQuestions] = useState([]);
  const [category, setCategory] = useState("Home");
  return (
    <div className="App">
      <div>
        <div
          className="container"
          style={{
            width: "100%",
          }}>
          <div className="leftHalf">
            <JobDescription
              setSuggestedQuestions={setSuggestedQuestions}
              setCategory={setCategory}
            />
          </div>
          <div className="rightHalf">
            <ChatComponent
              suggestedQuestions={suggestedQuestions}
              category={category}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
