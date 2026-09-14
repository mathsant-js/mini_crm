from datetime import date

def model_lead(nome: str, email: str, status: str) -> dict:
    return {
        "name": nome,
        "email": email,
        "status": status,
        "created": date.today().isoformat()
    }