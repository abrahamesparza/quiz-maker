import React from "react"

function QuizBody({ results, hide }) {
    const categories = results.map(quiz => <li>{quiz.category}</li>);
    return (
        <ul>
            <li>{categories}</li>
        </ul>
    )
}

export default QuizBody