from pathlib import Path
from tkinter import Button, Entry, PhotoImage
from functions import navigate, overlay
from customer_info import customer_info


def reservations(window, canvas):
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

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(510.0, 227.0, image=image_image_3)

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(144.0, 200.619384765625, image=image_image_4)

    canvas.create_text(
        162.0, 194.5, anchor="nw", text="No. 1", fill="#232121", font=("Inter", 12 * -1)
    )

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(144.0, 227.5, image=image_image_5)

    canvas.create_text(
        162.0, 220.5, anchor="nw", text="1 - 2", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        136.0,
        245.5,
        anchor="nw",
        text="Vacant",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(510.0, 333.0, image=image_image_6)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat",
    )
    button_4.place(x=761.0, y=319.0, width=125.0, height=29.0)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(144.0, 306.619384765625, image=image_image_7)

    canvas.create_text(
        162.0, 300.5, anchor="nw", text="No. 1", fill="#232121", font=("Inter", 12 * -1)
    )

    image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(144.0, 333.5, image=image_image_8)

    canvas.create_text(
        162.0, 326.5, anchor="nw", text="1 - 2", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        136.0,
        351.5,
        anchor="nw",
        text="Occupied",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(510.0, 439.0, image=image_image_9)

    image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(144.0, 412.619384765625, image=image_image_10)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat",
    )
    button_5.place(x=761.0, y=424.0, width=125.0, height=29.0)

    canvas.create_text(
        162.0, 406.5, anchor="nw", text="No. 1", fill="#232121", font=("Inter", 12 * -1)
    )

    image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(144.0, 439.5, image=image_image_11)

    canvas.create_text(
        162.0, 432.5, anchor="nw", text="1 - 2", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        136.0,
        457.5,
        anchor="nw",
        text="Vacant",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat",
    )
    button_6.place(x=761.0, y=213.0, width=125.0, height=29.0)

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


def customers(window, canvas):
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

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(510.0, 227.0, image=image_image_3)

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(142.0, 201.0, image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(144.0, 227.0, image=image_image_5)

    canvas.create_text(
        162.0, 194.5, anchor="nw", text="Name", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        162.0,
        220.5,
        anchor="nw",
        text="023 123 222",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        136.0,
        245.5,
        anchor="nw",
        text="Checked Out",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: overlay(window, customer_info),
        relief="flat",
    )
    button_4.place(x=761.0, y=213.0, width=125.0, height=29.0)

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(510.0, 333.0, image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(142.0, 307.0, image=image_image_7)

    image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(144.0, 333.0, image=image_image_8)

    canvas.create_text(
        162.0, 300.5, anchor="nw", text="Name", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        162.0,
        326.5,
        anchor="nw",
        text="023 123 222",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        136.0,
        351.5,
        anchor="nw",
        text="Checked Out",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat",
    )
    button_5.place(x=761.0, y=319.0, width=125.0, height=29.0)

    image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(510.0, 439.0, image=image_image_9)

    image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(142.0, 413.0, image=image_image_10)

    image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(144.0, 439.0, image=image_image_11)

    canvas.create_text(
        162.0, 406.5, anchor="nw", text="Name", fill="#232121", font=("Inter", 12 * -1)
    )

    canvas.create_text(
        162.0,
        432.5,
        anchor="nw",
        text="023 123 222",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        136.0,
        457.5,
        anchor="nw",
        text="Checked Out",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat",
    )
    button_6.place(x=761.0, y=425.0, width=125.0, height=29.0)

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
