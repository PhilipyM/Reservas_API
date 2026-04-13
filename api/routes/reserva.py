from fastapi import APIRouter
from schemas.reserva import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("")
def criar_reserva_route(data: ReservaCreate):
    pass


@router.get("")
def listar_reservas_route():
    pass


@router.get("/usuario/{usuario_id}")
def listar_reservas_usuario_route(usuario_id: int):
    pass


@router.get("/{reserva_id}")
def buscar_reserva_route(reserva_id: int):
    pass


@router.put("/{reserva_id}/cancelar")
def cancelar_reserva_route(reserva_id: int):
    pass


@router.put("/{reserva_id}/finalizar")
def finalizar_reserva_route(reserva_id: int, hora_atual: str):
    pass