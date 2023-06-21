import time
from pythonping import ping
import zbx

def run_ping(host):
    while True:
        try:
            response = ping('www.google.com', count=6)
            loss_percentage = response.packet_loss
            response_time = response.rtt_avg_ms / 1000  # Convertendo para segundos
            return [1,format(response_time),format(loss_percentage)]
            #print("Pingou: Sim")
            #print("Loss: {}%".)
            #print("Tempo de resposta: {} segundos".f)
        except Exception as e:
            return [0,0,100]
            #print("Pingou: Não")
            #print("Loss: N/A")
            #print("Tempo de resposta: N/A")
            #print("Erro:", e)

        #time.sleep(180)  # Aguarda 3 minutos (180 segundos) antes do próximo teste

run_ping()


def inicio1():
    host = "4.2.2.1"
    result = run_ping(host)
    zbx.send(["pingA1","rtA1","lossA1"],result)
def inicio2():
    host = "4.2.2.2"
    result = run_ping(host)
    zbx.send(["pingA2","rtA2","lossA2"],result)
def inicio3():
    host = "4.2.2.3"
    result = run_ping(host)
    zbx.send(["pingA3","rtA3","lossA3"],result)
def inicio4():
    host = "4.2.2.4"
    result = run_ping(host)
    zbx.send(["pingA4","rtA4","lossA4"],result)