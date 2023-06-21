from multiprocessing import Process
import time
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import checkprivate
import chkping


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'Check-WGGalpao'
    _svc_display_name_ = 'Check-WGGalpao'

    logfile = checkprivate.logfile

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_running = True

    def SvcStop(self):
        with open(checkprivate.logfile, 'a') as file:
            file.write(f'\nRecebi Stop!\n')
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        with open(checkprivate.logfile, 'a') as file:
            file.write(f'\nRecebi Run!\n')
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        # Coloque aqui o código principal do seu serviço
        with open(checkprivate.logfile, 'a') as file:
            file.write(f'\nServiço em execução!\n')
        while self.is_running:
            try:
                # Criação dos processos
                processo1 = Process(target=chkping.inicio1())
                processo2 = Process(target=chkping.inicio2())
                processo3 = Process(target=chkping.inicio3())
                processo4 = Process(target=chkping.inicio4())

                # Inicia os processos
                processo1.start()
                processo2.start()
                processo3.start()
                processo4.start()

                # Aguarda a finalização dos processos
                processo1.join()
                processo2.join()
                processo3.join()
                processo4.join()

                with open(checkprivate.logfile, 'a') as file:
                    file.write(f'While!\n')
                    time.sleep(180)
            except Exception as e:
                with open(checkprivate.logfile, 'a') as file:
                    file.write(f'\nFALHA! - Self.Runing - {e}')
            
            pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
