from tkinter import *
from tkinter import ttk
import re


class ClientInfo:
    def __init__(self, parent):
        style = ttk.Style()
        style.theme_use("clam")

        # Colours
        background_colour = "#1a5c97"
        text_color_gold = "#d59e34"
        entry_background = "#a9b7c6"
        button_background_gold = "#d59e34"
        button_text_color = "black"

        # Styling
        style.configure("TFrame", background=background_colour)
        style.configure("TLabel", background=background_colour,
                        foreground=text_color_gold, font=("Palatino", 15, "bold"))
        style.configure("TEntry", foreground="black", fieldbackground=entry_background)
        style.configure("Error.TEntry", foreground="red")
        style.configure("Error.TLabel", background=background_colour,
                        foreground="#FF7F7F", font=("Palatino", 10, "italic"))

        # Styling for Buttons
        style.configure("TButton",
                        font=("Palatino", 12, "bold"),
                        foreground=button_text_color,
                        background=button_background_gold,
                        padding=[20, 10],
                        relief="solid",
                        borderwidth=6,
                        focuscolor="#f4cd83")

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.main_frame = ttk.Frame(parent, padding="20", style="TFrame")
        # Ensure main_frame fills the root window entirely
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Center all content inside main_frame horizontally
        self.main_frame.columnconfigure(0, weight=1)

        # Load image
        self.logo_image = PhotoImage(file="logo.png")

        # Add image label at top (row 0)
        self.img_label = ttk.Label(self.main_frame, image=self.logo_image, background=background_colour)
        self.img_label.grid(row=0, column=0, pady=(10, 20))

        # Dynamic Row Management for Even Gaps and Full Height
        current_row = 0

        # Top Spacer Row: This row will expand to push content down from the top
        self.main_frame.grid_rowconfigure(current_row, weight=2)
        current_row += 1

        # Title
        self.heading = ttk.Label(self.main_frame, text="THE MASSEY OVERNIGHTER",
                                 font=("Palatino", 25, "bold", "underline"), anchor="center")
        self.heading.grid(row=current_row, column=0, pady=(0, 30))  # Increased pady for gap below title
        current_row += 1

        # Spacer after Title, before Name (contributes to even gaps)
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

        # Spacer before Button Frame
        self.main_frame.grid_rowconfigure(current_row, weight=1)
        current_row += 1

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
        self.next_button.grid(row=0, column=1,  padx=(0, 20), sticky="ew")

        current_row += 1

        # Bottom Spacer Row
        self.main_frame.grid_rowconfigure(current_row, weight=3)

        self.booking_data = {}

    def validate_fields(self):
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

        if not (7 <= len(stripped_phone) <= 9):
            self.phone_entry.configure(style="Error.TEntry")
            self.phone_error.config(text="Phone must be 7–9 digits (excluding symbols).")
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

    def show_summary(self):
        if not self.booking_data:
            return

        top = Toplevel()  # Toplevel from tkinter import *
        top.title("Booking Summary")
        top.geometry("300x150")
        ttk.Label(top, text=f"Name: {self.booking_data['name']}").pack(pady=5)
        ttk.Label(top, text=f"Phone: {self.booking_data['phone']}").pack(pady=5)
        ttk.Label(top, text=f"Email: {self.booking_data['email']}").pack(pady=5)
        ttk.Button(top, text="Close", command=top.destroy).pack(pady=10)


# Main window
if __name__ == "__main__":
    root = Tk()  # Tk from tkinter import *
    root.title("The Massey Overnighter")
    root.geometry("600x800")  # Set the initial window size
    root.configure(bg="#1a5c97")  # Set root background to match frame

    app = ClientInfo(root)
    root.mainloop()