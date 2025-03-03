import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import './ChatRoom.css';

const ChatRoom: React.FC = () => {
  const [messages, setMessages] = useState<
    { role: string; text: string; timestamp: number }[]
  >([]);
  const [message, setMessage] = useState('');
  // Set role as either 'patient' or 'doctor' (this can come from props or firebase auth)
  const [role] = useState('patient'); 
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const socketRef = useRef<any>(null);

  useEffect(() => {
    // Connect to your socket server
    socketRef.current = io('http://localhost:5000');

    socketRef.current.on('connect', () => {
      console.log('Connected to chat server');
    });

    // Listen for incoming messages
    socketRef.current.on('message', (msg: { role: string; text: string; timestamp: number }) => {
      setMessages(prevMessages => [...prevMessages, msg]);
    });

    // Clean up on unmount
    return () => {
      socketRef.current.disconnect();
    };
  }, []);

  // Scroll to bottom on new messages
  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  const sendMessage = () => {
    if (message.trim() !== '') {
      const msgObj = { role, text: message, timestamp: Date.now() };
      // Emit the message via socket
      socketRef.current.emit('message', msgObj);
      setMessages(prevMessages => [...prevMessages, msgObj]);
      setMessage('');
    }
  };

  // If user presses Enter (without Shift), send the message
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Chat Room</h2>
        <p>You are logged in as <strong>{role}</strong></p>
      </div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.role}`}>
            <span className="chat-message-role">{msg.role}: </span>
            <span className="chat-message-text">{msg.text}</span>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="chat-input-container">
        <textarea
          className="chat-input"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} className="chat-send-button">
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatRoom;
