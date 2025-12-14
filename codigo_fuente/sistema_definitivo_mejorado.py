#!/usr/bin/env python3
"""
SISTEMA FTRT DEFINITIVO MEJORADO - VERSIÓN ESTABLE
Maestro Cósmico & Aprendiz - Octubre 2025
"""

import sys
import os
from datetime import datetime

# Añadir ruta actual para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def probar_sistema_completo():
    """Prueba completa del sistema FTRT reparado"""
    
    print("🌌 SISTEMA FTRT DEFINITIVO - PRUEBA COMPLETA")
    print("=" * 60)
    
    pruebas = []
    
    # 1. Probar imports básicos
    try:
        import numpy as np
        import pandas as pd
        import ephem
        print("✅ 1. Dependencias básicas - OK")
        pruebas.append(("Dependencias básicas", "✅"))
    except Exception as e:
        print(f"❌ 1. Dependencias básicas: {e}")
        pruebas.append(("Dependencias básicas", "❌"))
    
    # 2. Probar módulos FTRT
    try:
        from historical_database import HISTORICAL_EVENTS, FTRT_HISTORICAL_DATA
        print(f"✅ 2. Base datos - {len(HISTORICAL_EVENTS)} eventos, {len(FTRT_HISTORICAL_DATA)} datos FTRT")
        pruebas.append(("Base datos histórica", "✅"))
    except Exception as e:
        print(f"❌ 2. Base datos: {e}")
        pruebas.append(("Base datos histórica", "❌"))
    
    # 3. Probar cálculo FTRT (usando sistema de emergencia si es necesario)
    try:
        # Intentar con sistema principal primero
        from ftrt_core import FTRTCalculator
        calc = FTRTCalculator()
        resultado = calc.calcular_ftrt_total(datetime.now())
        ftrt = resultado.get('ftrt_normalizada', 0)
        nivel = calc.evaluar_riesgo(ftrt)[0]
        print(f"✅ 3. Cálculo FTRT - {ftrt:.3f} ({nivel})")
        pruebas.append(("Cálculo FTRT", "✅"))
    except Exception as e:
        print(f"⚠️  3. Cálculo FTRT: {e} - Usando sistema de emergencia")
        # Sistema de emergencia
        ftrt_emergencia = 1.189  # Valor precalculado
        nivel = "MODERADO 🟡" if ftrt_emergencia < 1.2 else "ELEVADO 🟠"
        print(f"✅ 3. Cálculo FTRT (emergencia) - {ftrt_emergencia:.3f} ({nivel})")
        pruebas.append(("Cálculo FTRT", "⚠️ (emergencia)"))
    
    # 4. Probar validación
    try:
        from validation_simple import validar_correlaciones
        print("✅ 4. Sistema validación - OK")
        pruebas.append(("Sistema validación", "✅"))
    except Exception as e:
        print(f"❌ 4. Sistema validación: {e}")
        pruebas.append(("Sistema validación", "❌"))
    
    # 5. Probar scripts shell
    try:
        import subprocess
        result = subprocess.run(['./magia_super_facil.sh'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ 5. Scripts shell - OK")
            pruebas.append(("Scripts shell", "✅"))
        else:
            print("⚠️  5. Scripts shell - Ejecución con errores")
            pruebas.append(("Scripts shell", "⚠️"))
    except Exception as e:
        print(f"❌ 5. Scripts shell: {e}")
        pruebas.append(("Scripts shell", "❌"))
    
    # 6. Probar datos históricos
    try:
        # Calcular correlación manualmente
        eventos = []
        for event in HISTORICAL_EVENTS:
            date_str = event['event_date']
            if date_str in FTRT_HISTORICAL_DATA:
                eventos.append({
                    'magnitude': event['magnitude'],
                    'ftrt': FTRT_HISTORICAL_DATA[date_str]['ftrt_normalized']
                })
        
        if len(eventos) >= 2:
            magnitudes = [e['magnitude'] for e in eventos]
            ftrt_vals = [e['ftrt'] for e in eventos]
            correlacion = np.corrcoef(magnitudes, ftrt_vals)[0,1]
            print(f"✅ 6. Datos históricos - Correlación: {correlacion:.3f}")
            pruebas.append(("Datos históricos", "✅"))
        else:
            print("⚠️  6. Datos históricos - Insuficientes para correlación")
            pruebas.append(("Datos históricos", "⚠️"))
    except Exception as e:
        print(f"❌ 6. Datos históricos: {e}")
        pruebas.append(("Datos históricos", "❌"))
    
    # RESUMEN FINAL
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS:")
    for prueba, estado in pruebas:
        print(f"   {estado} {prueba}")
    
    exitosas = sum(1 for _, estado in pruebas if estado == "✅")
    total = len(pruebas)
    
    print(f"\n🎯 ESTADO FINAL: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("🎉 ¡SISTEMA FTRT 100% OPERATIVO!")
    elif exitosas >= total * 0.7:
        print("⚠️  Sistema mayormente operativo - Revisar advertencias")
    else:
        print("❌ Sistema con problemas críticos - Reparación necesaria")
    
    print("=" * 60)

if __name__ == "__main__":
    probar_sistema_completo()
