#!/usr/bin/env python3
"""
SISTEMA FTRT PRINCIPAL - DEFINITIVAMENTE CORREGIDO
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

import sys
import argparse
from datetime import datetime

def verificar_sistema():
    """Verifica que el sistema esté funcionando correctamente"""
    print("🔍 VERIFICANDO SISTEMA FTRT...")
    
    try:
        # Verificar módulos principales
        from ftrt_core import FTRTCalculator, calcular_ftrt_rapido
        
        print("✅ Módulos cargados correctamente")
        
        # Verificar cálculo básico con función rápida (solo strings)
        resultado_2024 = calcular_ftrt_rapido("2024-05-10")
        print(f"✅ Cálculo FTRT 2024-05-10: {resultado_2024['ftrt_normalizada']:.3f}")
        
        # Verificar evento histórico
        resultado_2003 = calcular_ftrt_rapido("2003-10-29")
        print(f"✅ Cálculo FTRT 2003-10-29: {resultado_2003['ftrt_normalizada']:.3f}")
        
        # Verificar fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        resultado_actual = calcular_ftrt_rapido(fecha_actual)
        print(f"✅ Cálculo FTRT actual ({fecha_actual}): {resultado_actual['ftrt_normalizada']:.3f}")
        
        print("🎉 ¡Sistema FTRT verificado correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en verificación: {e}")
        import traceback
        traceback.print_exc()
        return False

def modo_prediccion(dias=30):
    """Ejecuta modo predicción automática"""
    print(f"🔮 MODO PREDICCIÓN - Próximos {dias} días")
    
    try:
        from ftrt_core import FTRTCalculator
        calculadora = FTRTCalculator()
        
        fecha_inicio = datetime.now().strftime('%Y-%m-%d')  # Convertir a string
        predicciones = calculadora.predecir_ftrt_rango(fecha_inicio, dias=dias)
        
        # Mostrar días de alto riesgo
        alto_riesgo = predicciones[predicciones['ftrt_normalizada'] > 1.8]
        print(f"📅 Días de alto riesgo detectados: {len(alto_riesgo)}")
        
        if len(alto_riesgo) > 0:
            print("🚨 ALERTA - Períodos de alto riesgo:")
            for _, fila in alto_riesgo.iterrows():
                print(f"   • {fila['fecha']}: FTRT={fila['ftrt_normalizada']:.2f} ({fila['nivel_riesgo']} {fila['color_alerta']})")
        else:
            print("   ✅ No se detectaron días de alto riesgo en el período")
            
    except Exception as e:
        print(f"❌ Error en predicción: {e}")
        import traceback
        traceback.print_exc()

def mostrar_estado():
    """Muestra estado actual del sistema"""
    print("🌌 ESTADO DEL SISTEMA FTRT")
    print("==========================")
    
    try:
        from ftrt_core import calcular_ftrt_rapido
        from datetime import datetime
        
        # Fecha actual (como string)
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        resultado_actual = calcular_ftrt_rapido(fecha_actual)
        
        print(f"📅 Fecha actual: {fecha_actual}")
        print(f"📊 FTRT actual: {resultado_actual['ftrt_normalizada']:.3f}")
        print(f"🚨 Nivel de alerta: {resultado_actual['nivel_riesgo']} {resultado_actual['color_alerta']}")
        
        # Interpretación del nivel
        nivel = resultado_actual['nivel_riesgo']
        if nivel == 'EXTREMO':
            print("💀 RECOMENDACIÓN: Monitoreo intensivo - posible evento mayor")
        elif nivel == 'CRÍTICO':
            print("⚠️  RECOMENDACIÓN: Alertas activadas - alta probabilidad de tormenta")
        elif nivel == 'ELEVADO':
            print("🔶 RECOMENDACIÓN: Preparación - posible actividad solar")
        elif nivel == 'MODERADO':
            print("🔸 RECOMENDACIÓN: Vigilancia - actividad normal-alta")
        else:
            print("✅ RECOMENDACIÓN: Situación normal")
            
    except Exception as e:
        print(f"❌ Error al obtener estado: {e}")
        import traceback
        traceback.print_exc()

def demo_rapida():
    """Demo rápida del sistema"""
    print("🚀 DEMO RÁPIDA FTRT")
    print("===================")
    
    try:
        from ftrt_core import calcular_ftrt_rapido
        
        eventos = [
            ("2003-10-29", "Tormenta Halloween"),
            ("2024-05-10", "Tormenta Mayo"),
            (datetime.now().strftime('%Y-%m-%d'), "Fecha actual")
        ]
        
        for fecha, descripcion in eventos:
            resultado = calcular_ftrt_rapido(fecha)
            print(f"📅 {descripcion} ({fecha}):")
            print(f"   FTRT: {resultado['ftrt_normalizada']:.3f}")
            print(f"   Nivel: {resultado['nivel_riesgo']} {resultado['color_alerta']}")
            print()
            
    except Exception as e:
        print(f"❌ Error en demo: {e}")

def main():
    """Función principal del sistema"""
    parser = argparse.ArgumentParser(
        description='🌌 Sistema de Predicción FTRT - Fuerza de Marea Relativa Total',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Ejemplos de uso:
  python sistema_ftrt.py --verificar    # Verifica el sistema
  python sistema_ftrt.py --estado       # Muestra estado actual
  python sistema_ftrt.py --prediccion 7 # Predice próximos 7 días
  python sistema_ftrt.py --demo         # Demo rápida
  python sistema_ftrt.py --interactivo  # Modo interactivo completo
        '''
    )
    
    parser.add_argument('--verificar', action='store_true', help='Verificar sistema completo')
    parser.add_argument('--prediccion', type=int, metavar='DIAS', help='Predicción para X días')
    parser.add_argument('--interactivo', action='store_true', help='Modo interactivo completo')
    parser.add_argument('--estado', action='store_true', help='Estado actual del sistema')
    parser.add_argument('--demo', action='store_true', help='Demo rápida del sistema')
    
    args = parser.parse_args()
    
    if args.verificar:
        verificar_sistema()
    elif args.prediccion:
        modo_prediccion(args.prediccion)
    elif args.estado:
        mostrar_estado()
    elif args.demo:
        demo_rapida()
    elif args.interactivo:
        try:
            from interactive_ftrt import main as interactive_main
            interactive_main()
        except ImportError:
            print("❌ Modo interactivo no disponible")
            print("💡 Ejecuta: python interactive_ftrt.py directamente")
    else:
        # Modo por defecto: demo rápida
        print("🌌 SISTEMA FTRT - BIENVENIDO")
        print("=============================")
        print("Ejecuta con --help para ver todas las opciones")
        print()
        demo_rapida()

if __name__ == "__main__":
    main()
