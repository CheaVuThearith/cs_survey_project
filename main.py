from pages import startwindow
from page_navigation import create_canvas, create_window


def main():
    window = create_window()
    canvas = create_canvas(window)
    window.resizable(False, False)
    window.title("Restaurant Management")
    startwindow(window, canvas)


main()
