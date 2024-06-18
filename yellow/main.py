from pages import customers
from functions import create_canvas, create_window


def main():
    window = create_window()
    canvas = create_canvas(window)
    window.resizable(False, False)
    customers(window, canvas)


main()
