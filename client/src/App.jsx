import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Landing from './Landing';
import SignUp from './SignUp';

function App() {
  let [formData, setFormData] = useState({})
  let [userCreated, setUserCreated] = useState(false)

  useEffect(() => {
    axios.get('/')
    .then(response => {
      console.log(response.status)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value})
  }

  const handleSignUp = (e) => {
    e.preventDefault()
    axios.post('/user/signup', formData)
    .then(response => {
        let status = response.status
        console.log(status)
        validateStatus(status)
    })
    .catch(error => console.log(error))
  }

  const validateStatus = (responseStatus) => {
    if (responseStatus === 201) {
        setUserCreated(true)
    } else {
        console.log(`Error with response status, code: ${responseStatus}`)
    }
  }

  return (
    <div className="app">
      {userCreated ? <Landing /> : <SignUp formData={formData} onChange={handleChange} onSignUp={handleSignUp}/> }
    </div>
  );
}

export default App;
