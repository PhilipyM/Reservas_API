class Reserva:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        sala_id: int,
        data: str,
        hora_inicio: str,
        hora_fim: str,
        status: str = "active"
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.status = status

    def cancelar(self, reserva_id):
        if self.status == "active":
            pass#to do

        

    def finalizar(self, hora_atual: str):
        pass

    def duracao_em_horas(self) -> float:
        pass

    def conflita_com(self, outra_reserva) -> bool:
        pass