import tkinter as tk
from tkinter import ttk, PhotoImage, StringVar, Radiobutton
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
            self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=self.background_colour)
            self.img_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        self.current_row = 1  # Start after logo


# ------- Client Information Page -------
class ClientInfo(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        style = ttk.Style()
        style.theme_use("clam")

        # Grid Set up
        current_row = 1

        # Title
        self.heading = ttk.Label(self.main_frame, text="THE MASSEY OVERNIGHTER",
                                 font=("Palatino", 25, "bold", "underline"), anchor="center")
        self.heading.grid(row=current_row, column=0, pady=(0, 30))
        current_row += 1

        # Spacer
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Name + Input Box
        self.name_label = ttk.Label(self.main_frame, text="Name:")
        self.name_label.grid(row=current_row, column=0, sticky="w")
        current_row += 1
        self.name_entry = ttk.Entry(self.main_frame, width=40)
        self.name_entry.grid(row=current_row, column=0, sticky="ew", pady=5, ipady=6)
        current_row += 1
        self.name_error = ttk.Label(self.main_frame, text="", style="Error.TLabel")
        self.name_error.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        # Spacer
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Phone + Input Box
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

        # Spacer
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

        # Email + Input Box
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

        # So Buttons can expand
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # Booking Summary Button
        self.summary_button = ttk.Button(button_frame, text="BOOKING SUMMARY")
        self.summary_button.grid(row=0, column=0, padx=(0, 20), sticky="ew")

        # Next Button
        self.next_button = ttk.Button(button_frame, text="NEXT", command=self.validate_fields)
        self.next_button.grid(row=0, column=1, padx=(0, 20), sticky="ew")

        # Bottom spacer row pushes content up
        self.main_frame.grid_rowconfigure(current_row, weight=3)

    # Validates Input in Name, Phone, Email Boxes
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

        # Checks Name entered is Valid
        if not name.strip() or any(char.isdigit() for char in name):
            self.name_entry.configure(style="Error.TEntry")
            self.name_error.config(text="Name must not be blank or contain numbers.")
            valid = False

        # Extract only the part after the prefill "(+64)"
        user_part = phone.replace("(+64)", "").strip()
        stripped_phone = re.sub(r'\D', '', user_part)

        # Checks Phone Number entered is a New Zealand Number
        if not (7 <= len(stripped_phone) <= 10):
            self.phone_entry.configure(style="Error.TEntry")
            self.phone_error.config(text="Phone must be 7–10 digits (excluding (+64)).")
            valid = False

        # Checks that the user has put in a valid email by checking for a @ and . after the @
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            self.email_entry.configure(style="Error.TEntry")
            self.email_error.config(text="Please enter a valid email address.")
            valid = False

        # Saves Data
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

            # Move to Seat Selection Page
            self.controller.show_frame("SeatSelection")

    def reset_fields(self):
        # Clear text fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, "(+64)")  # keep placeholder
        self.email_entry.delete(0, tk.END)

        # Clear any error messages
        self.name_error.config(text="")
        self.phone_error.config(text="")
        self.email_error.config(text="")

        # Reset entry styles to default
        self.name_entry.configure(style="TEntry")
        self.phone_entry.configure(style="TEntry")
        self.email_entry.configure(style="TEntry")


# ------- Seat Selection Page --------
class SeatSelection(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        # Parameters for Routes
        self.route_seats = {
            "1": {"recliners": 20, "bunks": 15},
            "2": {"recliners": 20, "bunks": 15},
            "3": {"recliners": 20, "bunks": 15},
        }

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
                             fg=self.text_color_gold, activebackground=self.background_colour,
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
        button_frame.grid(row=current_row, column=0, pady=(40, 80), sticky="ew")
        button_frame.columnconfigure(0, weight=1)

        self.next_button = ttk.Button(button_frame, text="NEXT", command=self.submit_selection)
        self.next_button.grid(row=0, column=0, padx=10)

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

        # Validate recliners and bunks as int
        try:
            recliners = int(self.recliner_entry.get())
            bunks = int(self.bunk_entry.get())
        except ValueError:
            self.avail_label.configure(text="Invalid input: Please enter whole numbers.", style="Error.TLabel")
            self.recliner_entry.configure(style="Error.TEntry")
            self.bunk_entry.configure(style="Error.TEntry")
            return

        if recliners < 0 or bunks < 0:
            self.avail_label.configure(text="Invalid input: No negative values allowed.", style="Error.TLabel")
            if recliners < 0:
                self.recliner_entry.configure(style="Error.TEntry")
            if bunks < 0:
                self.bunk_entry.configure(style="Error.TEntry")
            return

        if recliners + bunks == 0:
            self.avail_label.configure(text="Invalid input: Must book at least one seat.", style="Error.TLabel")
            self.recliner_entry.configure(style="Error.TEntry")
            self.bunk_entry.configure(style="Error.TEntry")
            return

        if recliners > seats['recliners'] or bunks > seats['bunks']:
            self.avail_label.configure(text="Invalid input: Not enough seats available. Try Again :)",
                                       style="Error.TLabel")
            if recliners > seats['recliners']:
                self.recliner_entry.configure(style="Error.TEntry")
            if bunks > seats['bunks']:
                self.bunk_entry.configure(style="Error.TEntry")
            return

        # If validation passes, update booking data and seat availability
        self.controller.booking_data["route"] = self.routes[route]
        self.controller.booking_data["recliners"] = recliners
        self.controller.booking_data["bunks"] = bunks

        self.route_seats[route]["recliners"] -= recliners
        self.route_seats[route]["bunks"] -= bunks

        self.avail_label.configure(text="Booking confirmed!", style="TLabel")
        self.update_availability_label()

        # Move to next page
        self.controller.show_frame("BookingPreview")
        print("Full booking info:", self.controller.booking_data)

    def reset_selection(self):
        # Reset entries
        self.recliner_entry.delete(0, tk.END)
        self.bunk_entry.delete(0, tk.END)

        # Reset route selection to default
        self.route_var.set("2")

        # Reset seat availability to initial values
        self.route_seats = {
            "1": {"recliners": 20, "bunks": 15},
            "2": {"recliners": 20, "bunks": 15},
            "3": {"recliners": 20, "bunks": 15},
        }

        # Update availability label text accordingly
        self.update_availability_label()

        # Clear error styles if any
        self.clear_error_styles()


# Cost calculator
def calculate_cost(recliners, bunks):
    price_per_recliner = 25
    price_per_bunk = 50

    total_recliners = recliners * price_per_recliner
    total_bunks = bunks * price_per_bunk
    total_cost = total_bunks + total_recliners

    gst_portion = total_cost - (total_cost / 1.15)
    gst_portion = round(gst_portion, 2)

    return total_cost, gst_portion


class BookingPreview(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        style = ttk.Style()
        style.theme_use("clam")

        self.current_row = 1
        self.heading = ttk.Label(self.main_frame, text="BOOKING PREVIEW",
                                 font=("Palatino", 25, "bold", "underline"), anchor="center")
        self.heading.grid(row=self.current_row, column=0, pady=(0, 30))
        self.current_row += 1

        self.labels = []  # store widgets so we can destroy later

        # Configure all rows above button to expand
        for r in range(self.current_row, self.current_row + 10):  # reserve rows for labels (approximate)
            self.main_frame.grid_rowconfigure(r, weight=1)

        # Button frame at bottom
        button_row = self.current_row + 11
        button_frame = ttk.Frame(self.main_frame, style="TFrame")
        button_frame.grid(row=button_row, column=0, pady=40)

        edit_button = ttk.Button(button_frame, text="EDIT", command=self.edit_booking, width=15)
        edit_button.grid(row=0, column=0, padx=(0, 20))

        confirm_button = ttk.Button(button_frame, text="CONFIRM", command=lambda: controller.show_frame("ConfirmationPage"), width=15)
        confirm_button.grid(row=0, column=1)

        # Make button row NOT expandable vertically
        self.main_frame.grid_rowconfigure(button_row, weight=0)

    def display_booking_info(self):
        # Clear old labels
        for label in self.labels:
            label.destroy()
        self.labels.clear()

        data = self.controller.booking_data
        if not data:
            booking_lines = ["No booking data available."]
        else:
            recliners = data.get("recliners", 0)
            bunks = data.get("bunks", 0)
            total_cost, gst_portion = calculate_cost(recliners, bunks)

            booking_lines = [
                f"Name: {data.get('name', '')}",
                f"Email: {data.get('email', '')}",
                f"Phone: {data.get('phone', '')}",
                f"Route Selected: {data.get('route', '')}",
                f"Recliner Seats: {recliners}",
                f"Bunk Seats: {bunks}",
                f"Total Cost: ${total_cost:.2f} NZD",
                f"GST Portion: ${gst_portion:.2f} NZD"
            ]

        row = self.current_row
        for line in booking_lines:
            label = ttk.Label(self.main_frame, text=line, anchor="center", justify="center")
            label.grid(row=row, column=0, pady=5, sticky="ew")
            self.labels.append(label)
            row += 1

    def edit_booking(self):
        seat_selection_frame = self.controller.frames.get("SeatSelection")
        if seat_selection_frame:
            # 1. Release seats back to availability
            data = self.controller.booking_data
            if data:
                route_key = None
                # Find the route key matching the route string
                for key, route_name in seat_selection_frame.routes.items():
                    if route_name == data.get("route"):
                        route_key = key
                        break

                if route_key:
                    # Add back previously booked seats
                    seat_selection_frame.route_seats[route_key]["recliners"] += data.get("recliners", 0)
                    seat_selection_frame.route_seats[route_key]["bunks"] += data.get("bunks", 0)

            # 2. Pre-fill inputs with booking data
            if data:
                seat_selection_frame.route_var.set(route_key if route_key else "2")
                seat_selection_frame.recliner_entry.delete(0, tk.END)
                seat_selection_frame.recliner_entry.insert(0, str(data.get("recliners", 0)))
                seat_selection_frame.bunk_entry.delete(0, tk.END)
                seat_selection_frame.bunk_entry.insert(0, str(data.get("bunks", 0)))

            # 3. Update availability label to show correct availability
            seat_selection_frame.update_availability_label()

        self.controller.show_frame("SeatSelection")

    def confirm_booking(self):
        print("Booking confirmed - submit or save data here")

    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.display_booking_info()


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
            command=self.start_new_booking
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

    def start_new_booking(self):
        # Reset client info inputs
        client_info_frame = self.controller.frames["ClientInfo"]
        client_info_frame.reset_fields()

        # Reset seat selection page (route + availability)
        seat_selection_frame = self.controller.frames["SeatSelection"]
        seat_selection_frame.reset_selection()

        # Clear stored booking data
        self.controller.booking_data.clear()

        # Go back to the first page
        self.controller.show_frame("ClientInfo")


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

        for F in (ClientInfo, SeatSelection, BookingPreview, ConfirmationPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ClientInfo")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        # Call update_preview if available to refresh displayed data
        if hasattr(frame, "update_preview"):
            frame.update_preview()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
