import './App.css';
import './components/chatcomponent.css'
import ChatComponent from './components/chatcomponent';
import JobDescription from './components/jobDescription';


function App() {
  return (
    <div className="App">
      <header className="App-header">
       {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <h1>
          Search Quest AI
        </h1>
      </header>
      <div className='container'>
        <div className='leftHalf'>
          <JobDescription />
        </div>
        <div className='rightHalf'>
          <ChatComponent />
        </div>
      </div>
    </div>
  );
}

export default App;
