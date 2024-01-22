import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog

compartments = {}
max_items_allowed = float('inf')

def get_number_of_compartments():
    try:
        return int(simpledialog.askstring("Number of Compartments", "Enter the number of compartments:"))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return get_number_of_compartments()

def set_max_items_allowed():
    global max_items_allowed
    max_items_allowed = simpledialog.askinteger("Set Maximum Items", "Enter the maximum number of items allowed:")
    if max_items_allowed is not None:
        messagebox.showinfo("Info", f"Maximum number of items set to {max_items_allowed}.")

def set_number_of_compartments():
    global compartments
    num_compartments = get_number_of_compartments()
    compartments = {f"Compartment {i+1}": {"item": None, "quantity": 0, "max_quantity": max_items_allowed} for i in range(num_compartments)}
    messagebox.showinfo("Info", f"Number of compartments set to {num_compartments}.")

def show_empty_compartments():
    empty_compartments = get_free_compartments()
    if not empty_compartments:
        messagebox.showinfo("Info", "All compartments are occupied.")
        return

    empty_compartments_window(empty_compartments)

def empty_compartments_window(empty_compartments):
    window = tk.Toplevel(root)
    window.title("Empty Compartments")

    listbox = tk.Listbox(window)
    for compartment in empty_compartments:
        listbox.insert(tk.END, compartment)

    listbox.pack(padx=50, pady=50)

    select_button = tk.Button(window, text="Select Compartment", command=lambda: store_item_from_window(window, listbox.get(tk.ACTIVE)))
    select_button.pack(pady=10)

def store_item_from_window(window, selected_compartment):
    window.destroy()
    if selected_compartment:
        item = simpledialog.askstring("Store Item", "Enter the item to store:")
        if item:
            quantity = simpledialog.askinteger("Store Item", "Enter the quantity:")
            if quantity is not None:
                if quantity > max_items_allowed:
                    messagebox.showinfo("Info", f"Exceeded maximum quantity of {max_items_allowed}.")
                else:
                    compartments[selected_compartment]["item"] = item
                    compartments[selected_compartment]["quantity"] += quantity
                    message = f"{item} stored in {selected_compartment}"
                    messagebox.showinfo("Info", message)
                    show_main_screen()

def retrieve_item():
    item = simpledialog.askstring("Retrieve Item", "Enter the item to retrieve:")
    if not item:
        return
    
    quantity_to_retrieve = simpledialog.askinteger("Retrieve Item", f"Enter the quantity of {item} to retrieve:")
    if quantity_to_retrieve is not None:
        compartments_to_retrieve = get_compartments_with_quantity(item, quantity_to_retrieve)

        if compartments_to_retrieve:
            for compartment in compartments_to_retrieve:
                compartments[compartment]["quantity"] -= quantity_to_retrieve
                if compartments[compartment]["quantity"] == 0:
                    compartments[compartment]["item"] = None

            message = f"{quantity_to_retrieve} {item}(s) retrieved from compartments: {', '.join(compartments_to_retrieve)}"
            messagebox.showinfo("Info", message)
        else:
            message = f"{item} not found in sufficient quantity in any compartment."
            messagebox.showinfo("Info", message)
    # compartments_with_item = [compartment for compartment, stored_item in compartments.items() if stored_item == item]

    # if compartments_with_item:
    #     message = f"{item} found in compartments: {', '.join(compartments_with_item)}"
    #     messagebox.showinfo("Info", message)
    #     print(f"{item} found in compartments: {', '.join(compartments_with_item)}")
    # else:
    #     message = f"{item} not found in any compartment."
    #     messagebox.showinfo("Info", message)
    #     print(f"{item} not found in any compartment.")

    show_main_screen()

def get_free_compartments():
    return [compartment for compartment, data in compartments.items() if data["item"] is None]

def get_compartments_with_quantity(item, quantity):
    return [compartment for compartment, data in compartments.items() if data["item"] == item and data["quantity"] >= quantity]

def show_main_screen():
    root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    root.title("MAS")
    

    ttk.Label(root, text="MAS", foreground='white', background='black', 
              font=('Arial', 48, 'bold'), 
              relief='raised').pack(padx=20, pady=20)
    
    tk.Button(root, text='Drug Compartments', foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='pirate', 
                        command=set_number_of_compartments).pack(padx=50,pady=50)
    
    tk.Button(root, text='Maximum Medications', foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='pirate', 
                        command=set_max_items_allowed).pack(padx=50,pady=50)
    
    tk.Button(root, text="Store Medications", foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='gumby', 
                        command=show_empty_compartments).pack(padx=50,pady=50)
    
    tk.Button(root, text='Retrieve Medications', foreground='black', background='orange', 
                        font=('Arial', 24, 'bold'), relief='raised', cursor='pirate', 
                        command=retrieve_item).pack(padx=50,pady=50)
    

    root.mainloop()
