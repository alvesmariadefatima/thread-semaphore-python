from threading import Semaphore, Thread
from time import sleep

# Número máximo de threads a serem executadas simultaneamente
control_threads = Semaphore(5)

# Função para visualizar o log de uma thread de semáforo em Python
def view_log(number: int):
  with control_threads:
    print(f'O número atual é: {number}')
    sleep(5)

# Fazendo loop 20x mais a cada 5x terá uma pausa de 5 segundos
for number in range(20):
  thread = Thread(
      target = view_log,
      args = [number]
  )

  thread.start()