// src/pages/ResetPassword.jsx
import React, { useState } from 'react';
import Layout from '../components/Layout';
import axiosInstance from '../services/AxiosInstance';

const ResetPassword = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setMessage('');
    try {
      await axiosInstance.post('auth/password-reset/', { email }, {
        headers: { "Content-Type": "application/json" },
      });
      setMessage("Password reset email sent! Please check your inbox.");
    } catch (err) {
      console.error("Error during password reset:", err.response ? err.response.data : err);
      setError("Failed to send password reset email. Please try again.");
    }
  };

  return (
    <Layout>
      <div className="container mx-auto p-4 flex justify-center">
        <form onSubmit={handleSubmit} className="w-full max-w-sm bg-white p-6 rounded shadow">
          <h1 className="text-2xl font-bold mb-4">Reset Password</h1>
          {message && <p className="text-green-500 mb-2">{message}</p>}
          {error && <p className="text-red-500 mb-2">{error}</p>}
          <div className="mb-4">
            <label className="block text-gray-700">Enter your email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <button type="submit" className="bg-blue-500 text-white w-full py-2 rounded hover:bg-blue-600">
            Send Reset Email
          </button>
        </form>
      </div>
    </Layout>
  );
};

export default ResetPassword;
