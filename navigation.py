from tkinter import Canvas, Tk


def create_canvas(window):
    canvas = Canvas(
        window,
        bg="#F1F1F1",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    return canvas


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def create_window():
    window = Tk()
    window.geometry("960x540")
    window.configure(bg="#F1F1F1")
    return window


def navigate(window, destination):
    clear_window(window)
    canvas = create_canvas(window)
    destination(window, canvas)

def overlay(window, destination):
    destination(window)
