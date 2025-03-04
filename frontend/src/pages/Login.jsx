// src/pages/Login.jsx
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import axiosInstance from '../services/AxiosInstance';

const Login = () => {
  const [credentials, setCredentials] = useState({ email: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axiosInstance.post('auth/login/', credentials, {
        headers: { "Content-Type": "application/json" },
      });
      // Suponiendo que usas JWT y la respuesta trae access y refresh tokens:
      localStorage.setItem("accessToken", response.data.access);
      localStorage.setItem("refreshToken", response.data.refresh);
      navigate('/'); // Redirige a la página de inicio o dashboard
    } catch (err) {
      console.error("Error during login:", err.response ? err.response.data : err);
      setError('Invalid credentials. Please try again.');
    }
  };

  const handleGoogleLogin = () => {
    window.location.href = 'http://localhost:8000/accounts/google/login/'; // 👈 URL correcta
  };
  
  const handleMetaLogin = () => {
    window.location.href = 'http://localhost:8000/accounts/facebook/login/'; // 👈 URL correcta
  };

  return (
    <Layout>
      <div className="container mx-auto p-4 flex justify-center">
        <form onSubmit={handleSubmit} className="w-full max-w-sm bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Login</h1>
          {error && <p className="text-red-500 mb-2">{error}</p>}
          <div className="mb-4">
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              name="email"
              value={credentials.email}
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
          <div className="mt-4 flex flex-col items-center space-y-2">
            <button
              type="button"
              onClick={handleGoogleLogin}
              className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
            >
              Login with Google
            </button>
            <button
              type="button"
              onClick={handleMetaLogin}
              className="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-900"
            >
              Login with Meta
            </button>
          </div>
          <div className="mt-4 text-center">
            <Link to="/reset-password" className="text-blue-500 underline">
              Forgot Password?
            </Link>
          </div>
          <div className="mt-4 text-center">
            <p>
              Don't have an account?{' '}
              <Link to="/register" className="text-blue-500 underline">
                Register here
              </Link>
            </p>
          </div>
        </form>
      </div>
    </Layout>
  );
};

export default Login;
