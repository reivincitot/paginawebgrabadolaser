import React, { useState } from 'react';
import Header from '../components/Header';
import axiosInstance from '../services/AxiosInstance';
import { useNavigate } from 'react-router-dom';
import Footer from '../components/Footer';

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setCredentials({...credentials, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axiosInstance.post('auth/login/', credentials);
      localStorage.setItem('accessToken', response.data.access);
      localStorage.setItem('refreshToken', response.data.refresh);
      navigate('/'); // Redirige a la página de inicio o dashboard según corresponda
    } catch (err) {
      console.error("Error during login:", err);
      setError('Invalid credentials. Please try again.');
    }
  };

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4 flex justify-center">
        <form onSubmit={handleSubmit} className="w-full max-w-sm bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Login</h1>
          {error && <p className="text-red-500 mb-2">{error}</p>}
          <div className="mb-4">
            <label className="block text-gray-700">Username</label>
            <input
              type="text"
              name="username"
              value={credentials.username}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              name="password"
              value={credentials.password}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <button type="submit" className="bg-blue-500 text-white w-full py-2 rounded hover:bg-blue-600">
            Login
          </button>
          <div className="mt-4 flex justify-center space-x-4">
            <button type="button" className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
              Login with Google
            </button>
            <button type="button" className="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-900">
              Login with Meta
            </button>
          </div>
        </form>
      </div>
      <Footer/>
    </div>
  );
};

export default Login;
