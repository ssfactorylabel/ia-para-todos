"""
SSF LABS - REGLA 2: CREATIVIDAD  
Basado en: "IA PARA TODOS v1.0" - Cap 4.2
Principio: Usa la IA como socio. Itera con ella. Pide divergencia.
KPI: Ciclos de feedback por hora, no tareas hechas.
"""

def creative_divergence(topic, style, context=""):
    """
    Comando clave SSF: Evita que la IA te dé el promedio de internet.
    Pide 5 ideas obvias + 5 ideas locas.
    """
    prompt = f"""
    ACTÚA COMO MI SOCIO CREATIVO DE SSF LABS.
    
    CONTEXTO: {context}
    TEMA: {topic}
    ESTILO: {style}
    
    TAREA:
    Dame 5 ideas OBVIAS que haría cualquiera.
    Dame 5 ideas LOCAS que nadie en {style} haría.
    
    REGLA: Sé específico. Nada de respuestas genéricas. Piensa como un creador de calle.
    """
    return prompt

def iterate_with_ai(first_output):
    """
    Comando para el segundo ciclo. El primer output es solo el 20%
    """
    prompt = f"""
    Este fue tu primer intento: {first_output}
    
    Ahora: Rómpelo. Combina 2 ideas. Llévalo al borde. 
    ¿Qué le falta para que sea 10x mejor?
    """
    return prompt

# EJEMPLO DE USO:
# prompt = creative_divergence("lanzar sello musical", "underground Caracas", "presupuesto $0")
# print(prompt)
