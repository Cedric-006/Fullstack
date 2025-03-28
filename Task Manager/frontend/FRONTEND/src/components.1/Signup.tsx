import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { registerUser } from '../api';
import { AxiosError } from 'axios';

interface SignUpProps {
    setSignupMessage : (msg: string) => void;
}

export const SignUp: React.FC<SignUpProps> = ({ setSignUpMesage}) => {
    const [ username, setUsername ] = useState ('');
    const [ password, setPassword ] = useState ('');
    const [ error, setError ] = useState<string | null>(null);
    const Navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        try{
            const response = registerUser({username, password});
            setSignUpMesage(response.data.msg ?? null);
            Navigate('/signin');
        }catch (err){
            const axiosError = err as AxiosError<{ msg?: string }>;
            setError(axiosError.response?.data.msg ?? 'Registration failed');
        };
};
return(
    <div className="flex items-center justify-center min-h-screen">
        <form onSubmit={handleSubmit}className="bg-white p-6 rounded shadow-md w-96">
            <h2 className="text-2xl font-bold mb-4">Sign Up</h2>
            {error && <p className="text-red-500 mb-4">{error}</p>}
            <input 
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full p-2 mb-4 border rounded"
            type="text"
            placeholder="Enter your username" 
            />
            <input
            className="w-full p-2 mb-4 border rounded"
            type="text"
            placeholder="Enter your password"
            />
            {error && <p className="text-red-500 mb-4">{error}</p>}
            <button className="w-full bg-blue-500 text-white p-2 rounded hover:bg-bluen-600" type="submit" onClick={handleSubmit}>Sign Up</button> 
        </form>
        <div></div>
    </div>
);
}