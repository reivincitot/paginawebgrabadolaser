// src/routes/AppRoutes.jsx
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Catalog from '../pages/Catalog';
import Cart from '../pages/Cart';
import Checkout from '../pages/Checkout';
import Login from '../pages/Login';
import UserProfile from '../pages/UserProfile';
import Dashboard from '../pages/Dashboard';

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/catalog" element={<Catalog />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
