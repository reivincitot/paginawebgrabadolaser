// src/pages/Register.jsx
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import axiosInstance from '../services/AxiosInstance';
import countries from '../data/countries.json'; 

const Register = () => {
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    first_name: '',
    last_name: '',
    phone_number: '',
    country_code: countries[0].code, // Valor por defecto
    address: '',
    birthdate: '',
    password: '',
    password2: '',
  });
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
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
        const errorMessages = Object.entries(err.response.data)
          .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
          .join(' | ');
        setError(errorMessages);
      } else {
        setError("Registration failed. Please try again.");
      }
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
        <form onSubmit={handleSubmit} className="w-full max-w-lg bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Register</h1>
          {error && <p className="text-red-500 mb-2">{error}</p>}
          {successMessage && <p className="text-green-500 mb-2">{successMessage}</p>}
          
          {/* Email */}
          <div className="mb-3">
            <label className="block text-gray-700">Email</label>
            <input 
              type="email" 
              name="email" 
              placeholder="Email" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Username */}
          <div className="mb-3">
            <label className="block text-gray-700">Username</label>
            <input 
              type="text" 
              name="username" 
              placeholder="Username" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* First Name */}
          <div className="mb-3">
            <label className="block text-gray-700">First Name</label>
            <input 
              type="text" 
              name="first_name" 
              placeholder="First Name" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Last Name */}
          <div className="mb-3">
            <label className="block text-gray-700">Last Name</label>
            <input 
              type="text" 
              name="last_name" 
              placeholder="Last Name" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Phone Number with Country Code */}
          <div className="mb-3 flex space-x-2">
            <div className="w-1/3">
              <label className="block text-gray-700">Country Code</label>
              <select 
                name="country_code"
                value={formData.country_code}
                onChange={handleChange}
                className="w-full border p-2 rounded"
              >
                {countries.map(country => (
                  <option key={country.code} value={country.code}>
                    {country.flag} {country.code}
                  </option>
                ))}
              </select>
            </div>
            <div className="w-2/3">
              <label className="block text-gray-700">Phone Number</label>
              <input 
                type="text" 
                name="phone_number" 
                placeholder="Phone Number" 
                onChange={handleChange} 
                className="border p-2 rounded w-full"
                required
              />
            </div>
          </div>
          {/* Address */}
          <div className="mb-3">
            <label className="block text-gray-700">Address</label>
            <input 
              type="text" 
              name="address" 
              placeholder="Address" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Birthdate */}
          <div className="mb-3">
            <label className="block text-gray-700">Birthdate</label>
            <input 
              type="date" 
              name="birthdate" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Password */}
          <div className="mb-3">
            <label className="block text-gray-700">Password</label>
            <input 
              type="password" 
              name="password" 
              placeholder="Password" 
              onChange={handleChange} 
              className="border p-2 rounded w-full"
              required
            />
          </div>
          {/* Confirm Password */}
          <div className="mb-3">
            <label className="block text-gray-700">Confirm Password</label>
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
