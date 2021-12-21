import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [dbItems, setDbItems] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  useEffect(() => {
    fetch('/items').then(res => res.json()).then(data => {
      setDbItems(data.items);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
        <p>NEO4J DB Items: <br></br> {dbItems}.</p>
      </header>
    </div>
  );
}

export default App;