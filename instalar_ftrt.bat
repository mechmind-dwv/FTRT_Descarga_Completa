@echo off
echo 🔧 Instalador Automático FTRT para Windows
echo ========================================

:: Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no encontrado. Por favor instala Python 3.8 o superior.
    pause
    exit /b 1
)

:: Crear entorno virtual
echo 🐍 Creando entorno virtual...
python -m venv ftrt_env
call ftrt_env\Scripts\activate.bat

:: Instalar dependencias
echo 📦 Instalando dependencias...
pip install numpy pandas matplotlib scipy

:: Verificar instalación
echo ✅ Verificando instalación...
cd codigo_fuente
python -c "from ftrt_core import FTRTCalculator; print('🎉 Sistema FTRT instalado correctamente!')"

echo.
echo 🚀 ¡Instalación completada!
echo 📚 Documentación en: documentacion/
echo 💻 Ejemplos en: ejemplos/
echo 🎮 Ejecutar: ftrt_env\Scripts\activate && python sistema_ftrt.py --interactivo
pause
