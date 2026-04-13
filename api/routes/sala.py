from fastapi import APIRouter
from schemas.sala import SalaCreate

router = APIRouter(prefix="/salas", tags=["Salas"])


@router.post("")
def criar_sala_route(data: SalaCreate):
    pass


@router.get("")
def listar_salas_route():
    pass