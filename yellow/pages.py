from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage
from functions import navigate, overlay
from customer_info import customer_info
from components import info_card
from vacant_table import vacant_table


def reservations(window, canvas: Canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

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

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    navbar_customers = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, customers),
        relief="flat",
    )
    navbar_customers.place(x=29.0, y=245.5, width=40.0, height=40.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat",
    )
    button_3.place(x=29.0, y=298.5, width=40.0, height=40.0)

    canvas.create_text(
        118.0,
        67.0,
        anchor="nw",
        text="Reservations",
        fill="#232121",
        font=("Inter Bold", 36 * -1),
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(656.0, 89.0, image=image_image_2)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(642.0, 89.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
    entry_1.place(x=440.0, y=80.0, width=404.0, height=16.0)

    canvas.create_text(
        118.0,
        143.0,
        anchor="nw",
        text="Total tables - 20",
        fill="#000000",
        font=("Inter", 16 * -1),
    )

    card_0 = info_card(
        type="table",
        status="Checked Out",
        top_text="UserName",
        bottom_text="291 312 322",
        pos=0,
        window=window,
        canvas=canvas,
    )
    card_1 = info_card(
        type="table",
        status="Checked Out",
        top_text="UserToptetop_text",
        bottom_text="291 312 322",
        pos=1,
        window=window,
        canvas=canvas,
    )
    card_2 = info_card(
        type="table",
        status="Checked Ot",
        top_text="UserName",
        bottom_text="291 312 322",
        pos=2,
        window=window,
        canvas=canvas,
    )

    card_0.create_card()
    card_1.create_card()
    card_2.create_card()

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat",
    )
    button_7.place(x=877.0, y=502.0, width=25.0, height=25.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat",
    )
    button_8.place(x=849.0, y=502.0, width=25.0, height=25.0)
    window.mainloop()


def customers(window, canvas: Canvas):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

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

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat",
    )
    button_2.place(x=29.0, y=245.5, width=40.0, height=40.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    navbar_reservations = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate(window, reservations),
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

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(656.0, 89.0, image=image_image_2)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(642.0, 89.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
    entry_1.place(x=440.0, y=80.0, width=404.0, height=16.0)

    canvas.create_text(
        118.0,
        143.0,
        anchor="nw",
        text="Total Customers - 20",
        fill="#000000",
        font=("Inter", 16 * -1),
    )

    card_0 = info_card(
        type="customer",
        status="Checked Out",
        top_text="UserName",
        bottom_text="291 312 322",
        pos=0,
        window=window,
        canvas=canvas,
    )
    card_1 = info_card(
        type="customer",
        status="Checked Out",
        top_text="UserToptetop_text",
        bottom_text="291 312 322",
        pos=1,
        window=window,
        canvas=canvas,
    )
    card_2 = info_card(
        type="customer",
        status="Checked Ot",
        top_text="UserName",
        bottom_text="291 312 322",
        pos=2,
        window=window,
        canvas=canvas,
    )

    card_0.create_card()
    card_1.create_card()
    card_2.create_card()

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    forward_button = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("forward_button clicked"),
        relief="flat",
    )
    forward_button.place(x=877.0, y=502.0, width=25.0, height=25.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    backwards_button = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("backwards_button clicked"),
        relief="flat",
    )
    backwards_button.place(x=849.0, y=502.0, width=25.0, height=25.0)
    window.mainloop()
