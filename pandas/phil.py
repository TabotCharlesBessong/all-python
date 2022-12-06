import time
import random
import threading

N = 5
TIEMPO_TOTAL = 3


class Filosofo(threading.Thread):
    semaforo = threading.Lock()  # SEMAFORO BINARIO ASEGURA LA EXCLUSION MUTUA
    estado = []  # PARA CONOCER EL ESTADO DE CADA FILOSOFO
    tenedores = []  # ARRAY DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    count = 0

    def __init__(self):
        super().__init__()  # HERENCIA
        self.id = Filosofo.count  # DESIGNA EL ID AL FILOSOFO
        Filosofo.count += 1  # AGREGA UNO A LA CANT DE FILOSOFOS
        Filosofo.estado.append('PENSANDO')  # EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        Filosofo.tenedores.append(threading.Semaphore(0))  # AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        print("FILOSOFO {0} - PENSANDO".format(self.id))

    def __del__(self):
        print("FILOSOFO {0} - Se para de la mesa".format(self.id))  # NECESARIO PARA SABER CUANDO TERMINA EL THREAD

    def pensar(self):
        time.sleep(random.randint(0, 5))  # CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO

    def derecha(self, i):
        return (i - 1) % N  # BUSCAMOS EL INDICE DE LA DERECHA

    def izquierda(self, i):
        return (i + 1) % N  # BUSCAMOS EL INDICE DE LA IZQUIERDA

    def verificar(self, i):
        if Filosofo.estado[i] == 'HAMBRIENTO' and Filosofo.estado[self.izquierda(i)] != 'COMIENDO' and Filosofo.estado[
            self.derecha(i)] != 'COMIENDO':
            Filosofo.estado[i] = 'COMIENDO'
            Filosofo.tenedores[
                i].release()  # SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A
            # COMIENDO

    def tomar(self):
        Filosofo.semaforo.acquire()  # SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        Filosofo.estado[self.id] = 'HAMBRIENTO'
        self.verificar(self.id)  # VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        Filosofo.semaforo.release()  # SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        Filosofo.tenedores[self.id].acquire()  # SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO

    def soltar(self):
        Filosofo.semaforo.acquire()  # SEÑALA QUE SOLTARA LOS TENEDORES
        Filosofo.estado[self.id] = 'PENSANDO'
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        Filosofo.semaforo.release()  # YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
        time.sleep(2)  # TIEMPO ARBITRARIO PARA COMER
        print("FILOSOFO {} TERMINO DE COMER".format(self.id))

    def run(self):
        for i in range(TIEMPO_TOTAL):
            self.pensar()  # EL FILOSOFO PIENSA
            self.tomar()  # AGARRA LOS TENEDORES CORRESPONDIENTES
            self.comer()  # COME
            self.soltar()  # SUELTA LOS TENEDORES


def main():
    lista = []
    for i in range(N):
        lista.append(Filosofo())  # AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start()  # ES EQUIVALENTE A RUN()

    for f in lista:
        f.join()  # BLOQUEA HASTA QUE TERMINA EL THREAD


if __name__ == "__main__":
    main()