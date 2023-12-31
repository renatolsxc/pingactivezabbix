from pyzabbix import ZabbixSender, ZabbixMetric
import platform
import checkprivate

def send(chave,valor):

    # Configurações do servidor Zabbix
    zabbix_server = checkprivate.zabbix_server
    zabbix_port =  checkprivate.zabbix_port
    

    # Dados ue serão enviados
    hostname = platform.node()
    hostname=hostname.upper()
    

    # Cria uma lista de métricas ZabbixMetric
    metrics = [
        ZabbixMetric(hostname,chave[0],valor[0]),
        ZabbixMetric(hostname,chave[1],valor[1]),
        ZabbixMetric(hostname,chave[2],valor[2])
    ]

    #print(f"Hostname: {hostname}")
    #print(f"\'{hostname}\',\'{chave_unica_do_item}\',{valor_do_item}")
    # Cria uma instância do ZabbixSender
    sender = ZabbixSender(zabbix_server, zabbix_port)

    # Envia as métricas para o servidor Zabbix
    try:
        result = sender.send(metrics)
        
        # Exibe os valores
        #print(f'\tProcessados: {result.processed}')
        #print(f'\tFalhas: {result.failed}')
        #print(f'\tTotal: {result.total}')
        #print(f'\tTempo: {result.time}')
        #print(f'\tChunk: {result.chunk}')

        if not result.failed:
            if result.processed:
                return (f'TRUE: {hostname} ; {chave} ; {valor}')
            #print(f'Métricas enviadas com sucesso. - {result.time}')
            else:
                return (f'FALSE: {hostname} ; {chave} ; {valor}')
            #print(f'Falha ao enviar as métricas. - {result.time}')
        else:
            return f"Falhou ZBX - SEM TIMEOUT {hostname},{chave[0]},{valor[0]},{chave[1]},{valor[1]},{chave[2]},{valor[2]}"
        
    except Exception as e:
        return "Falhou ZBX - EXCECAO" 
        