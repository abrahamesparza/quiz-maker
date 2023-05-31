import React from "react";

function LogIn({formData, onChange, onLogIn}) {

    return (
        <div className="loginBody">
            <form  className='loginForm' onSubmit={onLogIn}>
                <p className="form-text">Welcome Back! Login for access.</p>
                <label>Username</label>
                <input type="text" name="username" value={formData.username} onChange={onChange} required/><br/>
                <label>Password</label>
                <input type="password" name="password" value={formData.password} onChange={onChange} required/><br/>
                <button type="submit">Submit</button>
            </form>
            <div className="signup-button">
                <p>Click here to create a new account.</p>
            </div>
        </div>
    )
}

export default LogIn;