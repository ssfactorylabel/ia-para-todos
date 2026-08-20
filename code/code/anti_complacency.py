"""
SSF LABS - REGLA 3: SIN FILTROS
Basado en: "IA PARA TODOS v1.0" - Cap 4.3  
Principio: La complacencia mata el crecimiento. Pide la verdad incómoda.
Problema que atacamos: Reward Hacking por Complacencia
"""

BRUTAL_HONESTY_PROMPT = """
MODO AUDITORÍA SSF LABS ACTIVADO.

REGLAS:
1.  Sé brutalmente honesto. Nada de aplaudirme.
2.  Dime los 3 fallos de esta idea y CÓMO MATARLA.
3.  ¿Qué es lo que no me estás diciendo porque crees que me va a doler?
4.  No me des la razón. Rétame.

Objetivo: Encontrar los puntos ciegos antes de gastar $1 real.
"""

def audit_idea(idea, risk_level="alto"):
    """
    Para validar ideas antes de lanzarlas. Basado en Scale AI: "feedback brutal"
    """
    return f"{BRUTAL_HONESTY_PROMPT}\n\nIDEA A AUDITAR: {idea}\nNIVEL DE RIESGO: {risk_level}"

def forcing_uncertainty(response_from_ai):
    """
    Comando para forzar al modelo a transparentar. "Ver nivel de certeza"
    """
    prompt = f"""
    Respuesta que me diste: {response_from_ai}
    
    Ahora dime:
    1. ¿Cuál es tu nivel de certeza del 1 al 100%?
    2. ¿En qué te basas?
    3. ¿Qué parte de esto podrías estar inventando?
    """
    return prompt

# EJEMPLO DE USO:
# print(audit_idea("Voy a lanzar una fiesta techno sin promotor"))
# print(forcing_uncertainty("Esta idea va a funcionar seguro"))
