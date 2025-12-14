#!/bin/bash

echo "🔧 Instalador Automático FTRT"
echo "============================="

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no encontrado. Por favor instala Python 3.8 o superior."
    exit 1
fi

# Crear entorno virtual
echo "🐍 Creando entorno virtual..."
python3 -m venv ftrt_env
source ftrt_env/bin/activate

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install numpy pandas matplotlib scipy

# Verificar instalación
echo "✅ Verificando instalación..."
cd codigo_fuente
python -c "from ftrt_core import FTRTCalculator; print('🎉 Sistema FTRT instalado correctamente!')"

echo ""
echo "🚀 ¡Instalación completada!"
echo "📚 Documentación en: documentacion/"
echo "💻 Ejemplos en: ejemplos/"
echo "🎮 Ejecutar: source ftrt_env/bin/activate && python sistema_ftrt.py --interactivo"
