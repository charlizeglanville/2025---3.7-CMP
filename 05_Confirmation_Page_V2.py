import tkinter as tk
from tkinter import ttk, PhotoImage
import re


# Styling for Header that is Shared
class BasePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # GUI Colours
        self.background_colour = "#1a5c97"
        self.text_color_gold = "#d59e34"
        self.entry_background = "#a9b7c6"
        self.button_background_gold = "#d59e34"
        self.button_text_color = "black"

        # Button, Text Stylings
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=self.background_colour)
        style.configure("TLabel", background=self.background_colour,
                        foreground=self.text_color_gold, font=("Palatino", 15, "bold"))
        style.configure("TEntry", foreground="black", fieldbackground=self.entry_background)
        style.configure("Error.TEntry", foreground="red")
        style.configure("Error.TLabel", background=self.background_colour,
                        foreground="#FF7F7F", font=("Palatino", 12, "italic"))
        style.configure("TButton",
                        font=("Palatino", 12, "bold"),
                        foreground=self.button_text_color,
                        background=self.button_background_gold,
                        padding=[20, 10],
                        relief="solid",
                        borderwidth=3,
                        focuscolor="#f4cd83")

        # General Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self, padding="20", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)

        # Logo Placement
        try:
            self.logo_image = PhotoImage(file="logo.png")
        except Exception:
            self.logo_image = None
        if self.logo_image:
            self.img_label = tk.Label(self.main_frame, image=self.logo_image, bg=self.background_colour)
            self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        self.current_row = 1  # Start after logo


class ConfirmationPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Title
        self.heading = ttk.Label(
            self.main_frame,
            text="CONFIRMATION",
            font=("Palatino", 25, "bold", "underline"),
            anchor="center"
        )
        self.heading.grid(row=self.current_row, column=0, pady=(0, 30))
        self.current_row += 1

        # Spacer
        self.main_frame.grid_rowconfigure(self.current_row, weight=1)
        self.current_row += 1

        # Booking Successful message
        booking_label = ttk.Label(
            self.main_frame,
            text="Booking Successful!",
            font=("Palatino", 20, "bold"),
            foreground=self.text_color_gold
        )
        booking_label.grid(row=self.current_row, column=0, pady=(0, 40), sticky="n")
        self.current_row += 1

        # Safe Trip message
        safe_trip_label = ttk.Label(
            self.main_frame,
            text="Have a Safe Trip :)",
            font=("Palatino", 18, "bold"),
            foreground=self.text_color_gold
        )
        safe_trip_label.grid(row=self.current_row, column=0, pady=(0, 40), sticky="n")
        self.current_row += 1

        # Stretchable bottom spacer to push buttons near the bottom
        self.main_frame.rowconfigure(self.current_row, weight=1)
        self.current_row += 1

        # Buttons frame
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=self.current_row, column=0, pady=(20, 40))

        another_booking_btn = ttk.Button(
            button_frame,
            text="ANOTHER BOOKING?",
            command=lambda: controller.show_frame("ClientInfo")
        )
        another_booking_btn.grid(row=0, column=0, padx=15)

        booking_summary_btn = ttk.Button(
            button_frame,
            text="BOOKING SUMMARY",
            command=lambda: controller.show_frame("BookingSummary")
        )
        booking_summary_btn.grid(row=0, column=1, padx=15)

        # Make columns stretch horizontally so everything stays centered
        self.main_frame.columnconfigure(0, weight=1)


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Massey Overnighter")
        self.geometry("600x800")
        self.configure(bg="#1a5c97")

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.booking_data = {}

        # For now, we only have ConfirmationPage
        for F in (ConfirmationPage,):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ConfirmationPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if hasattr(frame, "update_preview"):
            frame.update_preview()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
