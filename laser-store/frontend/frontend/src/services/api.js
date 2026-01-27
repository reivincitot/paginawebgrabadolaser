import axios from 'axios';

// Configurar axios
const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json'
    },
});

// Interceptor para agregar token
api.interceptors.request.use(
    (config) => {
      const token = localstorage.getItem('token');
      if (token) {
          config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
);

// Interceptor para manejar respuestas
api.interceptors.response.use(
    (response) => response.data,
    (error) => {
        if (error.response?.status === 401) {
            localStorage.removeItem('token');
            window.location.href = '/login';
        }
        return Promise.reject(error.response?.data || error.message);
    }
);

// Servicios específicos
export const productServices = {
    getAll: () => api.get('/products'),
    getById: (id) => api.get('/products/${id}'),
    create: (data) => api.post('/products', data),
    update: (id, data) => api.put('/products/${id}', data),
    delete: (id) => api.delete('/products/${id}'),
};

export const orderServices = {
    login: (credentials) => api.post('/auth/login', credentials),
    getUserOrders: () => api.get('/orders/users'),
    getById: (id) => api.get('/orders/${id}'),
};

export const authServices = {
    login: (credentials) => api.post('/auth/login', credentials),
    register: (data) => api.post('/auth/register', data),
    logout: () => api.post('/auth/logout'),
    getProfile: () => api.get('/auth/profile')
};

export default api;
