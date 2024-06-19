from pathlib import Path
from tkinter import Button, PhotoImage, Tk

from customer_info import customer_info
from functions import overlay

custom_path = Path(__file__).parent / "assets" / "custom"


def relative_to_assets(file):
    return custom_path / file

# TODO: use classes

background_image = PhotoImage(file=relative_to_assets("background_card_image.png"))
person_icon_image = PhotoImage(file=relative_to_assets("person_image.png"))
phone_icon_image = PhotoImage(file=relative_to_assets("phone_image.png"))
more_info_button_image = PhotoImage(file=relative_to_assets("more_info_button.png"))

def create_card(pos, window, canvas):
    window = window
    background_x = 510
    background_y = 227 + (106 * pos)

    background = canvas.create_image(background_x, background_y, image=background_image)

    person_icon_x = background_x - 368.0
    person_icon_y = background_y - 26.0
    person_icon = canvas.create_image(
        person_icon_x, person_icon_y, image=person_icon_image
    )

    phone_icon_x = background_x - 366.0
    phone_icon_y = background_y
    phone_icon = canvas.create_image(phone_icon_x, phone_icon_y, image=phone_icon_image)

    name_x = background_x - 348.0
    name_y = background_y - 32.5
    name = canvas.create_text(
        name_x,
        name_y,
        anchor="nw",
        text="Name",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    phone_number_x = background_x - 348.0
    phone_number_y = background_y - 6.5
    phone_number = canvas.create_text(
        phone_number_x,
        phone_number_y,
        anchor="nw",
        text="023 123 222",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    status_x = background_x - 374.0
    status_y = background_y + 18.5
    status = canvas.create_text(
        status_x,
        status_y,
        anchor="nw",
        text="Checked Out",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    more_info_button_x = background_x + 251.0
    more_info_button_y = background_y - 14.0
    more_info_button = Button(
        image=more_info_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: overlay(window, customer_info),
        relief="flat",
    )
    more_info_button.place(
        x=more_info_button_x, y=more_info_button_y, width=125.0, height=29.0
    )
