from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db


def criar_usuario(nome: str, email: str):
    if not nome and not email:
        raise ValueError("O usuário deve conter nome e email.")
    
    if email in db.usuario:
        raise ValueError("Não pode haver duas contas com o mesmo email.")

    usuario = Usuario(nome = nome, email = email)
    db.usuarios[db.next_usuario_id] = usuario
    db.next_usuario_id += 1
    return usuario

def listar_usuarios():
    return db.usuarios.get()


def criar_sala(nome: str, capacidade: int, bloco: str):
    if not nome:
        raise ValueError("A sala deve ter um nome.")

    if capacidade <= 0:
        raise ValueError("A capacidade deve ser maior que 0.")

    sala = Sala(nome = nome, capacidade = capacidade, bloco = bloco)
    db.salas[db.next_sala_id] = sala
    db.next_sala_id += 1
    return sala

def listar_salas():
    return db.sala.get()

def criar_reserva(usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
    #Não pode cadastrar sala no passdo (to do)

    if hora_fim < hora_inicio:
        raise ValueError("A hora final deve ser superior a hora inicial.")

    #A mesma sala não pode ter reservas com sobreposição de horário na mesma data

    #O mesmo usuário não pode ter duas reservas com sobreposição de horário na mesma data

    #Um usuário pode ter no máximo 2 reservas ativas por dia

    if hora_inicio - hora_fim > 2:
        raise ValueError("Uma sala não pode ser alugada por mais de 2:00 (duas horas).")

    reserva = Reserva(
        usuario_id = usuario_id,
        sala_id = sala_id,
        data = data,
        hora_inicio = hora_inicio,
        hora_fim = hora_fim
        )
    db.reservas[db.next_reserva_id] = reserva
    db.next_reserva_id += 1
    return reserva

def listar_reservas():
    return db.reservas.get()

def listar_reservas_usuario(usuario_id: int):
    return db.reservas.get(usuario_id)

def buscar_reserva(reserva_id: int):
    return db.reservas.get(reserva_id)

def cancelar_reserva(reserva_id: int):
    Reserva.cancelar(reserva_id)

def finalizar_reserva(reserva_id: int, hora_atual: str):
    #to do
    pass