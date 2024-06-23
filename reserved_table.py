from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

from sql_integration import cancle_reservation, check_in


def reserved_table(window: Tk, status, endTime, reservedBy, capacity, tableID):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"yellow_assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window_width = 960
    window_height = 540

    overlay_x = (window_width - 609) / 2
    overlay_y = (window_height - 337) / 2

    canvas = Canvas(
        window,
        bg="#fbfbfb",
        height=window_height,
        width=window_width,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(48.0, 47.119384765625, image=image_image_1)

    canvas.create_text(
        66.0,
        41.0,
        anchor="nw",
        text=f"No. {tableID}",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(48.0, 82.0, image=image_image_2)

    canvas.create_text(
        66.0,
        75.0,
        anchor="nw",
        text=f"{capacity}",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        108.0,
        anchor="nw",
        text=f"Status: {status}",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        141.0,
        anchor="nw",
        text=f"Reserved by: {reservedBy}",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        174.0,
        anchor="nw",
        text=f"Until: {endTime}",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    def close_overlay():
        canvas.destroy()
        x_button.destroy()
        button_1.destroy()
        button_2.destroy()

    x_button_image = PhotoImage(file=relative_to_assets("Framexicon.png"))
    x_button = Button(
        image=x_button_image,
        borderwidth=0,
        background="#fbfbfb",
        highlightthickness=0,
        command=lambda: close_overlay(),
        relief="flat",
    )
    x_button.place(x=904, y=36, width=24, height=24)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_overlay_after(check_in(tableID)),
        relief="flat",
    )
    button_1.place(
        x=overlay_x + 112.0, y=overlay_y + 268.0 + 100, width=173.0, height=29.0
    )

    def close_overlay_after(x):
        x
        close_overlay()

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_overlay_after(cancle_reservation(tableID)),
        relief="flat",
    )
    button_2.place(
        x=overlay_x + 324.0, y=overlay_y + 268.0 + 100, width=173.0, height=29.0
    )
    window.mainloop()
