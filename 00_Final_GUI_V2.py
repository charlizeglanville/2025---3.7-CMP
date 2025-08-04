import tkinter as tk
from tkinter import ttk, PhotoImage, StringVar, Radiobutton
import re


class ClientInfo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.booking_data = None
        self.controller = controller

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
        style.configure("TEntry", foreground="black", fieldbackground=entry_background)
        style.configure("Error.TEntry", foreground="red")
        style.configure("Error.TLabel", background=self.background_colour,
                        foreground="#FF7F7F", font=("Palatino", 12, "italic"))

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

        # Logo at row 0
        self.logo_image = PhotoImage(file="logo.png")
        self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=self.background_colour)
        self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        current_row = 1

        # Title row
        self.heading = ttk.Label(self.main_frame, text="THE MASSEY OVERNIGHTER",
                                 font=("Palatino", 25, "bold", "underline"), anchor="center")
        self.heading.grid(row=current_row, column=0, pady=(0, 30))
        current_row += 1

        # Spacer after title for balanced vertical spacing
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Name Section
        self.name_label = ttk.Label(self.main_frame, text="Name:")
        self.name_label.grid(row=current_row, column=0, sticky="w")
        current_row += 1
        self.name_entry = ttk.Entry(self.main_frame, width=40)
        self.name_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6)
        current_row += 1
        self.name_error = ttk.Label(self.main_frame, text="", style="Error.TLabel")
        self.name_error.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        # Spacer between Name and Phone
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Phone Section
        self.phone_label = ttk.Label(self.main_frame, text="Phone:")
        self.phone_label.grid(row=current_row, column=0, sticky="w")
        current_row += 1
        self.phone_entry = ttk.Entry(self.main_frame, width=40)
        self.phone_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6)
        self.phone_entry.insert(0, "(+64)")
        current_row += 1
        self.phone_error = ttk.Label(self.main_frame, text="", style="Error.TLabel")
        self.phone_error.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        # Spacer between Phone and Email
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Email Section
        self.email_label = ttk.Label(self.main_frame, text="Email:")
        self.email_label.grid(row=current_row, column=0, sticky="w")
        current_row += 1
        self.email_entry = ttk.Entry(self.main_frame, width=40)
        self.email_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6)
        current_row += 1
        self.email_error = ttk.Label(self.main_frame, text="", style="Error.TLabel")
        self.email_error.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        # Spacer before button frame
        self.main_frame.grid_rowconfigure(current_row, weight=1)

        # Button Frame
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=current_row, column=0,
                          pady=40)

        # Configure button_frame columns so buttons can expand
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.summary_button = ttk.Button(button_frame, text="BOOKING SUMMARY", command=self.show_summary)
        self.summary_button.grid(row=0, column=0, padx=(0, 20), sticky="ew")

        self.next_button = ttk.Button(button_frame, text="NEXT", command=self.validate_fields)
        self.next_button.grid(row=0, column=1, padx=(0, 20), sticky="ew")

        # Bottom spacer row pushes content up
        self.main_frame.grid_rowconfigure(current_row, weight=3)

    def validate_fields(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Reset styles and error texts
        self.name_entry.configure(style="TEntry")
        self.phone_entry.configure(style="TEntry")
        self.email_entry.configure(style="TEntry")
        self.name_error.config(text="")
        self.phone_error.config(text="")
        self.email_error.config(text="")

        valid = True

        if not name.strip() or any(char.isdigit() for char in name):
            self.name_entry.configure(style="Error.TEntry")
            self.name_error.config(text="Name must not be blank or contain numbers.")
            valid = False

        #    def validate_fields(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Reset styles
        self.name_entry.configure(style="TEntry")
        self.phone_entry.configure(style="TEntry")
        self.email_entry.configure(style="TEntry")
        self.name_error.config(text="")
        self.phone_error.config(text="")
        self.email_error.config(text="")

        valid = True

        if not name.strip() or any(char.isdigit() for char in name):
            self.name_entry.configure(style="Error.TEntry")
            self.name_error.config(text="Name must not be blank or contain numbers.")
            valid = False

        # Extract only the part after the prefill "(+64)"
        user_part = self.phone_entry.get().replace("(+64)", "").strip()
        stripped_phone = re.sub(r'\D', '', user_part)

        if not (7 <= len(stripped_phone) <= 10):
            self.phone_entry.configure(style="Error.TEntry")
            self.phone_error.config(text="Phone must be 7–10 digits (excluding (+64)).")
            valid = False

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            self.email_entry.configure(style="Error.TEntry")
            self.email_error.config(text="Please enter a valid email address.")
            valid = False

        if valid:
            full_phone = "+64" + stripped_phone
            self.booking_data = {
                "name": name,
                "phone": full_phone,
                "email": email
            }
            print("\n---Saved Client Info---")
            print(f"Name: {name}")
            print(f"Phone: {full_phone}")
            print(f"Email: {email}")
            print("\n---Info Has Been Saved---")

            # Save name, phone, email in dictionary
            self.controller.booking_data["name"] = name
            self.controller.booking_data["phone"] = full_phone
            self.controller.booking_data["email"] = email

            # Move to next page
            self.controller.show_frame("SeatSelection")

    def show_summary(self):
        data = self.controller.booking_data
        if not data:
            return

        top = tk.Toplevel()
        top.title("Booking Summary")
        top.geometry("300x250")

        ttk.Label(top, text=f"Name: {data.get('name', '')}").pack(pady=3)
        ttk.Label(top, text=f"Phone: {data.get('phone', '')}").pack(pady=3)
        ttk.Label(top, text=f"Email: {data.get('email', '')}").pack(pady=3)
        ttk.Label(top, text=f"Route: {data.get('route', 'Not selected')}").pack(pady=3)
        ttk.Label(top, text=f"Recliners: {data.get('recliners', '0')}").pack(pady=3)
        ttk.Label(top, text=f"Bunks: {data.get('bunks', '0')}").pack(pady=3)

        ttk.Button(top, text="Close", command=top.destroy).pack(pady=10)


class SeatSelection(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Parameters for Routes
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
        style.configure("TEntry", fieldbackground=entry_background, foreground="black")
        style.configure("Error.TEntry", foreground="red")
        style.configure("Error.TLabel", background=self.background_colour,
                        foreground="#FF7F7F", font=("Palatino", 12, "italic"))

        style.configure("TButton", font=("Palatino", 12, "bold"),
                        foreground=button_text_color,
                        background=button_background_gold,
                        padding=[20, 10],
                        relief="solid", borderwidth=3)

        # Layout --> To Match client information page
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self, padding="20", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)

        # logo row 0
        self.logo_image = PhotoImage(file="logo.png")
        self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=self.background_colour)
        self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        # title row 1
        self.title_label = ttk.Label(self.main_frame, text="ROUTE SELECTION",
                                     font=("Palatino", 25, "bold", "underline"))
        self.title_label.grid(row=1, column=0, pady=(0, 20))

        # content starts
        current_row = 2

        # Setting for radio buttons
        self.route_var = StringVar(value="2")
        self.routes = {
            "1": "One Way from PMR to AKL",
            "2": "One Way from AKL to PMR",
            "3": "Return (AKL to PMR to AKL)"
        }

        # Styling for the radio buttons
        for value, text in self.routes.items():
            rb = Radiobutton(self.main_frame, text=text, variable=self.route_var, value=value,
                             font=("Palatino", 16), bg=self.background_colour,
                             fg=text_color_gold, activebackground=self.background_colour,
                             selectcolor=self.background_colour,
                             highlightthickness=0, anchor="w", padx=20,
                             command=self.update_availability_label)
            rb.grid(row=current_row, column=0, sticky="w", pady=2)
            current_row += 1

        # Select Seats Title
        self.select_label = ttk.Label(self.main_frame, text="\nSelect Seats",
                                      font=("Palatino", 25, "bold", "underline"))
        self.select_label.grid(row=current_row, column=0)
        current_row += 1

        self.avail_label = ttk.Label(self.main_frame, text="", style="TLabel")
        self.avail_label.grid(row=current_row, column=0, pady=10)
        current_row += 1

        # Recliner Seat Label & title
        self.recliner_label = ttk.Label(self.main_frame, text="Recliner Seats")
        self.recliner_label.grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        self.recliner_entry = ttk.Entry(self.main_frame, style="TEntry")
        self.recliner_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6, padx=20)
        current_row += 2

        ttk.Label(self.main_frame, text="Max. 20").grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        # spacer
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Bunk Seat label & title
        self.bunk_label = ttk.Label(self.main_frame, text="Bunk Seats")
        self.bunk_label.grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        self.bunk_entry = ttk.Entry(self.main_frame, style="TEntry")
        self.bunk_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6, padx=20)
        current_row += 2

        ttk.Label(self.main_frame, text="Max. 15").grid(row=current_row, column=0, sticky="w", padx=20)
        current_row += 1

        # Spacer pushes the button down
        self.main_frame.rowconfigure(current_row, weight=1)
        current_row += 1

        # NEXT button
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=current_row, column=0, pady=(20, 10), sticky="ew")
        button_frame.columnconfigure(0, weight=1)

        self.next_button = ttk.Button(button_frame, text="NEXT", command=self.submit_selection)
        self.next_button.grid(row=0, column=0, sticky="ew", padx=150)

        self.update_availability_label()

    # Resets the styles to their normal state
    def clear_error_styles(self):
        self.avail_label.configure(style="TLabel", text=self.get_availability_text())
        self.recliner_entry.configure(style="TEntry")
        self.bunk_entry.configure(style="TEntry")

    # In Charge of presenting what seats are available depending on route
    def get_availability_text(self):
        route = self.route_var.get()
        seats = self.route_seats[route]
        return (f"Available Recliners: {seats['recliners']}\n"
                f"Available Bunks: {seats['bunks']}")

    # Updates the seat availability label to current availability
    def update_availability_label(self):
        self.clear_error_styles()

    def submit_selection(self):
        self.clear_error_styles()

        route = self.route_var.get()
        seats = self.route_seats[route]

        # Insures user doesn't put a decimal
        try:
            recliners = int(self.recliner_entry.get())
            bunks = int(self.bunk_entry.get())
        except ValueError:
            self.avail_label.configure(text="Invalid input: Please enter whole numbers.", style="Error.TLabel")
            self.recliner_entry.configure(style="Error.TEntry")
            self.bunk_entry.configure(style="Error.TEntry")
            return

        # The seat selection process cannot allow negative number
        if recliners < 0 or bunks < 0:
            self.avail_label.configure(text="Invalid input: No negative values allowed.", style="Error.TLabel")
            if recliners < 0:
                self.recliner_entry.configure(style="Error.TEntry")
            if bunks < 0:
                self.bunk_entry.configure(style="Error.TEntry")
            return

        # If User inputs 0 seats
        if recliners + bunks == 0:
            self.avail_label.configure(text="Invalid input: Must book at least one seat.", style="Error.TLabel")
            self.recliner_entry.configure(style="Error.TEntry")
            self.bunk_entry.configure(style="Error.TEntry")
            return

        # If there are no more seat available on that route
        if recliners > seats['recliners'] or bunks > seats['bunks']:
            self.avail_label.configure(text="Invalid input: Not enough seats available. Try Again :)",
                                       style="Error.TLabel")
            if recliners > seats['recliners']:
                self.recliner_entry.configure(style="Error.TEntry")
            if bunks > seats['bunks']:
                self.bunk_entry.configure(style="Error.TEntry")
            return

        # Saves Route, Recliner, Bunks Booking
        self.controller.booking_data["route"] = self.routes[route]
        self.controller.booking_data["recliners"] = recliners
        self.controller.booking_data["bunks"] = bunks

        # Deduct the booked seats from availability
        self.route_seats[route]["recliners"] -= recliners
        self.route_seats[route]["bunks"] -= bunks

        self.avail_label.configure(text="Booking confirmed!", style="TLabel")
        self.update_availability_label()

        print("Full booking info:", self.controller.booking_data)


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

        # Initialize shared booking_data dictionary
        self.booking_data = {}

        for F in (ClientInfo, SeatSelection):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ClientInfo")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
