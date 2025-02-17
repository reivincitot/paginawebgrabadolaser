import React, { useState } from 'react';
import Header from '../components/Header';
import axiosInstance from '../services/AxiosInstance';
import { useNavigate } from 'react-router-dom';
import Footer from '../components/Footer';

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
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
      const response = await axiosInstance.post('auth/register/', formData);
      setSuccessMessage("Registration successful! Please check your email for confirmation.");
      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (err) {
      console.error("Registration error:", err);
      setError("Registration failed. Please try again.");
    }
  };

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4 flex justify-center">
        <form onSubmit={handleSubmit} className="w-full max-w-md bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Register</h1>
          {error && <p className="text-red-500 mb-2">{error}</p>}
          {successMessage && <p className="text-green-500 mb-2">{successMessage}</p>}
          <div className="mb-3">
            <input 
              type="text" 
              name="username" 
              placeholder="Username" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
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
          <div className="mt-4 flex justify-center space-x-4">
            <button type="button" className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
              Register with Google
            </button>
            <button type="button" className="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-900">
              Register with Meta
            </button>
          </div>
        </form>
      </div>
      <Footer/>
    </div>
  );
};

export default Register;
