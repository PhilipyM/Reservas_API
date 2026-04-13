from fastapi import APIRouter
from schemas.usuario import UsuarioCreate

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("")
def criar_usuario_route(data: UsuarioCreate):
    pass


@router.get("")
def listar_usuarios_route():
    pass