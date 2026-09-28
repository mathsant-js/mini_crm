from datetime import date

def model_lead(nome: str, email: str, status: str) -> dict:
    """Modela o lead com a formato correto"""
    
    return {
        "name": nome,
        "email": email,
        "status": status,
        "created": date.today().isoformat()
    }