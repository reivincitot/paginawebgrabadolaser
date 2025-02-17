// src/pages/Dashboard.jsx
import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import axiosInstance from '../services/AxiosInstance';
import Footer from '../components/Footer';

const Dashboard = () => {
  const [salesReport, setSalesReport] = useState(null);
  const [paymentReport, setPaymentReport] = useState(null);
  const [shippingReport, setShippingReport] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const [salesRes, paymentRes, shippingRes] = await Promise.all([
          axiosInstance.get('reports/sales-reports/'),
          axiosInstance.get('reports/payment-reports/'),
          axiosInstance.get('reports/shipping-reports/'),
        ]);
        // Asumimos que el reporte del día actual es el primero de la lista
        setSalesReport(salesRes.data[0]);
        setPaymentReport(paymentRes.data[0]);
        setShippingReport(shippingRes.data[0]);
      } catch (err) {
        console.error("Error fetching reports:", err);
        setError("Failed to load reports.");
      } finally {
        setLoading(false);
      }
    };

    fetchReports();
  }, []);

  if (loading) {
    return (
      <div>
        <Header />
        <div className="container mx-auto p-4">
          <p>Loading dashboard...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <Header />
        <div className="container mx-auto p-4">
          <p className="text-red-500">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6">Admin Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Sales Report */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-semibold mb-2">Sales Report</h2>
            {salesReport ? (
              <div>
                <p><strong>Total Orders:</strong> {salesReport.total_orders}</p>
                <p><strong>Total Revenue:</strong> ${salesReport.total_revenue}</p>
                <p><strong>Completed Orders:</strong> {salesReport.total_completed_orders}</p>
              </div>
            ) : (
              <p>No sales data available.</p>
            )}
          </div>
          {/* Payment Report */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-semibold mb-2">Payment Report</h2>
            {paymentReport ? (
              <div>
                <p><strong>Total Payments:</strong> {paymentReport.total_payments}</p>
                <p><strong>Total Amount:</strong> ${paymentReport.total_amount}</p>
                <p><strong>Failed Payments:</strong> {paymentReport.failed_payments}</p>
              </div>
            ) : (
              <p>No payment data available.</p>
            )}
          </div>
          {/* Shipping Report */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-semibold mb-2">Shipping Report</h2>
            {shippingReport ? (
              <div>
                <p><strong>Total Shipments:</strong> {shippingReport.total_shipments}</p>
                <p><strong>Delivered Shipments:</strong> {shippingReport.delivered_shipments}</p>
                <p><strong>Pending Shipments:</strong> {shippingReport.pending_shipments}</p>
              </div>
            ) : (
              <p>No shipping data available.</p>
            )}
          </div>
        </div>
      </div>
      <Footer/>
    </div>
  );
};

export default Dashboard;
