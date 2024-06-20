from pages import customers_page
from page_navigation import create_canvas, create_window

def main():
    window = create_window()
    canvas = create_canvas(window)
    window.resizable(False, False)
    customers_page(window, canvas)


main()
