from tkinter import *
from serviceScanner import Running_processes, List_services, terminate_processes

main_frame = Tk()
main_frame.geometry("800x720")
button_fram = Frame(main_frame)
button_fram.place(x=0, y = 0)
detail_frame = Frame(main_frame)
detail_frame.place(x=215,y=0)

def display_running_processes():
    t = 1
    for widget in detail_frame.winfo_children():
        widget.destroy()
    process_id_name = Running_processes()
    Label(detail_frame, text = f"PID        Process Name                                       ", font=("Arial", 14), width=40, borderwidth=1, relief="solid", pady=10).grid(row=0, column=2)  
    process_name = Listbox(detail_frame, font=("Arial", 14), width=40, height=25)
    for i in range(len(process_id_name)): 
        process_name.insert(1, f"{process_id_name[i].split('_')[0]:<10}  {process_id_name[i].split('_')[1]}" )
    process_name.grid(row=1, column=2)

    def selected_item():
        i = process_name.curselection()
        prc_name = process_name.get(i[0]).split(" ")
        terminate_processes(prc_name[len(prc_name)-1])
        process_name.delete(ANCHOR)
    for widget in button_fram.winfo_children():
        t+=1
    if t == 3:
        terminate_processe = Button(button_fram, font=("Arial", 14), 
                                    text="Terminate Processe",
                                    command= selected_item,
                                    width=18,
                                    padx=10, pady=10).pack(side=TOP)


def display_running_services():
    t=0
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in button_fram.winfo_children():
        if t == 2:widget.destroy()
        t+=1
    service_id_state_name = List_services()
    Label(detail_frame, text = f"PID             Service Name                                                                 ", font=("Arial", 14), width=50, borderwidth=1, relief="solid", pady=10).grid(row=0, column=2)  
    process_name = Listbox(detail_frame, font=("Arial", 14), width=50, height=25)
    for i in range(len(service_id_state_name)): 
        if service_id_state_name[i].split('_')[0] != "0":
            process_name.insert(1, f"{service_id_state_name[i].split('_')[0]:<10}  {service_id_state_name[i].split('_')[1]}" )
    process_name.grid(row=1, column=2)
    



show_running_processes = Button(button_fram, font=("Arial", 14), 
                                text="Running Processes", 
                                width=18,
                                command=display_running_processes, 
                                padx=10, pady=10)
show_running_services = Button(button_fram, font=("Arial", 14), 
                                text="Running Services", 
                                command=display_running_services, 
                                width=18,
                                padx=10, pady=10)
                
show_running_processes.pack(side=TOP)
show_running_services.pack(side=TOP)


if __name__ == "__main__":
    main_frame.mainloop()