import time
from pythonping import ping

def run_ping():
    while True:
        try:
            response = ping('www.google.com', count=6)
            loss_percentage = response.packet_loss
            response_time = response.rtt_avg_ms / 1000  # Convertendo para segundos

            print("Pingou: Sim")
            print("Loss: {}%".format(loss_percentage))
            print("Tempo de resposta: {} segundos".format(response_time))
        except Exception as e:
            print("Pingou: Não")
            print("Loss: N/A")
            print("Tempo de resposta: N/A")
            print("Erro:", e)

        time.sleep(180)  # Aguarda 3 minutos (180 segundos) antes do próximo teste

run_ping()
