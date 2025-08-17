import tkinter as tk
from tkinter import ttk, PhotoImage


# --- Price Calculator Function ---
def calculate_cost(recliners, bunks):
    price_per_recliner = 25
    price_per_bunk = 50

    total_recliners = recliners * price_per_recliner
    total_bunks = bunks * price_per_bunk
    total_cost = total_bunks + total_recliners

    gst_portion = total_cost - (total_cost / 1.15)
    gst_portion = round(gst_portion, 2)

    return total_cost, gst_portion


# --- Booking Preview Page ---
class BookingPreview(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.booking_data = None

        # Style setup
        style = ttk.Style()
        style.theme_use("clam")

        # Colours
        self.background_colour = "#1a5c97"
        text_color_gold = "#d59e34"
        entry_background = "#a9b7c6"
        button_background_gold = "#d59e34"
        button_text_color = "black"

        # Styling
        style.configure("TFrame", background=self.background_colour)
        style.configure("TLabel", background=self.background_colour,
                        foreground=text_color_gold, font=("Palatino", 15, "bold"))
        style.configure("TButton",
                        font=("Palatino", 12, "bold"),
                        foreground=button_text_color,
                        background=button_background_gold,
                        padding=[20, 10],
                        relief="solid",
                        borderwidth=3,
                        focuscolor="#f4cd83")

        # Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self, padding="20", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)

        # Logo
        try:
            self.logo_image = PhotoImage(file="logo.png")
        except Exception as e:
            print("Logo image not found or failed to load:", e)
            self.logo_image = None
        if self.logo_image:
            self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=self.background_colour)
            self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        current_row = 1

        # Title
        self.heading = ttk.Label(self.main_frame, text="BOOKING PREVIEW",
                                 font=("Palatino", 25, "bold", "underline"), anchor="center")
        self.heading.grid(row=current_row, column=0, pady=(0, 30))
        current_row += 2

        # Dummy booking data (replace later with self.controller.booking_data)
        dummy_data = {
            "name": "Charlize",
            "email": "24548@tgs.school.nz",
            "phone": "+64210111888",
            "route": "One way to AKL to PMR",
            "recliners": 2,
            "bunks": 2
        }

        total_cost, gst_portion = calculate_cost(dummy_data["recliners"], dummy_data["bunks"])

        # Display booking info
        booking_lines = [
            f"Name: {dummy_data['name']}",
            f"Email: {dummy_data['email']}",
            f"Phone: {dummy_data['phone']}",
            f"Route Selected: {dummy_data['route']}",
            f"Recliner Seats: {dummy_data['recliners']}",
            f"Bunk Seats: {dummy_data['bunks']}",
            f"Total Cost: ${total_cost:.2f} NZD",
            f"GST Portion: ${gst_portion:.2f} NZD"
        ]

        for line in booking_lines:
            label = ttk.Label(self.main_frame, text=line, anchor="center", justify="center")
            label.grid(row=current_row, column=0, pady=10)
            current_row += 1


        # Button Frame
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=current_row, column=0, pady=98)

        edit_button = ttk.Button(button_frame, text="EDIT", command=self.edit_booking)
        edit_button.grid(row=0, column=0, padx=10)

        confirm_button = ttk.Button(button_frame, text="CONFIRM", command=self.confirm_booking)
        confirm_button.grid(row=0, column=1, padx=10)

    def edit_booking(self):
        print("Edit button pressed - return to input page (not implemented yet)")

    def confirm_booking(self):
        print("Booking confirmed - submit or write to file (not implemented yet)")


# --- Main App Controller ---
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
        self.booking_data = {}  # shared dictionary

        for F in (BookingPreview,):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("BookingPreview")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# --- Run the App ---
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
