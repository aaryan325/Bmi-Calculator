import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Bmi Calculator By @Aaryansarda")

def Calculate_BMI():
    try:
        kg = float(entry_kg.get())
        height = float(entry_height.get())
        height /= 100
        bmi = kg / (height ** 2)
        label_result.config(text=f"BMI: {round(bmi, 2)}")
    except ValueError:
       tk.messagebox.showerror(title="Error", message="The number you entered is not a value") 

def Calculate_average_weight():
    try:
        kg = float(entry_kg.get())
        height = float(entry_height.get())
        height /= 100
        bmi = kg / (height ** 2)
        appropriate_weight = 18.5 * (height ** 2)
        appropriate_weight1 = 25 * (height ** 2)
        label_result1.config(text=f"your weight should be in between {round(appropriate_weight)} to {round(appropriate_weight1)}")
    except ValueError:
        tk.messagebox.showerror(title="Error", message="The number you entered is not a value")
    except:
        tk.messagebox.showerror(title="Error", message="You haven't entered a value")


#Create GUI

label_kg = tk.Label(root, text="KG : ", width=3)
label_kg.grid(row=0, column=0)

entry_kg = tk.Entry(root)
entry_kg.grid(row=0, column=1)

label_height = tk.Label(root, text="HEIGHT(cm) : ")
label_height.grid(row=1, column=0)

entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

button_calculate = tk.Button(root, text="Calculate", command=Calculate_BMI)
button_calculate.grid(row=2, column=0)

button_calculate1 = tk.Button(root, text="See your Appropriate weight", command=Calculate_average_weight)
button_calculate1.grid(row=2, column=1, columnspan=3)

label_result = tk.Label(root, text="BMI : ")
label_result.grid(row=3, column=1)

label_result1 = tk.Label(root, text="Appropriate Weight : ")
label_result1.grid(row=3, column=2, columnspan=4)



label_bmiInfo = tk.Label(root, text="Very Severely Underweight : 15")
label_bmiInfo.grid(row=5, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Severely underweight : from 15 to 16")
label_bmiInfo.grid(row=6, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Underweight : 16 to 18.5")
label_bmiInfo.grid(row=7, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Normal (healthy weight) : 18.5 to 25")
label_bmiInfo.grid(row=8, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Overweight : 25 to 30")
label_bmiInfo.grid(row=9, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Obese Class I (Moderately obese) : 30 to 35")
label_bmiInfo.grid(row=10, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Obese Class II (Severely obese) : 35 to 40")
label_bmiInfo.grid(row=11, column=0, columnspan=5)

label_bmiInfo = tk.Label(root, text="Obese Class III (Very severely obese)")
label_bmiInfo.grid(row=12, column=0, columnspan=5)

root.mainloop()