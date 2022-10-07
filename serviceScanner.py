import wmi

def Running_processes():
    f = wmi.WMI()
    print("pid        Process name")
    for process in f.Win32_Process():
        print(f"{process.ProcessId:<10} {process.Name}")

def List_services():
    f = wmi.WMI()
    print("pid        Service name                                            Status")
    for service in f.Win32_Service():
        print(f"{service.ProcessId:<10}    {service.Caption:<10}              {service.State:} ")

def terminate_processes(name):
    ti = 0
    f = wmi.WMI()
    for process in f.Win32_Process():
        if not ti:
            if process.name == name:
                process.Terminate()
                print("process terminated")
                ti += 1
    if ti == 0:
        print("Process not found")
    
def terminate_services(service_name):
    pass

if __name__ == "__main__":
    while True:
        print("1. Show all running Processes \n2. Show all running services \n3. Stop Specific Process \n4. Quit")
        option = int(input("Write Option number : "))
        if option == 1:
            Running_processes() 
        elif option == 2:
            List_services()    
        elif option == 3:
            process_name = input("write process name to stop process : ")
            terminate_processes(process_name)
        elif option == 4:
            break
        iteration = input("do you want to continue (y/n) : ")
        if(iteration == "n"):
            break
