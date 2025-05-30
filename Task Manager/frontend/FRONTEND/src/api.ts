import axios from "axios";
import { AuthResponse, Task, TaskCreatePayload } from "./types";

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    headers: {'Content-Type': 'application/json'}
});


export const registerUser =(user: {username: string; password: string}) => api.
post<Response>('/login', user);

export const LoginUser =(user: {username: string; password: string}) => api.
post<Response>('/login', user);

export const addTask =(task: TaskCreatePayload, token:string)=>api.
post<Response>('/tasks', task, {headers:{Authorization: `Bearer ${token}`}})

export const getTasks = (token: string) => api.get<Task[]>('/tasks', {headers: {Authorization: `Bearer ${token}`}})