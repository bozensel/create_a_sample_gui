import customtkinter

root= customtkinter.CTk()
root.geometry('900x560')
root.configure(bg_color='#262626')
root.resizable(2,4)
root.title('Sample GUI')

with open("Some text for GUI.txt") as f:
    gui_text = f.read()

sample_label = customtkinter.CTkLabel(master=root, text="Some GUI")
sample_label.place(y=10, x=20)

sample_label_entry = customtkinter.CTkTextbox(master=root)
sample_label_entry.grid(row=200, column=20)
sample_label_entry.place(y=50, x=25, width=510, height=750)
sample_label_entry.insert("0.0", gui_text)

root.mainloop()
