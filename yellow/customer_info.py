from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


def customer_info(window: Tk):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame5"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window_width = 960
    window_height = 540

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
    image_1 = canvas.create_image(48.0, 119.5, image=image_image_1)

    canvas.create_text(
        63.0,
        112.0,
        anchor="nw",
        text="099 712 872",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(46.0, 86.0, image=image_image_2)

    canvas.create_text(
        60.12841796875,
        79.0,
        anchor="nw",
        text="Name",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        145.5,
        anchor="nw",
        text="Status:  Reserved",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        178.5,
        anchor="nw",
        text="Times Visited: 0  ",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        211.5,
        anchor="nw",
        text="Times Canceled: ",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    canvas.create_text(
        40.0,
        244.5,
        anchor="nw",
        text="Amount Spent: 0",
        fill="#232121",
        font=("Inter", 12 * -1),
    )

    def close_overlay():
        canvas.destroy()
        x_button.destroy()

    x_button_image = PhotoImage(file=relative_to_assets("Framexicon.png"))
    x_button = Button(
        image=x_button_image,
        borderwidth=0,
        background="#fbfbfb",
        highlightthickness=0,
        command=lambda: close_overlay(),
        relief="flat",
    )
    x_button.place(x=904, y=70, width=24, height=24)

    window.mainloop()
