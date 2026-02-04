#!/bin/bash
cd /d/paginawebgrabadolaser/laser-store

echo "🔧 Corrigiendo estructura..."

# 1. DockerFile → Dockerfile
[ -f "frontend/DockerFile" ] && mv frontend/DockerFile frontend/Dockerfile

# 2. Eliminar estructura duplicada
[ -d "frontend/frontend" ] && mv frontend/frontend/* frontend/ 2>/dev/null; rmdir frontend/frontend/ 2>/dev/null

echo "✅ Correcciones aplicadas"
