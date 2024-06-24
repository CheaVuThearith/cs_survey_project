from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

from sql_integration import check_out


def occupied_table(window: Tk, tableID, capacity, status, reservedBy, endTime):
    window_width = 960
    window_height = 540

    overlay_x = (window_width - 609) / 2
    overlay_y = (window_height - 337) / 2

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"yellow_assets/frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg="#fbfbfb",
        height=window_height,
        width=window_width,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    def check_out_close():
        check_out(tableID, float(entry_1.get()))
        close_overlay()

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: check_out_close(),
        relief="flat",
    )
    button_1.place(
        x=324.0 + overlay_x, y=268.0 + 100 + overlay_y, width=125.0, height=29.0
    )

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
        text=f"Status: {status} ",
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
        entry_1.destroy()

    x_button_image = PhotoImage(file=relative_to_assets("Framexicon.png"))
    x_button = Button(
        image=x_button_image,
        borderwidth=0,
        background="#fbfbfb",
        highlightthickness=0,
        command=lambda: close_overlay(),
        relief="flat",
    )
    x_button.place(x=904, y=30, width=24, height=24)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        222.0 + overlay_x, 282.0 + overlay_y + 100, image=image_image_3
    )

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(226.0, 282.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
    entry_1.place(
        x=204.0 + overlay_x, y=273.0 + overlay_y + 100, width=44.0, height=17.0
    )
    window.mainloop()
