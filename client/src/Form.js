import React, { useState, useEffect } from "react";

import axios from "axios";

function Form() {
    const [formData, setFormData] = useState({
        'firstName': '',
        'lastName': '',
        'username': '',
        'email': '',
        'password': '',
    })

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value})
    }
    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('/user/signup', formData)
        .then(response => console.log(response.status))
        .catch(error => console.log(error))
    }

    return (
        <form div='signupForm' onSubmit={handleSubmit}>
            <label>First Name</label><br/>
            <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required/><br/>
            <label>Last Name</label><br/>
            <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required/><br/>
            <label>Username</label><br/>
            <input type="text" name="username" value={formData.username} onChange={handleChange} required/><br/>
            <label>Email</label><br/>
            <input type="text" name="email" value={formData.email} onChange={handleChange} required/><br/>
            <label>Password</label><br/>
            <input type="text" name="password" value={formData.password} onChange={handleChange} required/><br/>
            <button type="submit">Submit</button>
        </form>
    )
}

export default Form;