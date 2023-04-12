import React, { useEffect, useState } from 'react'
import axios from 'axios'

import QuizMaker from './QuizMaker'
import Form from './Form'

function App() {
  const [showQuiz, setShowQuiz] = useState(false)

  useEffect(() => {
    axios.get('/')
    .then(response => {
      console.log(response.status)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  function clickShowQuiz() {
    if (!showQuiz) {
      setShowQuiz(true)
    }
  }
  /*
  removed below to replace in a new page upon successful signup
  {showQuiz ? <QuizMaker show={showQuiz}/> : <button type='button' onClick={clickShowQuiz}>Show Quiz</button>}
  */
  return (
    <div className="App">
      <header className="App-header">
        <Form />
      </header>
    </div>
  );
}

export default App;
