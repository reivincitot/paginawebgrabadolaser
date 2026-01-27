import {signal, computed } from '@preact/signal-react';

// Estado global con Signals
export const cart = signal([]);
export const user = signal(null);
export const products = signal([]);
export const isLoading = signal(false);

// Computed values
export const cartToral = computed(() =>
    cart.value.reduce((total, item) => total + (item.price * item.quantity), 0)
);

export const cartCount = computed(() =>
    cart.value.reduce((count, item) => count + item.quantity, 0)
);

export const addToCart = (product, quantity =1) => {
    const existing = cart.value.find(item => item.id === product.id);
    if (existing) {
        existing.quantity += quantity;
        cart.value = [...cart.value];
    } else {
        cart.value = [...cart.value, { ...product, quantity }];
    }
};

export const updateQuantity = (productId, quantity) => {
    const item = cart.value.find(item => item.id === productId);
    if (item) {
        item.quantity = quantity;
        cart.value = [...cart.value];
    }
};

export const clearCart = () => {
    cart.value = [];
};