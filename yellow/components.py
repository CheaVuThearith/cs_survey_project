from pathlib import Path
import string
from tkinter import Button, PhotoImage, Tk
from typing import Literal
from customer_info import customer_info
from functions import overlay

custom_path = Path(__file__).parent / "assets" / "info_card"


def relative_to_assets(file):
    return custom_path / file


CardType = Literal["customer", "table"]


class info_card:
    def __init__(
        self, pos, top_text, bottom_text, status, window, canvas, type: CardType
    ) -> None:
        self.background_image = PhotoImage(
            file=relative_to_assets("background_card_image.png")
        )
        self.top_image = (
            PhotoImage(file=relative_to_assets("person_image.png"))
            if type == "customer"
            else PhotoImage(file=relative_to_assets("table_image.png"))
        )
        self.bottom_image = (
            PhotoImage(file=relative_to_assets("phone_image.png"))
            if type == "customer"
            else PhotoImage(file=relative_to_assets("multiple_people_image.png"))
        )
        self.more_info_button_image = PhotoImage(
            file=relative_to_assets("more_info_button.png")
        )
        self.pos = pos
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.status = status
        self.window = window
        self.canvas = canvas

    def create_card(self):
        background_x = 510
        background_y = 227 + (106 * self.pos)

        background = self.canvas.create_image(
            background_x, background_y, image=self.background_image
        )

        person_icon_x = background_x - 368.0
        person_icon_y = background_y - 26.0
        person_icon = self.canvas.create_image(
            person_icon_x, person_icon_y, image=self.top_image
        )

        phone_icon_x = background_x - 368.0
        phone_icon_y = background_y
        phone_icon = self.canvas.create_image(
            phone_icon_x, phone_icon_y, image=self.bottom_image
        )

        name_x = background_x - 348.0
        name_y = background_y - 32.5
        name = self.canvas.create_text(
            name_x,
            name_y,
            anchor="nw",
            text=self.top_text,
            fill="#232121",
            font=("Inter", 12 * -1),
        )

        phone_number_x = background_x - 348.0
        phone_number_y = background_y - 6.5
        phone_number = self.canvas.create_text(
            phone_number_x,
            phone_number_y,
            anchor="nw",
            text=self.bottom_text,
            fill="#232121",
            font=("Inter", 12 * -1),
        )

        status_x = background_x - 374.0
        status_y = background_y + 18.5
        status = self.canvas.create_text(
            status_x,
            status_y,
            anchor="nw",
            text=self.status,
            fill="#232121",
            font=("Inter", 12 * -1),
        )

        more_info_button_x = background_x + 251.0
        more_info_button_y = background_y - 14.0
        more_info_button = Button(
            image=self.more_info_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: overlay(self.window, customer_info),
            relief="flat",
        )
        more_info_button.place(
            x=more_info_button_x, y=more_info_button_y, width=125.0, height=29.0
        )
