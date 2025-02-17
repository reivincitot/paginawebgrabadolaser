import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import axiosInstance from '../services/AxiosInstance';
import Footer from '../components/Footer';

const Cart = () => {
	const [cartItems, setCartItems] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState('');

	// Función para obtener los ítems del carrito desde el backend
	const fetchCartItems = async () => {
		try {
			const response = await axiosInstance.get('cart/');
			setCartItems(response.data);
			setLoading(false);
		} catch (err) {
			console.error("Error fetching cart items:", err);
			setError("Failed to load cart items.");
			setLoading(false);
		}
	};

	useEffect(() => {
		fetchCartItems();
	}, []);

	// Función para actualizar la cantidad de un ítem
	const updateQuantity = async (id, newQuantity) => {
		try {
			const response = await axiosInstance.put(`cart/item/${id}/`, { quantity: newQuantity });
			// Actualiza el estado local con la cantidad actualizada
			setCartItems(cartItems.map(item => item.id === id ? { ...item, quantity: response.data.quantity } : item));
		} catch (err) {
			console.error("Error updating quantity:", err);
			setError("Failed to update quantity.");
		}
	};

	// Función para eliminar un ítem del carrito
	const removeItem = async (id) => {
		try {
			await axiosInstance.delete(`cart/item/${id}/`);
			setCartItems(cartItems.filter(item => item.id !== id));
		} catch (err) {
			console.error("Error removing item:", err);
			setError("Failed to remove item.");
		}
	};

	// Calcula el total del carrito
	const totalPrice = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);

	if (loading) {
		return (
			<div>
				<Header />
				<div className="container mx-auto p-4">
					<p>Loading cart...</p>
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
				<h1 className="text-3xl font-bold mb-6">Your Cart</h1>
				{cartItems.length === 0 ? (
					<p>Your cart is empty.</p>
				) : (
					<div className="space-y-4">
						{cartItems.map(item => (
							<div key={item.id} className="flex items-center bg-white shadow rounded p-4">
								<img
									src={item.image || '/placeholder.png'}
									alt={item.name}
									className="w-20 h-20 object-cover rounded mr-4"
								/>
								<div className="flex-1">
									<h2 className="text-xl font-semibold">{item.name}</h2>
									<p className="text-gray-700">${item.price.toFixed(2)}</p>
									<div className="mt-2 flex items-center">
										<label className="mr-2">Qty:</label>
										<input
											type="number"
											value={item.quantity}
											min="1"
											className="w-16 border rounded p-1"
											onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
										/>
									</div>
								</div>
								<button
									onClick={() => removeItem(item.id)}
									className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
								>
									Remove
								</button>
							</div>
						))}
						<div className="text-right mt-6">
							<h2 className="text-2xl font-bold">Total: ${totalPrice.toFixed(2)}</h2>
							<button className="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600 mt-4">
								Proceed to Checkout
							</button>
						</div>
					</div>
				)}
			</div>
			<Footer />
		</div>
	);
};

export default Cart;
