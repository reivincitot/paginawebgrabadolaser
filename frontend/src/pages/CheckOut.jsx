// src/pages/Checkout.jsx
import React, { useState } from 'react';
import Header from '../components/Header';
import axiosInstance from '../services/AxiosInstance';
import { useNavigate } from 'react-router-dom';
import Footer from '../components/Footer';

const Checkout = () => {
  const [shippingInfo, setShippingInfo] = useState({
    fullName: '',
    address: '',
    city: '',
    postalCode: '',
    country: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setShippingInfo({
      ...shippingInfo,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMessage('');
    setLoading(true);
    try {
      // Supongamos que tienes un endpoint para crear una orden de checkout, por ejemplo: orders/checkout/
      const response = await axiosInstance.post('orders/checkout/', shippingInfo);
      setSuccessMessage("Order created successfully!");
      // Una vez creada la orden, redirige al usuario (por ejemplo, a la página de pago o confirmación)
      navigate('/order-confirmation'); // Ajusta esta ruta según tu flujo
    } catch (err) {
      console.error("Checkout error:", err);
      setError("Failed to process your checkout. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6">Checkout</h1>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        {successMessage && <p className="text-green-500 mb-4">{successMessage}</p>}
        <form onSubmit={handleSubmit} className="max-w-lg mx-auto bg-white p-6 rounded shadow">
          <div className="mb-4">
            <label className="block text-gray-700">Full Name</label>
            <input
              type="text"
              name="fullName"
              value={shippingInfo.fullName}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Address</label>
            <input
              type="text"
              name="address"
              value={shippingInfo.address}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div className="mb-4 grid grid-cols-2 gap-4">
            <div>
              <label className="block text-gray-700">City</label>
              <input
                type="text"
                name="city"
                value={shippingInfo.city}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div>
              <label className="block text-gray-700">Postal Code</label>
              <input
                type="text"
                name="postalCode"
                value={shippingInfo.postalCode}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Country</label>
            <input
              type="text"
              name="country"
              value={shippingInfo.country}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white w-full py-2 rounded hover:bg-blue-600 transition-colors"
            disabled={loading}
          >
            {loading ? "Processing..." : "Confirm Order & Pay"}
          </button>
        </form>
      </div>
      <Footer/>
    </div>
  );
};

export default Checkout;
