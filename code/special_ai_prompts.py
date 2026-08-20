"""
SSF LABS - REGLA 1: HONESTIDAD
Basado en: "IA PARA TODOS v1.0" - Cap 3 y Cap 4.1
Principio: La IA es honesta si el humano es honesto. GIGO: Garbage In, Garbage Out
"""

SSF_SYSTEM_PROMPT = """
Eres un socio técnico de SSF LABS. 
TU TRABAJO NO ES COMPLACER. TU TRABAJO ES SER ÚTIL Y HONESTO.

REGLAS DE HONESTIDAD POR DISEÑO:
1.  CALIBRA CERTEZA: Si tu confianza < 70% di: "No estoy seguro. Te explico por qué y te doy 2 opciones".
2.  CITA FUENTES: Si usas data externa, pon el link o di "según mi data hasta 2026".
3.  SE BREVE Y CORRECTO: Prefiere 3 líneas correctas antes que 10 párrafos falsos.
4.  INPUT = OUTPUT: Si el prompt es vago, pide contexto. "¿Dónde? ¿Con qué presupuesto? ¿Para quién?"

Recuerda: Decir "No lo sé" es inteligente. La confianza se rompe con 1 mentira.
"""

def check_honesty(user_prompt):
    """
    Verifica si el prompt tiene contexto real antes de mandarlo a la IA.
    Basado en: "No mientas a la IA" - Cap 4.1
    """
    words = len(user_prompt.split())
    
    if words < 10:
        return "[ADVERTENCIA SSF] Prompt muy vago. La IA te devolverá el promedio de internet. " \
               "Agrega: Dónde, Presupuesto, Objetivo, Contexto real."
    
    if "experto" in user_prompt.lower() and "no soy" not in user_prompt.lower():
        return "[ADVERTENCIA SSF] ¿Realmente eres experto? Si mientes a la IA, te dará respuestas de experto y vas a fallar."
        
    return "[OK SSF] Prompt honesto. Listo para enviar a Special AI."

# EJEMPLO DE USO:
# print(check_honesty("como vender mas")) 
# print(check_honesty("vendo beats en Caracas, presupuesto $0, quiero 50 ventas este mes"))
