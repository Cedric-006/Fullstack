
import { BrowserRouter as Router, Route, Routes,Navigate } from "react-router-dom";
import { Landingpage } from "../components.1/Landingpage";
import { Signup } from "../components.1/Signup";
import { SignIn } from "../components.1/SignIn";
function App() {
    
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Landingpage />} />
                <Route path="/signup"element={<Signup />} />
                <Route path="/signin"element={<SignIn />} />
            </Routes>
        </Router>

    )
}

export default App