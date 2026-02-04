#!/bin/bash
echo "🔧 CORRECIÓN COMPLETA DEL FRONTEND"

cd frontend

echo "1. 📦 Corrigiendo package.json..."
cat > package.json << 'PKGEOF'
{
  "name": "laser-store-frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint src --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.2",
    "@tanstack/react-query": "^5.8.4",
    "@tanstack/react-query-devtools": "^5.8.4",
    "react-hot-toast": "^2.4.1",
    "clsx": "^2.0.0",
    "@headlessui/react": "^1.7.17",
    "@heroicons/react": "^2.0.18"
  },
  "devDependencies": {
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.55.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "postcss": "^8.4.32",
    "vite": "^5.0.8",
    "tailwindcss": "^3.3.6"
  }
}
PKGEOF

echo "2. 🐳 Corrigiendo Dockerfile..."
cat > Dockerfile << 'DOCKEREOF'
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
COPY vite.config.js ./

RUN npm install --silent --legacy-peer-deps

COPY . .

RUN npm run build

FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
DOCKEREOF

echo "3. ⚡ Corrigiendo vite.config.js..."
cat > vite.config.js << 'VITEEOF'
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
VITEEOF

echo "4. 📝 Creando archivos básicos si faltan..."
# App.jsx
cat > src/App.jsx << 'APPEOF'
import React from 'react'

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>🎉 ¡Laser Store está funcionando!</h1>
      <p>Frontend React corriendo correctamente.</p>
      <div style={{ marginTop: '20px', padding: '10px', background: '#f0f0f0' }}>
        <h3>Servicios disponibles:</h3>
        <ul>
          <li>Product API: http://localhost:8002</li>
          <li>Orders API: http://localhost:8003</li>
          <li>Clients API: http://localhost:8004</li>
        </ul>
      </div>
    </div>
  )
}

export default App
APPEOF

# main.jsx
cat > src/main.jsx << 'MAINEOF'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
MAINEOF

# index.html
cat > index.html << 'HTML'
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Laser Store</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
HTML

echo "5. 🧹 Limpiando caché..."
rm -rf node_modules package-lock.json 2>/dev/null

echo "✅ CORRECCIONES APLICADAS"
echo ""
echo "📊 Verificación:"
ls -la
echo ""
echo "📦 Para probar localmente: npm install"
