import React from "react";

import LogIn from "./LogIn";
import SignUp from "./SignUp";
import Landing from "./Landing";


function Page({ page, formData, handleChange, handleSignUp }) {
    if (!page) {
        return ''
    }
    if (page === 'login') {
        return <LogIn formData={formData} onChange={handleChange} onSignUp={handleSignUp} />;
    }
    if (page === 'signup') {
        return <SignUp formData={formData} onChange={handleChange} onSignUp={handleSignUp}/>;
    }
}

export default Page;