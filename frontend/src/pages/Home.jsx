// src/pages/Home.jsx
import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import ProductCard from '../components/ProductCard';
import { getProducts } from '../services/productServices';

const Home = () => {
  const [featuredProducts, setFeaturedProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchFeaturedProducts = async () => {
      try {
        const data = await getProducts();
        // Supongamos que los primeros 4 productos son destacados
        setFeaturedProducts(data.slice(0, 4));
      } catch (error) {
        console.error("Error fetching featured products:", error);
        setError("Failed to fetch featured products.");
      } finally {
        setLoading(false);
      }
    };
    fetchFeaturedProducts();
  }, []);

  return (
    <Layout>
      {/* Sección Hero */}
      <section className="bg-gray-200 py-20">
        <div className="container mx-auto text-center">
          <h1 className="text-4xl font-bold mb-4">Welcome to Grabados Láser 8102 GyP</h1>
          <p className="text-xl mb-8">Find the best products at the best prices.</p>
          <a
            href="/catalog"
            className="bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700 transition-colors"
          >
            Shop Now
          </a>
        </div>
      </section>
      
      {/* Sección de productos destacados */}
      <section className="py-10">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold mb-6 text-center">Featured Products</h2>
          {loading ? (
            <p className="text-center">Loading featured products...</p>
          ) : error ? (
            <p className="text-center text-red-500">{error}</p>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
              {featuredProducts.map(product => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          )}
        </div>
      </section>
    </Layout>
  );
};

export default Home;
