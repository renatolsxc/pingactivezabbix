from pythonping import ping
import zbx
import checkprivate

def run_ping(host):
    while True:
        try:
            response = ping(host, count=6)
            loss_percentage = response.packet_loss * 100

            #with open(checkprivate.logfile, 'a') as file:
            #    file.write(f'loss = {loss_percentage}\n')
            
            if loss_percentage == 100.0:
                response_time = 0
            else:
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

#run_ping()


def inicio1():
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio1\n')
    host = "4.2.2.1"
    result = run_ping(host)
    zbxresult = zbx.send(["pingA1","rtA1","lossA1"],result)
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio1.1 - {zbxresult}\n')

def inicio2():
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio2\n')
    host = "4.2.2.2"
    result = run_ping(host)
    zbxresult = zbx.send(["pingA2","rtA2","lossA2"],result)
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio2.1 - {zbxresult}\n')
def inicio3():
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio3\n')
    host = "4.2.2.3"
    result = run_ping(host)
    zbxresult = zbx.send(["pingA3","rtA3","lossA3"],result)
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio3.1 - {zbxresult}\n')
def inicio4():
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio4\n')
    host = "4.2.2.4"
    result = run_ping(host)
    zbxresult = zbx.send(["pingA4","rtA4","lossA4"],result)
    with open(checkprivate.logfile, 'a') as file:
        file.write(f'inicio4.1 - {zbxresult}\n')