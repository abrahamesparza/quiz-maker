import React, { useState } from "react";
import TypeWriter from 'typewriter-effect'
import Page from "./Page";

function Landing({ formData, handleChange, handleSignUp }) {
    let [page, setPage] = useState('')

    function handleComponentRender(e) {
        if (!page) {
            setPage(e.target.name)
        }
        else if (page !== e.target.name) {
            setPage(e.target.name)
        }
        else {
            setPage('')
        }
    }

    console.log('page:', page)
    return (
        <div>
            <div className="landing-nav">
                <button onClick={handleComponentRender} name="signup" className="form-button">Sign Up</button>
                <button onClick={handleComponentRender} name="login" className="form-button">Log In</button>
            </div>
            <Page page={page} formData={formData} onChange={handleChange} onSignUp={handleSignUp}/>
        </div>
    )
}

export default Landing;