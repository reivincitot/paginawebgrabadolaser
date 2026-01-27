#!/bin/bash
cd /d/paginawebgrabadolaser/laser-store

echo "🔍 Verificando Docker..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado o no está en el PATH"
    exit 1
fi

echo "🚀 Iniciando Laser Store en modo desarrollo..."
echo "⏳ Esto puede tomar unos minutos..."

# Función para verificar si un contenedor está saludable
check_container() {
    local container_name=$1
    local max_attempts=30
    local attempt=1
    
    echo "⏳ Esperando a $container_name..."
    
    while [ $attempt -le $max_attempts ]; do
        if docker ps --filter "name=$container_name" --format "{{.Status}}" | grep -q "Up"; then
            echo "✅ $container_name está listo"
            return 0
        fi
        sleep 2
        attempt=$((attempt + 1))
    done
    
    echo "❌ $container_name no se pudo iniciar después de $((max_attempts * 2)) segundos"
    return 1
}

# 1. Iniciar bases de datos
echo "🐘 Iniciando PostgreSQL y MongoDB..."
docker compose up -d db_products mongo

# Verificar bases de datos
check_container "db_products" || exit 1
check_container "mongo" || exit 1

# 2. Iniciar microservicios
echo "🐍 Iniciando microservicios Django..."
docker compose up -d product_service orders_service client_service

# Verificar microservicios
check_container "product_service" || exit 1
check_container "orders_service" || exit 1
check_container "client_service" || exit 1

# 3. Iniciar frontend
echo "⚛️  Iniciando frontend React..."
docker compose up -d frontend

check_container "frontend" || exit 1

echo ""
echo "🎉 ¡Laser Store está listo!"
echo ""
echo "🌐 URLs de acceso:"
echo "   - Frontend:       http://localhost:3000"
echo "   - Product API:    http://localhost:8002"
echo "   - Orders API:     http://localhost:8003"
echo "   - Clients API:    http://localhost:8004"
echo "   - PostgreSQL:     localhost:54322"
echo "   - MongoDB:        localhost:27017"
echo ""
echo "🔧 Comandos útiles:"
echo "   ./stop-dev.sh           # Detener todos los servicios"
echo "   docker compose logs     # Ver logs"
echo "   docker compose ps       # Ver estado"
echo "   docker compose restart  # Reiniciar servicios"
echo ""
echo "📝 Para ver logs en tiempo real: docker compose logs -f"
