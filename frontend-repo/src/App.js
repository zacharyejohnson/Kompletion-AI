import "./App.css";
import "./styles/jobDescription.css";
import ChatComponent from "./components/chatcomponent";
import JobDescription from "./components/jobDescription";
import paperTexture from "../src/paper-texture.jpg";

function App() {
  console.log(paperTexture);
  return (
    <div className="App">
      <header className="App-header">
        <h1>Search Quest AI</h1>
      </header>
      <div style={{ backgroundImage: `url(${paperTexture})` }}>
        <div
          className="container"
          style={{
            width: "100%",
            backgroundColor: "rgb(0, 0, 0, 0.5)",
          }}>
          <div className="leftHalf">
            <JobDescription />
          </div>
          <div className="rightHalf">
            <ChatComponent />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
