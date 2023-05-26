import React, { useState } from "react";

function SignUp( { formData, onChange, onSignUp }) {

    return (
        <div className="signupBody">
            <form  className='signupForm' onSubmit={onSignUp}>
                <p className="form-text">Sign Up For Access</p><br/>
                <label>First Name</label>
                <input type="text" name="firstName" value={formData.firstName} onChange={onChange} required/><br/>
                <label>Last Name</label>
                <input type="text" name="lastName" value={formData.lastName} onChange={onChange} required/><br/>
                <label>Username</label>
                <input type="text" name="username" value={formData.username} onChange={onChange} required/><br/>
                <label>Email</label>
                <input type="text" name="email" value={formData.email} onChange={onChange} required/><br/>
                <label>Password</label>
                <input type="password" name="password" value={formData.password} onChange={onChange} required/><br/>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default SignUp;