import React, { useState } from 'react';
import axios from 'axios';

const CreateOrder = ({ carItems }) => {
  const [order, setOrder] = useState(null);

  const handleCreateOrder = async () => {
    try {
      const response = await axios.post('http://localhost:8002/api/orders/', {
        items: carItems.map(
          item => ({
            product_id: item.id,
            quantity: item.quantity,
            price: item.price
          }))
      }); 
      setOrder(response.data);
    } catch (error) {
      console.error('Error creando orden:', error);
    }
  };
  return (
    <div>
      <button onClick={handleCreateOrder}>CreateOrder</button>
      {order && <div>Order #{order.id} creation successfully!</div>}
    </div>
  );
};