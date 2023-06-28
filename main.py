from tkinter import * 
from tkinter import ttk
import json, urllib.request

def conversion():
    entry_converted_amount.delete(0,END)
    getAmount = entry_amount.get()
    getFromCurrency = default_currency.get()
    getToCurrency = default_currency_1.get()

    url = "https://v6.exchangerate-api.com/v6/f60395541395e6fbeee05dfc/latest/" + getFromCurrency
    data = urllib.request.urlopen(url)
    result = data.read()
    json_data = json.loads(result)
    setConvertedAmount = float(getAmount) * json_data['conversion_rates'][getToCurrency]
    entry_converted_amount.insert(0,str(round(setConvertedAmount,4)))

def clear_all():
    entry_amount.delete(0,END)
    entry_converted_amount.delete(0,END)

if __name__ == "__main__":

    # GUI configurations
    window = Tk()
    window.title("Currency Converter")
    window.geometry = (450, 450)
    window.config(bg="white")
    window.resizable(False,False)
    Image = PhotoImage(file="logo_icon.png")
    window.iconphoto(False,Image)

    # Frames
    bottom_frame = Frame(window,bg="white", width=450, height=350)
    bottom_frame.grid(row=1,column=0)
    head_frame = Frame(window,bg="white",width=450,height=100)
    head_frame.grid(row=0,column=0)


    # Labels
    label_1 = Label(head_frame,text="Currency Converter",font="Verdana 19 bold", bg="white")
    label_1.grid(row=0,column=0)

    label_space = Label(bottom_frame, text="", bg="white")
    label_space.grid(row=0,column=0)

    label_2 = Label(bottom_frame,text="Amount:",font="Verdana 12 bold", bg="white")
    label_2.grid(row=1,column=0, sticky=W)

    label_3 = Label(bottom_frame,text="From Currency:", font="Verdana 12 bold", bg="white")
    label_3.grid(row=2,column=0,sticky=W)

    label_4 = Label(bottom_frame, text="To Currency:", font="Verdana 12 bold", bg="white")
    label_4.grid(row=3,column=0,sticky=W)

    label_5 = Label(bottom_frame, text="Converted Amount:", font="Verdana 12 bold", bg="white")
    label_5.grid(row=7,column=0,sticky=W)
    
    label_space_1 = Label(bottom_frame, text="", bg="white")
    label_space_1.grid(row=8,column=0)

    # Buttons
    bt_1 = Button(bottom_frame, text="Convert", font="Verdana 12 bold", bg="#48faf4",activebackground="#48faf4",
                  command=conversion)
    bt_1.grid(row=4,column=0)

    bt_2 = Button(bottom_frame, text="Clear All", font="Verdana 12 bold", bg="#48faf4",
                  activebackground="#48faf4", command=clear_all)
    bt_2.grid(row=8,column=0)

    # Entrys
    entry_amount = Entry(bottom_frame, bg="white", width=15)
    entry_amount.grid(row=1,column=0,sticky=E)

    entry_converted_amount = Entry(bottom_frame, bg="white", width=25)
    entry_converted_amount.grid(row=7, column=1,sticky=W)

    # Combo Boxs
    currency = ['USD', 'BRL', 'EUR', 'GBP', 'CNY', 'JPY', 'AUD']

    default_currency = StringVar()
    default_currency.set("Select a Currency")

    from_currency_list_box = OptionMenu(bottom_frame,default_currency,*currency)
    from_currency_list_box.grid(row=2,column=1, ipadx=30, sticky=W)

    default_currency_1 = StringVar()
    default_currency_1.set("Select a Currency")

    to_currency_list_box = OptionMenu(bottom_frame,default_currency_1, *currency)
    to_currency_list_box.grid(row=3,column=1, ipadx=30, sticky=W)






    window.mainloop()