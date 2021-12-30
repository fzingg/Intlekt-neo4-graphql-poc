import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import VisNetwork from './VisNetwork';
import VisNetworkWithClass from './VisNetworkWithClass';
import { Container } from '@material-ui/core';
import Graphindemo1 from './Graphindemo1';
import Graphindemo2 from './Graphindemo2';
import Graphindemo3 from './Graphindemo3';
import Graphindemo4 from './Graphindemo4';
import Graphindemo5 from './Graphindemo5';
import Graphindemo6 from './Graphindemo6';
import Graphindemo7 from './Graphindemo7';
import Graphindemo8 from './Graphindemo8';
import Graphindemo9 from './Graphindemo9';
import GraphinIcons from './GraphinIcons';

ReactDOM.render(

  // <Container component="main" maxWidth="lg" className="main">
  <Graphindemo9 />
  // </Container>


  ,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
