import React, { useState } from "react";
//import axios from 'axios';
import OpenAI from "openai";
import "../styles/chatcomponent.css";
import styled from "styled-components";

const ChatContainer = styled.div`
  padding: 10px;
  border: 10px solid #57c4e1;
  border-radius: 8px;
  margin: 10px;
  padding-bottom: 60px;
  background-color: white;
  max-height: 580px;
  min-height: 580px;
  overflow: scroll;
`;

const MessageContainer = styled.div`
  margin-bottom: 0px;

  &.user {
    text-align: right;
    color: #007bff;
  }

  &.assistant {
    overflow-y: scroll;

    border-right: 2px solid;
    width: 0;
    animation: typing 1.5s steps(30, end) forwards, blinking 1s infinite;
    text-align: left;
    color: #000000;
    white-space: normal;
  }
`;

const InputContainer = styled.div`
  display: flex;
  position: sticky;
  top: 0;
  width: 92%;
  margin-left: 22px;
  margin-bottom: 20px;

  input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ccc;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    margin-left: -10px;
    margin-bottom: -10px;
  }

  button {
    background-color: #57c4e1;
    color: #fff;
    padding: 8px 12px;
    border: none;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    margin-bottom: -10px;
    cursor: pointer;
  }
`;

const ChatComponent = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSendMessage = async () => {
    // Make a request to the ChatGPT API with the user input
    //   const apiKey = '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';
    const openai = new OpenAI({
      apiKey: process.env.REACT_APP_OPENAI_API_KEY,
      dangerouslyAllowBrowser: true,
    });

    // const endpoint = 'https://api.openai.com/v1/completions';
    try {
      // Make a request to the ChatGPT API with the user input using the openai library
      const chatCompletion = await openai.chat.completions.create({
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: input },
        ],
        model: "gpt-3.5-turbo",
      });

      // Check if chatCompletion and chatCompletion.choices are defined
      if (chatCompletion && chatCompletion.choices) {
        // Access the content from the first choice in the array
        const content = chatCompletion.choices[0].message.content;
        setMessages([...messages, { role: "assistant", content }]);
      } else {
        console.error("chatCompletion or chatCompletion.choices is undefined");
      }

      // Clear the input field
      setInput("");
    } catch (error) {
      console.error("API Error:", error.response.data); // Log the error response
    }
  };

  return (
    <>
      <InputContainer
        onKeyUp={(e) => {
          if (e.key === "Enter") handleSendMessage();
        }}>
        <input type="text" value={input} onChange={handleInputChange} />
        <button onClick={handleSendMessage}>Send</button>
      </InputContainer>
      <ChatContainer>
        <div className="Typed">
          {messages.map((message, index) => (
            <MessageContainer key={index} className={message.role}>
              {message.content}
            </MessageContainer>
          ))}
        </div>
      </ChatContainer>
    </>
  );
};

export default ChatComponent;
