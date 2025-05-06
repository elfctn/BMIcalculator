import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=100, pady=100)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / float(height) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")


weight_input_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=20)
weight_input.pack()
height_input_label = tkinter.Label(text="Enter Your Height (m)")
height_input_label.pack()
height_input = tkinter.Entry(width=20)
height_input.pack()
calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()



window.mainloop()