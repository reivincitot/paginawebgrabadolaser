import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true,
    proxy: {
      '/api/products': {
        target: 'http://product_service:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/products/, '')
      },
      '/api/orders': {
        target: 'http://orders_service:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/orders/, '')
      },
      '/api/clients': {
        target: 'http://client_service:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/clients/, '')
      }
    }
  }
})
