// src/pages/Register.jsx
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import axiosInstance from '../services/AxiosInstance';

const Register = () => {
  const [formData, setFormData] = useState({
    email: '',
    phone_number: '',
    password: '',
    password2: '',
  });
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await axiosInstance.post('auth/register/', formData, {
        headers: { "Content-Type": "application/json" },
      });
      setSuccessMessage("Registration successful! Please check your email for confirmation.");
      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (err) {
      console.error("Registration error:", err.response ? err.response.data : err);
      if (err.response && err.response.data) {
        // Formatea el error para mostrarlo de forma amigable
        const errorMessages = Object.entries(err.response.data)
          .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
          .join(' | ');
        setError(errorMessages);
      } else {
        setError("Registration failed. Please try again.");
      }
    }
  };

  const handleGoogleRegister = () => {
    window.location.href = 'http://127.0.0.1:8000/api/auth/google/';
  };

  const handleMetaRegister = () => {
    window.location.href = 'http://127.0.0.1:8000/api/auth/meta/';
  };

  return (
    <Layout>
      <div className="container mx-auto p-4 flex justify-center">
        <form onSubmit={handleSubmit} className="w-full max-w-md bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Register</h1>
          {error && <p className="text-red-500 mb-2">{error}</p>}
          {successMessage && <p className="text-green-500 mb-2">{successMessage}</p>}
          <div className="mb-3">
            <input 
              type="email" 
              name="email" 
              placeholder="Email" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          <div className="mb-3">
            <input 
              type="text" 
              name="phone_number" 
              placeholder="Phone Number" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
            />
          </div>
          <div className="mb-3">
            <input 
              type="password" 
              name="password" 
              placeholder="Password" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          <div className="mb-3">
            <input 
              type="password" 
              name="password2" 
              placeholder="Confirm Password" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          <button type="submit" className="bg-blue-500 text-white w-full py-2 rounded hover:bg-blue-600 transition-colors">
            Register
          </button>
          <div className="mt-4 flex flex-col items-center space-y-2">
            <button
              type="button"
              onClick={handleGoogleRegister}
              className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
            >
              Register with Google
            </button>
            <button
              type="button"
              onClick={handleMetaRegister}
              className="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-900"
            >
              Register with Meta
            </button>
          </div>
          <div className="mt-4 text-center">
            <p>
              Already have an account?{' '}
              <Link to="/login" className="text-blue-500 underline">
                Login here
              </Link>
            </p>
          </div>
        </form>
      </div>
    </Layout>
  );
};

export default Register;
