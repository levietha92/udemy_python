import tkinter

window = tkinter.Tk()

window.minsize(100,80)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

#First row design
miles_entry_box = tkinter.Entry()
miles_entry_box.focus()
miles_entry_box.config(width=10)
miles_entry_box.grid(column=1,row=0)
miles_text = tkinter.Label()
miles_text.grid(column=2, row=0)

#Second row design
default_text = tkinter.Label(text="is equal to ")
default_text.grid(column=0,row=1)

def return_output():
    # while miles_entry_box.get() == None:
    #     km_conversion = 0
    #     print("zero")
    km_conversion = float(miles_entry_box.get()) * 1.609344
    km_output = tkinter.Label(text=km_conversion)
    km_output.grid(column=1,row=1)
    print(km_conversion)
    return km_conversion

# return_output()
km_text = tkinter.Label(text= "Km")
km_text.grid(column=2, row=1)

# Third row
calc_button = tkinter.Button(text="Calculate", command=return_output)
calc_button.grid(column=1,row=2)

window.mainloop()