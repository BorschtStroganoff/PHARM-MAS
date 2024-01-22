import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog

class DrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawer Organizer")

        # Define the dimensions of the drawer
        self.rows = 4
        self.columns = 5

        # Create a 2D array to represent compartments in the drawer
        self.compartments = [[None] for _ in range(self.rows * self.columns)]

        # Create buttons for each compartment
        for i in range(self.rows):
            for j in range(self.columns):
                compartment_index = i * self.columns + j
                button = tk.Button(root, text=f"Compartment {compartment_index + 1}", command=lambda index=compartment_index: self.open_message_box(index))
                button.grid(row=i, column=j, padx=5, pady=5)

    def open_message_box(self, compartment_index):
        current_contents = self.compartments[compartment_index]
        user_input = simpledialog.askstring("Input", f"Enter the contents for Compartment {compartment_index + 1}:", initialvalue=current_contents)

        if user_input is not None:
            self.compartments[compartment_index] = user_input
            tk.messagebox.showinfo("Success", f"Contents for Compartment {compartment_index + 1} set to: {user_input}")

def compartment_full(dummy): #(dummy function to replace) if there is no empty compartment to load drugs in
    dummy = int(input())
    return dummy
def check_compartment(): #check if there is any empty box for load drug process
    if (compartment_full == 0):
        message_full = messagebox.showinfo("No empty compartment")
    else:
        window2.withdraw()
        window_choose_box.deiconify()
        
def open_window2(): #open window 2
    window1.withdraw()  # Hide the first window
    window2.deiconify()  # Show the second window
def back_to_window1(): #main window
    window2.withdraw()  # Hide the second window
    window3.withdraw()
    window_choose_box.withdraw()
    window1.deiconify()  # Show the first window
def open_window3(): #open window 3
    window1.withdraw()
    window3.deiconify()

if __name__ == "__main__":
    # Create the main application window (window1)
    window1 = tk.Tk()
    #window1.geometry('500x500')
    window1.state('zoomed')
    window1.title("MAS")


    # Create a label and a button in the first window
    ttk.Label(window1, text="Drugs, cuh?", foreground='white', background='black', font=('Arial', 48, 'bold'), relief='raised').pack(padx=20, pady=20)
    tk.Button(window1, text="Drug Possession", foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='gumby', command=open_window2).pack(padx=50,pady=50)
    tk.Button(window1, text='Drug Distribution', foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='pirate', command=open_window3).pack(padx=50,pady=50)


    #------Load Drugs------#
    # Create the second window 
    window2 = tk.Toplevel(window1)  
    window2.geometry('500x500')
    window2.title("Window 2")

    # Create a label and a button in the second window
    ttk.Label(window2, text="Drug Possession", foreground='black', background='orange', font=('Arial', 24, 'bold'), relief='raised').pack(padx=20, pady=20)
    tk.Button(window2, text='Drug Compartment', command=check_compartment).pack(padx=50,pady=50)

    button12 = tk.Button(window2, text="This ain't it", command=back_to_window1)

    button12.pack()
    window2.withdraw()  # Initially hide the second window

    #------Get Drugs------#
    # Create the third window 
    window3 = tk.Toplevel(window1)  
    window3.geometry('500x500')
    window3.title("Window 3")

    # Create a label and a button in the third window
    ttk.Label(window3, text='Drug Distribution', foreground='black', background='orange', font=('Arial', 24, 'bold'), relief='raised').pack(padx=20, pady=20)
    button13 = tk.Button(window3, text="Bach", command=back_to_window1)

    button13.pack()
    window3.withdraw()  # Initially hide the third window

    #------Choose Compartment for Load Drug------#
    # Create the third window 
    window_choose_box = tk.Toplevel(window1)  
    #window_choose_box.geometry('500x500')
    window_choose_box.title("Window 3")

    # Create a label and a button in the third window
    ttk.Label(window_choose_box, text='Choose Box', foreground='black', background='orange', font=('Arial', 24, 'bold'), relief='raised').pack(padx=20, pady=20)



    button14 = tk.Button(window_choose_box, text="Bach", command=back_to_window1)

    button14.pack()
    window_choose_box.withdraw()  # Initially hide the third window





    window1.mainloop()  # Start the main event loop 
    #window 1 is main screen where you choose to load or take drugs
    #window 2 is load drug
    #window 3 is take drug

