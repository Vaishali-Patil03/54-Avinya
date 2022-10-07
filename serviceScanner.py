import wmi
import os
import win32con
import win32service

def Running_processes():
    f = wmi.WMI()
    print("pid        Process name")
    for process in f.Win32_Process():
        print(f"{process.ProcessId:<10} {process.Name}")
        # print(process)

def List_services():
    resume = 0
    accessSCM = win32con.GENERIC_READ

    #Open Service Control Manager
    hscm = win32service.OpenSCManager(None, None, accessSCM)

    #Enumerate Service Control Manager DB
    typeFilter = win32service.SERVICE_WIN32
    stateFilter = win32service.SERVICE_STATE_ALL
    statuses = win32service.EnumServicesStatus(hscm, typeFilter, stateFilter)

    for (short_name, desc, status) in statuses:
        print(f"{short_name}                        {desc}") 


def terminate_processes():
    ti = 0
    name = 'Process_Name'
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == name:
            process.Terminate()
            ti += 1
    if ti == 0:
        print("Process not found!!!")

if __name__ == "__main__":
    List_services();     #for listing services
    Running_processes();  #for showing running processes
    terminate_processes()   #for terminating processes
