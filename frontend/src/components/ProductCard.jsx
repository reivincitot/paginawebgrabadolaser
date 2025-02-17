import React from 'react';
import { Link } from 'react-router-dom';

const ProductCard = ({ product }) => {
  return (
    <div className="bg-white shadow-md rounded overflow-hidden">
      <img 
        src={product.images || '/placeholder.png'} 
        alt={product.name} 
        className="w-full h-40 object-cover" 
      />
      <div className="p-4">
        <h2 className="text-xl font-bold">{product.name}</h2>
        <p className="text-gray-700">${product.price.toFixed(2)}</p>
        <div className="mt-4 flex justify-between">
          <Link 
            to={`/product/${product.id}`} 
            className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 transition-colors"
          >
            Details
          </Link>
          <div className="flex space-x-2">
            <button className="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600">
              Cart
            </button>
            <button className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
              Pay Now
            </button>
          </div>
        </div>
        <div className="mt-2 flex justify-between">
          <button className="text-red-500 hover:text-red-600">❤️</button>
          <button className="text-gray-500 hover:text-gray-600">🔗</button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
