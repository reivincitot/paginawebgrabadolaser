import {createSlice} from '@reduxjs/toolkit';


const loadCartFormStorage = () => {
  const cart = localStorage.getItem('cart');
  return cart ? JSON.parse(cart) : [];
};

const cartSlice = createSlice({
  name:'cart',
  initialState: loadCartFormStorage(),
  reducers: {
    addToCart: (state, action) => {
      const existingItem = state.find(item => item.id === action.payload.id);
      
      if (existingItem){
        existingItem.quantity +=1;
      } else {
      state.push({
        ...action.payload,
      });
    }

    localStorage.setItem('cart', JSON.stringify(state));
    },
    removeFromCart: (state, action) => {
      const newState = state.filter(item => item.id !== action.payload);
      localStorage.setItem('cart', JSON.stringify(newState));
      return newState;
    },
  },
});

export const {addToCart} = cartSlice.actions;
export default cartSlice.reducer;
