import React, { useEffect, useState } from 'react'
import axios from 'axios'
import QuizBody from './QuizBody'

function QuizMaker({ show }) {
    const [quizData, setQuizData] = useState([])
    
    useEffect(() => {
        axios.get('/quiz')
        .then(response => {
            setQuizData(response.data)
        })
        .catch(error => {
            console.log(`error: ${error}`)
        })
    }, [])

    return (
        <div className='quiz_table'>
            {/* working on logic to show/close quiz */}
            {/* <button type='button' onClick={clickCloseQuiz}>Close Quiz</button> */}

            {show ? <QuizBody results={quizData} hide={show}/> : ''}
        </div>
    )
}

export default QuizMaker