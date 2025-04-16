import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

def get_available_currencies():
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return [currency.upper() for currency in data['rates'].keys()]

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

def validate_input(amount, from_currency, to_currency):
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "Please enter a valid number greater than zero."
    except ValueError:
        return False, "Please enter a valid amount."

    valid_currencies = get_available_currencies()

    if from_currency not in valid_currencies or to_currency not in valid_currencies:
        return False, "Please select a valid currency."

    return True, ""

def on_convert(amount_entry, from_currency, to_currency, result_label):
    amount = amount_entry.get()
    from_curr = from_currency.get().upper()  # Normalize to uppercase
    to_curr = to_currency.get().upper()  # Normalize to uppercase

    is_valid, msg = validate_input(amount, from_curr, to_curr)
    if not is_valid:
        result_label.config(text=msg)
        return

    try:
        amount = float(amount)
        converted_amount = convert_currency(amount, from_curr, to_curr)
        result_label.config(text=f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def main():
    root = tk.Tk()
    root.title("Currency Converter")

    # Set the window size
    root.geometry("600x400")

    #set background image
    bg_image = Image.open("bg.png")
    bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    currencies = get_available_currencies()

    font_heading = ("Times New Roman", 24, "bold","italic") 
    font_large = ("Times New Roman", 16)
    font_medium = ("Times New Roman", 14)

    # Heading
    heading_label = tk.Label(root, text="Currency Converter", font=font_heading, bg="light blue")
    heading_label.place(x=0, y=0, width=600, height=60)

    # Amount entry
    tk.Label(root, text="Amount:", font=font_large, bg="lightblue").place(x=150, y=100, width=100, height=30)
    amount_entry = tk.Entry(root, font=font_medium)
    amount_entry.place(x=260, y=100, width=200, height=30)

    # From currency
    tk.Label(root, text="From:", font=font_large, bg="lightblue").place(x=150, y=150, width=100, height=30)
    from_currency = ttk.Combobox(root, values=currencies, font=font_medium)
    from_currency.place(x=260, y=150, width=200, height=30)

    # To currency
    tk.Label(root, text="To:", font=font_large, bg="lightblue").place(x=150, y=200, width=100, height=30)
    to_currency = ttk.Combobox(root, values=currencies, font=font_medium)
    to_currency.place(x=260, y=200, width=200, height=30)

    # Convert button
    convert_button = tk.Button(root, text="Convert", command=lambda: on_convert(amount_entry, from_currency, to_currency, result_label), font=font_large)
    convert_button.place(x=260, y=250, width=120, height=40)

    # Result label
    global result_label
    result_label = tk.Label(root, text="", font=font_medium, bg="lightblue")
    result_label.place(x=100, y=300, width=450, height=30)

    root.resizable(0, 0)
    root.mainloop()

if __name__ == "__main__":
    main()
