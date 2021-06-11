from partida import *
from jugador import *
from carta import *
from crear_segundojugador import *
import random

def mezclar_cartas(carta):
    list_temporal = []
    for x in range(len(carta)):
        list_temporal.append(carta[x].id)
    for x in range(len(carta)):
        cont_ale = random.randint(0,len(carta)-1)
        temporal = list_temporal[x]
        list_temporal[x] = list_temporal[cont_ale]
        list_temporal[cont_ale] = temporal
    return list_temporal


print("Iniciando la partida")
carta = []
for x in range(52):
    cont = x//13
    carta.append(Carta(x+1-cont*13, cont, x))
cartas_mez = mezclar_cartas(carta)
print(cartas_mez)
servidor = Jugador()
servidor.iniciarSesion()
cliente = Jugador()
cliente.nombre_de_usuario = crear_Segundojugador()
partida_actual = Partida()
if(partida_actual.primerJugador == 0):
    print("Tu eres el primer jugador")
    servidor.tipo_de_turno = 1
    cliente.tipo_de_turno = 0
else:
    print("El primer jugador es ", cliente.nombre_de_usuario)
    servidor.tipo_de_turno = 0
    cliente.tipo_de_turno = 1

print("=================================================================")
while(servidor.estado or cliente.estado):
    print("Es el turno numero: ", partida_actual.n_turno)
    indice = partida_actual.n_turno + 1
    if(servidor.estado == True and (partida_actual.n_turno%2) == servidor.tipo_de_turno):
        print("Es el turno de ", servidor.nombre_de_usuario)
        if(partida_actual.n_turno <= 2):
            indice = partida_actual.primerJugador + partida_actual.n_turno - 1
            servidor.robarCarta(carta[cartas_mez[indice]].numero, carta[cartas_mez[indice]].valor, carta[cartas_mez[indice]].tipo)
            indice = partida_actual.primerJugador + partida_actual.n_turno
        servidor.robarCarta(carta[cartas_mez[indice]].numero, carta[cartas_mez[indice]].valor, carta[cartas_mez[indice]].tipo)
        print("El puntaje del usuario ", servidor.nombre_de_usuario, " es: ", servidor.puntos)
        servidor.seguirJugando()
    elif(cliente.estado == True and (partida_actual.n_turno%2) == cliente.tipo_de_turno):
        print("Es el turno de ", cliente.nombre_de_usuario)
        if(partida_actual.n_turno <= 2):
            indice = - partida_actual.primerJugador + partida_actual.n_turno
            cliente.robarCarta(carta[cartas_mez[indice]].numero, carta[cartas_mez[indice]].valor, carta[cartas_mez[indice]].tipo)
            indice = 1 - partida_actual.primerJugador + partida_actual.n_turno
        cliente.robarCarta(carta[cartas_mez[indice]].numero, carta[cartas_mez[indice]].valor, carta[cartas_mez[indice]].tipo)
        print("El puntaje del usuario ", cliente.nombre_de_usuario, " es: ", cliente.puntos)
        cliente.seguirJugando()
    partida_actual.incrementarTurno()
    print("-------------------------------------------------------------")
partida_actual.obtenerGanador()
