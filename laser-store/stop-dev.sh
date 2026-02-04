#!/bin/bash
cd /d/paginawebgrabadolaser/laser-store
echo "🛑 Deteniendo servicios Laser Store..."
docker compose down
echo "✅ Servicios detenidos"
echo "💡 Para iniciar de nuevo: ./start-dev.sh"
