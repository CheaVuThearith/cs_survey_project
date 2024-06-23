import math
from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, StringVar
from page_navigation import delete_cards, navigate
from components import info_card
from sql_integration import get_data


def make_cards_customers(window, canvas, page, where="CustomerID"):
    cards_list = []
    customers = get_data("Customers", page, limit=3, where=where)
    for i, customer in enumerate(customers):
        card = info_card(
            obj=customer,
            canvas=canvas,
            type="customer",
            window=window,
            pos=i,
            top_text=f"{customer["Name"]}",
            bottom_text=customer["PhoneNumber"],
            status=customer["Status"],
        )
        cards_list.append(card)
        card.create_card()
    return cards_list


def make_cards_tables(window, canvas, page, where="TableID"):
    cards_list = []
    tables = get_data("Tables", page, limit=3, where=where)
    for i, table in enumerate(tables):
        card = info_card(
            obj=table,
            canvas=canvas,
            type="table",
            window=window,
            pos=i,
            top_text=f"No. {table["TableID"]}",
            bottom_text=table["Capacity"],
            status=table["Status"],
        )
        cards_list.append(card)
        card.create_card()
    return cards_list


def tables_page(window, canvas: Canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"yellow_assets\info_page")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(49.0, 265.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, staffprofile),
        relief="flat",
    )
    button_1.place(x=29.0, y=192.5, width=40.0, height=40.0)

    navbar_customers_image = PhotoImage(
        file=relative_to_assets("customers_deactivated.png")
    )
    navbar_customers = Button(
        image=navbar_customers_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, customers_page),
        relief="flat",
    )
    navbar_customers.place(x=29.0, y=245.5, width=40.0, height=40.0)

    navbar_reservations_image = PhotoImage(
        file=relative_to_assets("reservations_activated.png")
    )
    navbar_reservations = Button(
        image=navbar_reservations_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat",
    )
    navbar_reservations.place(x=29.0, y=298.5, width=40.0, height=40.0)

    canvas.create_text(
        118.0,
        67.0,
        anchor="nw",
        text="Reservations",
        fill="#232121",
        font=("Inter Bold", 36 * -1),
    )

    def search_tables(*args):
        nonlocal cards_list
        nonlocal current_page
        delete_cards(cards_list)
        search = entry_text.get()
        where = f"TableID LIKE '%{search}%' or Capacity LIKE '%{search}%' or Status LIKE '%{search}%'"
        cards_list = make_cards_tables(window, canvas, 1, where)
        current_page = 1

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(656.0, 89.0, image=image_image_2)

    entry_text = StringVar()
    entry_text.trace_add("write", search_tables)

    entry_1 = Entry(
        bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0, textvariable=entry_text
    )
    entry_1.place(x=440.0, y=82.0, width=404.0, height=16.0)

    canvas.create_text(
        118.0,
        143.0,
        anchor="nw",
        text=f"Total Tables - {len(get_data("Tables", limit=100, page=1, where="TableID"))}",
        fill="#000000",
        font=("Inter", 16 * -1),
    )

    current_page = 1
    cards_list = make_cards_tables(window, canvas, current_page, where="TableID")

    def paginate_tables(backwards):
        nonlocal cards_list
        nonlocal current_page
        search = entry_text.get()
        where = f"TableID LIKE '%{search}%' or Capacity LIKE '%{search}%' or Status LIKE '%{search}%'"
        delete_cards(cards_list)
        page = (
            max(current_page - 1, 1)
            if backwards
            else min(
                current_page + 1,
                math.ceil(len(get_data("Tables", limit=100, page=1, where=where)) / 3),
            )
        )
        cards_list = make_cards_tables(window, canvas, page, where=where)
        current_page = page

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    forward_button = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: paginate_tables(backwards=False),
        relief="flat",
    )
    forward_button.place(x=877.0, y=502.0, width=25.0, height=25.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    backwards_button = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: paginate_tables(backwards=True),
        relief="flat",
    )
    backwards_button.place(x=849.0, y=502.0, width=25.0, height=25.0)
    window.mainloop()


def customers_page(window, canvas: Canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"yellow_assets\info_page")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(49.0, 265.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, staffprofile),
        relief="flat",
    )
    button_1.place(x=29.0, y=192.5, width=40.0, height=40.0)

    navbar_customers_image = PhotoImage(
        file=relative_to_assets("customers_activated.png")
    )
    navbar_customers = Button(
        image=navbar_customers_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("navbar_customers clicked"),
        relief="flat",
    )
    navbar_customers.place(x=29.0, y=245.5, width=40.0, height=40.0)

    navbar_reservations_image = PhotoImage(
        file=relative_to_assets("reservations_deactivated.png")
    )
    navbar_reservations = Button(
        image=navbar_reservations_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, tables_page),
        relief="flat",
    )
    navbar_reservations.place(x=29.0, y=298.5, width=40.0, height=40.0)

    canvas.create_text(
        118.0,
        67.0,
        anchor="nw",
        text="Customers",
        fill="#232121",
        font=("Inter Bold", 36 * -1),
    )

    current_page = 1
    cards_list = make_cards_customers(window, canvas, current_page)

    def search_customers(*args):
        nonlocal cards_list
        nonlocal current_page
        search = entry_text.get()
        where = f"CustomerID LIKE '%{search}%' or Name LIKE '%{search}%' or PhoneNumber LIKE '%{search}%' or Status LIKE '%{search}%' or TimesCancelled LIKE '%{search}%' or AmountSpent LIKE '%{search}%'"
        delete_cards(cards_list)
        cards_list = make_cards_customers(window, canvas, 1, where)
        current_page = 1

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(656.0, 89.0, image=image_image_2)

    entry_text = StringVar()
    entry_text.trace_add("write", search_customers)

    entry_1 = Entry(
        bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0, textvariable=entry_text
    )
    entry_1.place(x=440.0, y=82.0, width=404.0, height=16.0)

    canvas.create_text(
        118.0,
        143.0,
        anchor="nw",
        text=f"Total Customers - {len(get_data("Customers", limit=100, page=1, where="CustomerID"))}",
        fill="#000000",
        font=("Inter", 16 * -1),
    )

    def paginate_customers(backwards):
        nonlocal cards_list
        nonlocal current_page
        search = entry_text.get()
        where = f"CustomerID LIKE '%{search}%' or Name LIKE '%{search}%' or PhoneNumber LIKE '%{search}%' or Status LIKE '%{search}%' or TimesCancelled LIKE '%{search}%' or AmountSpent LIKE '%{search}%'"
        delete_cards(cards_list)
        page = (
            max(current_page - 1, 1)
            if backwards
            else min(
                current_page + 1,
                math.ceil(
                    len(get_data("Customers", limit=100, page=1, where=where)) / 3
                ),
            )
        )
        cards_list = make_cards_customers(window, canvas, page, where=where)
        current_page = page

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    forward_button = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: paginate_customers(backwards=False),
        relief="flat",
    )
    forward_button.place(x=877.0, y=502.0, width=25.0, height=25.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    backwards_button = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: paginate_customers(backwards=True),
        relief="flat",
    )
    backwards_button.place(x=849.0, y=502.0, width=25.0, height=25.0)
    window.mainloop()

from navigation import navigate
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import pymysql.cursors

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import messagebox

from pages import customers_page, tables_page
from sql_credentials import get_creds


def startwindow(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"green_assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(862.0, 320.0, image=image_image_1)

    canvas.create_text(
        25.0,
        48.0,
        anchor="nw",
        text="Restaurant ",
        fill="#232121",
        font=("Inter Bold", 48 * -1),
    )

    canvas.create_text(
        24.0,
        108.0,
        anchor="nw",
        text="Table ",
        fill="#232121",
        font=("Inter Bold", 48 * -1),
    )

    canvas.create_text(
        25.0,
        166.0,
        anchor="nw",
        text="Reservation",
        fill="#232121",
        font=("Inter Bold", 48 * -1),
    )

    canvas.create_text(
        30.0,
        245.0,
        anchor="nw",
        text="Member Login",
        fill="#232121",
        font=("Inter Bold", 20 * -1),
    )

    canvas.create_rectangle(24.0, 232.0, 342.0, 233.0, fill="#232121", outline="")

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    loginbutton = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, stafflogin),
        relief="flat",
    )
    loginbutton.place(x=30.0, y=352.0, width=108.0, height=47.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    registerbutton = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, staffregistration),
        relief="flat",
    )
    registerbutton.place(x=153.0, y=351.0, width=177.0, height=56.0)

    canvas.create_rectangle(387.0, 0.0, 396.0, 540.0, fill="#D9D9D9", outline="")
    window.mainloop()


def staffregistration(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"green_assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def button_click():
        gender = "Male" or "Female"
        if entry_2.get() == "":
            messagebox.showerror("Alert", "Please enter your first name")
        elif entry_5.get() == "":
            messagebox.showerror("Alert", "Please enter your last name")
        elif entry_3.get() == "":
            messagebox.showerror("Alert", "Please enter your gender")
        elif entry_3.get() != gender:
            messagebox.showerror("Alert", "Please enter Male or Female")
        elif entry_4.get() == "":
            messagebox.showerror("Alert", "Please enter your position")
        elif entry_1.get() == "":
            messagebox.showerror("Alert", "Please enter your username")
        elif entry_6.get() == "":
            messagebox.showerror("Alert", "Please enter your password")
        elif entry_7.get() == "":
            messagebox.showerror("Alert", "Please confirm your password")
        elif entry_6.get() != entry_7.get():
            messagebox.showerror("Alert", "Password do not match")
        else:
            global username

            firstname = entry_2.get()
            lastname = entry_5.get()
            gender = entry_3.get()
            position = entry_4.get()
            username = entry_1.get()
            password = entry_6.get()

            print(firstname, lastname, gender, position, username, password)

            conn = None
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password=get_creds(),
                    db="cs_survey",
                )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)
            else:
                print("Database Connection SUCCESS")

            # STEP 3 - CHECK Connection is Establish or not
            if conn is not None:
                # STEP 4 Create Query
                query = "insert into Employees(FirstName, LastName, Gender, Position, Username, Password) values (%s, %s, %s, %s, %s, %s) "

                try:
                    # STEP 6 - CREATE cursor Object
                    cursor = conn.cursor()

                    # STEP 7 - EXECUTE THE Query
                    noofrecoredinsert = cursor.execute(
                        query,
                        (firstname, lastname, gender, position, username, password),
                    )
                    conn.commit()
                except Exception as e:
                    print("INSERT PROBLEM ", e)
                else:
                    if noofrecoredinsert > 0:
                        print("RECORD INSERTED ")
                        messagebox.showinfo("Success", "Successful Registration")
                        navigate(window, stafflogin)

                        # STEP 8 - Commit Database

                        entry_1.delete(0, END)
                        entry_2.delete(0, END)
                        entry_3.delete(0, END)
                        entry_4.delete(0, END)
                        entry_5.delete(0, END)
                        entry_6.delete(0, END)
                        entry_7.delete(0, END)

                    else:
                        print("RECORD NOT INSERTED")
                finally:
                    conn.close()

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(262.0, 323.9999084472656, image=image_image_1)

    canvas.create_rectangle(505.0, 119.0, 906.0, 503.0, fill="#D9D9D9", outline="")

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(706.0, 271.0, image=entry_image_1)
    entry_1 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_1.place(x=535.0, y=256.0, width=342.0, height=28.0)

    canvas.create_text(
        525.0,
        240.0,
        anchor="nw",
        text="USERNAME",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(608.0, 163.5, image=entry_image_2)
    entry_2 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_2.place(x=531.5, y=150.0, width=153.0, height=25.0)

    canvas.create_text(
        527.0,
        134.0,
        anchor="nw",
        text="FIRST NAME",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(608.0, 216.5, image=entry_image_3)
    entry_3 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_3.place(x=531.5, y=203.0, width=153.0, height=25.0)

    canvas.create_text(
        527.0,
        187.0,
        anchor="nw",
        text="GENDER",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(801.0, 216.5, image=entry_image_4)
    entry_4 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_4.place(x=724.5, y=203.0, width=153.0, height=25.0)

    canvas.create_text(
        720.0,
        187.0,
        anchor="nw",
        text="POSITION",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(801.0, 163.5, image=entry_image_5)
    entry_5 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_5.place(x=724.5, y=150.0, width=153.0, height=25.0)

    canvas.create_text(
        720.0,
        134.0,
        anchor="nw",
        text="LAST NAME",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(706.0, 330.0, image=entry_image_6)
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 10),
        show="*",
    )
    entry_6.place(x=534.0, y=316.0, width=344.0, height=26.0)

    canvas.create_text(
        527.0,
        301.0,
        anchor="nw",
        text="PASSWORD",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(705.0, 388.5, image=entry_image_7)
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 10),
        show="*",
    )
    entry_7.place(x=534.5, y=373.0, width=341.0, height=29.0)

    canvas.create_text(
        524.0,
        357.0,
        anchor="nw",
        text="CONFIRM PASSWORD",
        fill="#000000",
        font=("Inter Light", 11 * -1),
    )

    canvas.create_text(
        508.0,
        86.0,
        anchor="nw",
        text="Fill in the information below ",
        fill="#000000",
        font=("Inter Light", 20 * -1),
    )

    canvas.create_text(
        93.0,
        20.0,
        anchor="nw",
        text="Staff Registration",
        fill="#232121",
        font=("Inter Bold", 43 * -1),
    )

    canvas.create_rectangle(92.0, 85.0, 472.0, 86.0, fill="#232121", outline="")

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_register = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(),
        relief="flat",
    )
    button_register.place(
        x=520.0, y=430.0, width=148.34683227539062, height=50.927032470703125
    )

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_back = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, startwindow),
        relief="flat",
    )
    button_back.place(x=14.0, y=20.0, width=59.0, height=59.0)

    window.mainloop()


def stafflogin(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"green_assets\frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def check_login():
        if entry_2.get() == "":
            messagebox.showerror("Alert", "Please enter your username")
        elif entry_1.get() == "":
            messagebox.showerror("Alert", "Please enter your password")
        else:
            global usernamel
            usernamel = entry_2.get()
            passwordl = entry_1.get()

            conn = None
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password=get_creds(),
                    db="cs_survey",
                )

            except Exception as ex:
                print("PROBLEM WITH Database Connection", ex)
            else:
                print("Database Connection SUCCESS")

            # STEP 3 - CHECK Connection is Establish or not
            if conn is not None:
                # STEP 4 Create Query
                query = "select * from Employees where password=%s and username=%s"

                try:
                    # STEP 6 - CREATE cursor Object
                    cursor = conn.cursor()

                    # STEP 7 - EXECUTE THE Query
                    cursor.execute(query, (passwordl, usernamel))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Alert", "Incorrect username or password")
                        return
                    else:
                        messagebox.showinfo("Success", "Login Successful")
                        navigate(window, staffprofile)

                        entry_2.delete(0, END)
                        entry_1.delete(0, END)

                except Exception as e:
                    print("INSERT PROBLEM ", e)
                finally:
                    conn.close()

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    backbutton = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, startwindow),
        relief="flat",
    )
    backbutton.place(x=13.0, y=11.0, width=59.0, height=59.0)

    canvas.create_rectangle(121.0, 0.0, 1185.0, 540.0, fill="#D9D9D9", outline="")

    canvas.create_rectangle(265.0, 78.0, 913.0, 461.0, fill="#F1F1F1", outline="")

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    toStaffProfile = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: check_login(),
        relief="flat",
    )
    toStaffProfile.place(x=282.0, y=301.0, width=613.0, height=59.11640167236328)

    canvas.create_text(
        293.0,
        223.0,
        anchor="nw",
        text="USERNAME",
        fill="#000000",
        font=("Inter Light", 12 * -1),
    )

    canvas.create_text(
        608.0,
        220.0,
        anchor="nw",
        text="PASSWORD",
        fill="#000000",
        font=("Inter Light", 12 * -1),
    )

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(748.0, 264.5, image=entry_image_1)
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 10),
        show="*",
    )
    entry_1.place(x=601.0, y=245.0, width=294.0, height=37.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(429.0, 264.5, image=entry_image_2)
    entry_2 = Entry(
        bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=("Inter", 10)
    )
    entry_2.place(x=282.0, y=245.0, width=294.0, height=37.0)

    canvas.create_text(
        367.0,
        184.0,
        anchor="nw",
        text="FILL THE INFORMATION TO LOG IN TO YOUR ACCOUNT",
        fill="#000000",
        font=("Inter Light", 16 * -1),
    )

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    registernowbutton = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, staffregistration),
        relief="flat",
    )
    registernowbutton.place(x=458.0, y=378.0, width=43.0, height=20.0)

    canvas.create_text(
        293.0,
        379.0,
        anchor="nw",
        text="*Not Registered? Click",
        fill="#000000",
        font=("Inter Light", 16 * -1),
    )

    canvas.create_text(
        506.0,
        379.0,
        anchor="nw",
        text="To Register",
        fill="#000000",
        font=("Inter Light", 16 * -1),
    )

    canvas.create_text(
        499.0,
        141.0,
        anchor="nw",
        text="STAFF LOG IN",
        fill="#000000",
        font=("Inter Bold", 24 * -1),
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(579.0, 82.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(579.0, 77.0, image=image_image_2)

    window.mainloop()


def staffprofile(window, canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"green_assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def display_info():
        conn = None
        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password=get_creds(),
                db="cs_survey",
            )

        except Exception as ex:
            print("PROBLEM WITH Database Connection", ex)
        else:
            print("Database Connection SUCCESS")

        # STEP 3 - CHECK Connection is Establish or not
        if conn is not None:
            # STEP 4 Create Query
            fnquery = "select FirstName from Employees where Username=%s"
            lnquery = "select LastName from Employees where Username=%s"
            gdquery = "select Gender from Employees where Username=%s"
            psquery = "select Position from Employees where Username=%s"
            unquery = "select Username from Employees where Username=%s"

            try:
                # STEP 6 - CREATE cursor Object
                cursor = conn.cursor()

                # STEP 7 - EXECUTE THE Query
                cursor.execute(fnquery, usernamel)
                global fn
                fn = cursor.fetchone()
                print(fn)

                cursor.execute(lnquery, usernamel)
                global ln
                ln = cursor.fetchone()
                print(ln)

                cursor.execute(gdquery, usernamel)
                global gd
                gd = cursor.fetchone()
                print(gd)

                cursor.execute(psquery, usernamel)
                global ps
                ps = cursor.fetchone()
                print(ps)

                cursor.execute(unquery, usernamel)
                global un
                un = cursor.fetchone()
                print(un)

            except Exception as e:
                print("INSERT PROBLEM ", e)
            finally:
                conn.close()

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(49.0, 265.0, image=image_image_1)

    display_info()

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat",
    )
    button_1.place(x=29.0, y=192.5, width=40.0, height=40.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_customer = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, customers_page),
        relief="flat",
    )
    button_customer.place(x=29.0, y=245.5, width=40.0, height=40.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_table = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, tables_page),
        relief="flat",
    )
    button_table.place(x=29.0, y=298.5, width=40.0, height=40.0)

    canvas.create_rectangle(114.0, 307.0, 793.0, 450.0, fill="#D9D9D9", outline="")

    canvas.create_text(
        135.0,
        385.0,
        anchor="nw",
        text="Gender: ",
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        135.0,
        414.0,
        anchor="nw",
        text="Position: ",
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        135.0,
        356.0,
        anchor="nw",
        text="Last Name: ",
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        135.0,
        327.0,
        anchor="nw",
        text="First Name: ",
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        250.0,
        328.0,
        anchor="nw",
        text=fn,
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        250.0,
        356.0,
        anchor="nw",
        text=ln,
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        250.0,
        385.0,
        anchor="nw",
        text=gd,
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        250.0,
        414.0,
        anchor="nw",
        text=ps,
        fill="#000000",
        font=("Inter Medium", 16 * -1),
    )

    canvas.create_text(
        118.0,
        187.0,
        anchor="nw",
        text=un,
        fill="#000000",
        font=("Inter Medium", 50 * -1),
    )

    canvas.create_text(
        118.0,
        266.0,
        anchor="nw",
        text="Basic Information",
        fill="#000000",
        font=("Inter Medium", 24 * -1),
    )

    canvas.create_text(
        118.0,
        146.0,
        anchor="nw",
        text="Welcome Back!",
        fill="#232121",
        font=("Inter Medium", 24 * -1),
    )

    canvas.create_text(
        118.0,
        67.0,
        anchor="nw",
        text="Staff Profile",
        fill="#232121",
        font=("Inter Bold", 36 * -1),
    )

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_switch = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, stafflogin),
        relief="flat",
    )
    button_switch.place(x=635.0, y=70.0, width=158.0, height=41.0)

    canvas.create_rectangle(
        117.0, 123.00000005508787, 794.9999839536031, 126.0, fill="#232121", outline=""
    )

    window.mainloop()
