from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "¡Hola desde FastAPI en Docker!"}

@router.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}
