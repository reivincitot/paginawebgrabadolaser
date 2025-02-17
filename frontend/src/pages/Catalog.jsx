import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import ProductCard from '../components/ProductCard';
import { getProducts } from '../services/productServices';
import Footer from '../components/Footer';

const Catalog = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await getProducts();
        setProducts(data);
      } catch (err) {
        console.error("Error fetching products:", err);
        setError("Failed to fetch products. Please try again.");
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) {
    return (
      <div>
        <Header />
        <div className="container mx-auto p-4 text-center">
          <p>Loading products...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <Header />
        <div className="container mx-auto p-4 text-red-500 text-center">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6">Product Catalog</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Catalog;
