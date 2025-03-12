import React, { useEffect, useState, UseState } from 'react';
import { getProducts } from '../api/products';
import { addToCart } from '../store/cartSlice';
import { useDispatch } from 'react-redux';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const dispatch = useDispatch();

  useEffect(() => {
    getProducts().then(response => setProducts(response.data));
  },[]);

  return (
    <div className='gri grid-cols3 gap-4'>
      {products.map(product => (
        <div key={product.id} className='border p-4'>
        <img src={product.image} alt={product.name} className='w-full h-48 object-cover'/>
        <h3 className='text-xl'>{product.name}</h3>
        <p className='text-gray-600'>${product.price}</p>
        <button
        onClick={() => dispatch(addToCart(product))}
        className='bg-blue-500 text-white px-4 py-2 mt-2'>Agregar al carrito</button>
        </div>
      ))}
    </div>
  );
};

export default ProductList;