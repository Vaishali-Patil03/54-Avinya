from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import SimpleDialog
from serviceScanner import Running_processes, List_services, terminate_processes
from portScanner import port_scanner
from webScanner import scan_xss


main_frame = Tk()
main_frame.geometry("800x720")
photo = PhotoImage(file="scn_1.png")
main_frame.wm_title("Security Scanner")
main_frame.iconphoto(False, photo)
bg = PhotoImage(file="bg_1.png")
label2 = Label(main_frame, image=bg)
label2.place(x=0, y=0, relwidth=1, relheight=1)
button_fram = Frame(main_frame)
button_fram.place(x=0, y=0)
detail_frame = Frame(main_frame)
detail_frame.place(x=215, y=0)


def display_running_processes():
    t = 1
    for widget in detail_frame.winfo_children():
        widget.destroy()
    process_id_name = Running_processes()
    Label(detail_frame, text=f"PID        Process Name                                       ", font=(
        "Arial", 14), width=40, borderwidth=1, relief="solid", pady=10).grid(row=0, column=2)
    process_name = Listbox(detail_frame, font=(
        "Arial", 14), width=40, height=25)
    for i in range(len(process_id_name)):
        process_name.insert(
            1, f"{process_id_name[i].split('_')[0]:<10}  {process_id_name[i].split('_')[1]}")
    process_name.grid(row=1, column=2)

    def selected_item():
        i = process_name.curselection()
        prc_name = process_name.get(i[0]).split(" ")
        terminate_processes(prc_name[len(prc_name)-1])
        process_name.delete(ANCHOR)
    for widget in button_fram.winfo_children():
        t += 1
    if t == 6:
        terminate_processe = Button(button_fram, font=("Arial", 14),
                                    text="Terminate Processe",
                                    command=selected_item,
                                    width=18,
                                    padx=10, pady=10).pack(side=TOP)


def display_running_services():
    t = 0
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in button_fram.winfo_children():
        if t == 5:
            widget.destroy()
        t += 1
    service_id_state_name = List_services()
    Label(detail_frame, text=f"PID             Service Name                                                                 ",
          font=("Arial", 14), width=50, borderwidth=1, relief="solid", pady=10).grid(row=0, column=2)
    process_name = Listbox(detail_frame, font=(
        "Arial", 14), width=50, height=25)
    for i in range(len(service_id_state_name)):
        if service_id_state_name[i].split('_')[0] != "0":
            process_name.insert(
                i, f"{service_id_state_name[i].split('_')[0]:<10}  {service_id_state_name[i].split('_')[1]}")
    process_name.grid(row=1, column=2)


def scanning_ports():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    port_frame = Frame(main_frame)
    port_frame.place(x=221, y=57)
    port_rang = StringVar()
    for widget in port_frame.winfo_children():
        widget.destroy()
    Label(detail_frame, text="Port Range", font=(
        "Arial", 14), padx=8, pady=10).grid(row=0, column=3)
    text_box = Entry(detail_frame, font=("Arial", 14),
                     textvariable=port_rang, width=30)
    text_box.grid(row=0, column=4)
    text_box.insert(0, "ex. 0-500 default range is 0-65535")

    def start_scanning():
        try:
            result = port_scanner(port_rang.get())
            Label(port_frame, text="Open Ports",font=("Arial", 14), width=49, borderwidth=1, relief="solid", pady=10).grid(row=1, column=2)
            open_ports = Listbox(port_frame, font=("Arial", 14), width=49, height=25)
            for i in range(len(result)):
                open_ports.insert(
                    i, f"{result[i]}")
            open_ports.grid(row=2, column=2)

        except:
            tkinter.messagebox.showinfo("Alert","please enter range only ex. 0-100")
    Label(detail_frame, text="", padx=10, pady=10).grid(row=0, column=5)
    Button(detail_frame, font=("Arial", 14),
           text="Scan",
           padx=8, pady=10,
           command=start_scanning).grid(row=0, column=6)
    
def web_scanner():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    port_frame = Frame(main_frame)
    port_frame.place(x=221, y=57)
    url_rang = StringVar()
    for widget in port_frame.winfo_children():
        widget.destroy()
    Label(detail_frame, text="URL", font=(
        "Arial", 14), padx=8, pady=10).grid(row=0, column=3)
    text_box = Entry(detail_frame, font=("Arial", 14),
                     textvariable=url_rang, width=30)
    text_box.grid(row=0, column=4)
    text_box.insert(0, "Ex. https://www.google.co.in/")
    def start_scanning():
        result = scan_xss(url_rang.get())
        if result:
            tkinter.messagebox.showinfo("Alert","Given URL is vulnerable")
        else:
            tkinter.messagebox.showinfo("Alert","Given URL is Safe and non-vulnerable")
    Label(detail_frame, text="", padx=10, pady=10).grid(row=0, column=5)
    Button(detail_frame, font=("Arial", 14),
           text="Scan",
           padx=8, pady=10,
           command=start_scanning).grid(row=0, column=6)


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
Scan_Ports = Button(button_fram, font=("Arial", 14),
                    text="Scan Ports",
                    command=scanning_ports,
                    width=18,
                    padx=10, pady=10)
Scan_web_vulnerable = Button(button_fram, font=("Arial", 14),
                    text="WEB Vulnerability",
                    command=web_scanner,
                    width=18,
                    padx=10, pady=10)
Label(button_fram, text=" ", width=10, height=500).pack(side=BOTTOM)

show_running_processes.pack(side=TOP)
show_running_services.pack(side=TOP)
Scan_Ports.pack(side=TOP)
Scan_web_vulnerable.pack(side=TOP)


if __name__ == "__main__":
    main_frame.mainloop()
