// Removed unused React import
import { BrowserRouter as Router, Route, Routes,Navigate } from "react-router-dom";
import { Landingpage } from "./components.1/Landingpage";
import { SignUp } from "./components.1/Signup";
import { SignIn } from "./components.1/SignIn";
import Dashboard from "./components.1/Dashboard";
import { useState } from "react";

function App() {}
    const [token, setToken] = useState<string | null>(localStorage.getItem('token'));
    const [signupmessage, setSignupMessage]= useState<string |null>(null);

    const handleLogin = (token: string) => {
        setToken(newToken)
        localStorage.setItem('token', newToken)
    }
    const handleLogout = () => {
        setToken(null);
        localStorage.removeItem('token')
    
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Landingpage />} />
                <Route path="/signup"element={<SignUp />} />
                <Route path="/signin"element={<SignIn />} />
                <Route path="/dashboard"element={<Dashboard />} />
            </Routes>
        </Router>

    )
}

export default App