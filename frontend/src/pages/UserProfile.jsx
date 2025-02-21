// src/pages/UserProfile.jsx
import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import axiosInstance from '../services/AxiosInstance';
import { Link } from 'react-router-dom';

const UserProfile = () => {
  const [userData, setUserData] = useState(null);
  const [orderHistory, setOrderHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const userResponse = await axiosInstance.get('users/profile/');
        setUserData(userResponse.data);
      } catch (err) {
        console.error("Error fetching user data:", err);
        setError("Failed to load user data.");
      }
    };

    const fetchOrderHistory = async () => {
      try {
        const ordersResponse = await axiosInstance.get('orders/');
        setOrderHistory(ordersResponse.data);
      } catch (err) {
        console.error("Error fetching order history:", err);
        setError("Failed to load order history.");
      }
    };

    Promise.all([fetchUserData(), fetchOrderHistory()]).then(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <Layout>
        <div className="container mx-auto p-4 text-center">
          <p>Loading profile...</p>
        </div>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout>
        <div className="container mx-auto p-4 text-center">
          <p className="text-red-500">{error}</p>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6">User Profile</h1>
        {userData ? (
          <div className="bg-white p-6 rounded shadow mb-6">
            <h2 className="text-2xl font-semibold mb-2">Personal Information</h2>
            <p><strong>Username:</strong> {userData.username || "Not provided"}</p>
            <p><strong>Email:</strong> {userData.email || "Not provided"}</p>
            <p><strong>Phone:</strong> {userData.phone_number || "Not provided"}</p>
            <p>
              <Link to="/profile/edit" className="text-blue-500 underline">
                Complete/Update your profile
              </Link>
            </p>
          </div>
        ) : (
          <div className="text-center">
            <p>No user data available.</p>
            <Link to="/register" className="text-blue-500 underline">
              Register here
            </Link>
          </div>
        )}
        <div className="bg-white p-6 rounded shadow">
          <h2 className="text-2xl font-semibold mb-2">Order History</h2>
          {orderHistory.length > 0 ? (
            <ul className="divide-y">
              {orderHistory.map(order => (
                <li key={order.id} className="py-2">
                  <p><strong>Order ID:</strong> {order.id}</p>
                  <p><strong>Status:</strong> {order.status}</p>
                  <p><strong>Date:</strong> {order.date}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No orders found.</p>
          )}
        </div>
      </div>
    </Layout>
  );
};

export default UserProfile;
