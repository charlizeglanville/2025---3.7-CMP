from tkinter import *
from tkinter import ttk

class SeatSelection:
    def __init__(self, parent):
        # Seat availability per route
        self.route_seats = {
            "1": {"recliners": 20, "bunks": 15},
            "2": {"recliners": 20, "bunks": 15},
            "3": {"recliners": 20, "bunks": 15},
        }

        # Colours
        self.background_colour = "#1a5c97"
        text_color_gold = "#d59e34"
        entry_background = "#a9b7c6"
        button_background_gold = "#d59e34"
        button_text_color = "black"

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=self.background_colour)
        style.configure("TLabel", background=self.background_colour,
                        foreground=text_color_gold, font=("Palatino", 15, "bold"))
        style.configure("TEntry", fieldbackground=entry_background)
        style.configure("TButton", font=("Palatino", 12, "bold"),
                        foreground=button_text_color,
                        background=button_background_gold,
                        padding=[20, 10],
                        relief="solid", borderwidth=3)

        # Layout
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(parent, padding="20", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)

        # === TOP LOGO (Row 0) ===
        self.logo_image = PhotoImage(file="logo.png")
        self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=self.background_colour)
        self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        # === TITLE (Row 1) ===
        self.title_label = ttk.Label(self.main_frame, text="ROUTE SELECTION",
                                     font=("Palatino", 25, "bold", "underline"))
        self.title_label.grid(row=1, column=0, pady=(0, 20))

        # === CONTENT STARTS FROM ROW 2 ===
        current_row = 2

        self.route_var = StringVar(value="2")
        self.routes = {
            "1": "One Way to PMR to AKL",
            "2": "One Way to AKL to PMR",
            "3": "Return (AKL to PMR to AKL)"
        }

        for value, text in self.routes.items():
            rb = Radiobutton(self.main_frame, text=text, variable=self.route_var, value=value,
                             font=("Palatino", 13), bg=self.background_colour,
                             fg=text_color_gold, activebackground=self.background_colour,
                             selectcolor=self.background_colour,
                             highlightthickness=0, anchor="w", padx=20,
                             command=self.update_availability_label)
            rb.grid(row=current_row, column=0, sticky="w", pady=2)
            current_row += 1

        self.select_label = ttk.Label(self.main_frame, text="\nSelect Seats", font=("Palatino", 18, "bold", "underline"))
        self.select_label.grid(row=current_row, column=0)
        current_row += 1

        self.avail_label = ttk.Label(self.main_frame, text="")
        self.avail_label.grid(row=current_row, column=0, pady=10)
        current_row += 1

        # Recliner Seat Input
        self.recliner_label = ttk.Label(self.main_frame, text="Recliner Seats")
        self.recliner_label.grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        self.recliner_entry = ttk.Entry(self.main_frame)
        self.recliner_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6, padx=20)
        current_row += 1

        ttk.Label(self.main_frame, text="Max. 20").grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        # Bunk Seat Input
        self.bunk_label = ttk.Label(self.main_frame, text="Bunk Seats")
        self.bunk_label.grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        self.bunk_entry = ttk.Entry(self.main_frame)
        self.bunk_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6, padx=20)
        current_row += 1

        ttk.Label(self.main_frame, text="Max. 15").grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        # Spacer pushes the button down
        self.main_frame.rowconfigure(current_row, weight=1)
        current_row += 1

        # === BOTTOM NEXT BUTTON ===
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=current_row, column=0, pady=(20, 10), sticky="ew")
        button_frame.columnconfigure(0, weight=1)

        self.next_button = ttk.Button(button_frame, text="NEXT", command=self.submit_selection)
        self.next_button.grid(row=0, column=0, sticky="ew", padx=150)

        self.update_availability_label()

    def get_availability_text(self):
        route = self.route_var.get()
        seats = self.route_seats[route]
        return (f"Available Recliners: {seats['recliners']}\n"
                f"Available Bunks: {seats['bunks']}")

    def update_availability_label(self):
        self.avail_label.config(text=self.get_availability_text())

    def submit_selection(self):
        route = self.route_var.get()
        seats = self.route_seats[route]

        try:
            recliners = int(self.recliner_entry.get())
            bunks = int(self.bunk_entry.get())
        except ValueError:
            print("Please enter valid whole numbers.")
            return

        if recliners < 0 or bunks < 0:
            print("No negative values allowed.")
        elif recliners + bunks == 0:
            print("Must book at least one seat.")
        elif recliners > seats['recliners'] or bunks > seats['bunks']:
            print("Not enough seats available.")
        else:
            seats['recliners'] -= recliners
            seats['bunks'] -= bunks
            self.update_availability_label()
            print(f"Booking confirmed on Route {route}: {recliners} recliner(s), {bunks} bunk(s)")
            self.recliner_entry.delete(0, END)
            self.bunk_entry.delete(0, END)

# Run app
if __name__ == "__main__":
    root = Tk()
    root.title("The Massey Overnighter - Seat Selection")
    root.geometry("600x800")
    root.configure(bg="#1a5c97")

    SeatSelection(root)
    root.mainloop()
