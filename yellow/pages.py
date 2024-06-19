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
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\info_page")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window.geometry("960x540")
    window.configure(bg="#F1F1F1")

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(49.0, 265.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
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
        delete_cards(cards_list)
        page = (
            max(current_page - 1, 1)
            if backwards
            else min(
                current_page + 1,
                math.ceil(
                    len(get_data("Tables", limit=100, page=1, where="TableID")) / 3
                ),
            )
        )
        cards_list = make_cards_tables(window, canvas, page, where="TableID")
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
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\info_page")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window.geometry("960x540")
    window.configure(bg="#F1F1F1")

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(49.0, 265.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
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
        where = f"CustomerID LIKE '%{search}%' or Name LIKE '%{search}%' or PhoneNumber LIKE '%{search}%' or Status LIKE '%{search}%' or TimesCanceled LIKE '%{search}%' or AmountSpent LIKE '%{search}%'"
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
        delete_cards(cards_list)
        page = (
            max(current_page - 1, 1)
            if backwards
            else min(
                current_page + 1,
                math.ceil(len(get_data("Customers", limit=100, page=1, where="CustomerID")) / 3),
            )
        )
        cards_list = make_cards_customers(window, canvas, page, where="CustomerID")
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
