import React from 'react';
import { createRoot } from 'react-dom/client';

import Header from './components/Header/Header';
import Editor from './components/Editor/Editor';
import Ticker from './components/Ticker/Ticker';

import './index.scss';

const App = function () {
  return (
    <>
      <Header />
      <Ticker />
      <Editor />
    </>
  );
};

const element = document.getElementById('app');

createRoot(element!).render(<App />);
