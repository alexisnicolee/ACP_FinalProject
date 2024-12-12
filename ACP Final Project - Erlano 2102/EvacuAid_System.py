import mysql.connector
import tkinter as tk
from tkinter import ttk

# Function to create a connection to the database
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="",           
            database="evacuaid_db"  
        )
        if conn.is_connected():
            print("Successfully connected to the database.")  
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to store family registration data in the database
def store_family_registration(
    family_name, total_family, primary_contact, email, 
    original_address, shelter_location, shelter_capacity, 
    region, postal_code
):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()

        # Insert data into the Families table
        insert_family_query = """
        INSERT INTO Families (family_name, total_family, primary_contact, email, original_address, shelter_location)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        family_data = (family_name, total_family, primary_contact, email, original_address, shelter_location)
        cursor.execute(insert_family_query, family_data)
        family_id = cursor.lastrowid  # Get the inserted family ID for related tables

        # Insert data into the Contacts table
        insert_contact_query = """
        INSERT INTO Contacts (family_id, primary_contact, email)
        VALUES (%s, %s, %s)
        """
        contact_data = (family_id, primary_contact, email)
        cursor.execute(insert_contact_query, contact_data)

        # Insert data into the Address table
        insert_address_query = """
        INSERT INTO Address (family_id, original_address, region, postal_code)
        VALUES (%s, %s, %s, %s)
        """
        address_data = (family_id, original_address, region, postal_code)
        cursor.execute(insert_address_query, address_data)

        # Insert data into the Shelter table
        insert_shelter_query = """
        INSERT INTO Shelter (family_id, shelter_location, capacity)
        VALUES (%s, %s, %s)
        """
        shelter_data = (family_id, shelter_location, shelter_capacity)
        cursor.execute(insert_shelter_query, shelter_data)

        conn.commit() 
        print("Successfully stored in the database.")  

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()  

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Function to transition to the Family Registration Page (Page 2)
def go_to_registration_page():
    welcome_frame.pack_forget() 
    registration_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to go back to the Family Registration page (Page 2)
def go_back_to_registration():
    verification_frame.pack_forget()  
    registration_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to transition to the Verification Page (Page 3)
def go_to_verification_page():
    family_name = family_name_entry.get()
    total_family = total_family_entry.get()
    primary_contact = primary_contact_entry.get()
    email = email_entry.get()
    original_address = original_address_entry.get()
    shelter_location = shelter_location_entry.get()
    shelter_capacity = shelter_capacity_entry.get()
    region = region_entry.get() 
    postal_code = postal_code_entry.get()  

    global verification_data
    verification_data = {
        'family_name': family_name,
        'total_family': total_family,
        'primary_contact': primary_contact,
        'email': email,
        'original_address': original_address,
        'shelter_location': shelter_location,
        'shelter_capacity': shelter_capacity, 
        'region': region,  
        'postal_code': postal_code,
    }

    registration_frame.pack_forget()
    verification_frame.pack(fill="both", expand=True, padx=20, pady=20)

    family_info_display.config(text=f"Family Name: {family_name}\nTotal Family Members: {total_family}")
    contact_info_display.config(text=f"Primary Contact: {primary_contact}\nEmail: {email}")
    address_info_display.config(text=f"Original Address: {original_address}\nEvacuation Shelter: {shelter_location}")
    shelter_info_display.config(text=f"Shelter Capacity: {shelter_capacity}\nRegion: {region}\nPostal Code: {postal_code}")

# Function to verify and store data, then transition to the Agreement Page (Page 4)
def verify_and_store_data():
    family_name = verification_data.get('family_name')
    total_family = verification_data.get('total_family')
    primary_contact = verification_data.get('primary_contact')
    email = verification_data.get('email')
    original_address = verification_data.get('original_address')
    shelter_location = verification_data.get('shelter_location')
    shelter_capacity = verification_data.get('shelter_capacity')
    region = verification_data.get('region')
    postal_code = verification_data.get('postal_code')

    store_family_registration(
        family_name, 
        total_family, 
        primary_contact, 
        email, 
        original_address, 
        shelter_location,
        shelter_capacity,  
        region,  
        postal_code  
    )

    verification_frame.pack_forget() 
    agreement_frame.pack(fill="both", expand=True, padx=20, pady=20) 

# Function to go back to the Verification Page (Page 3)
def go_back_to_verification_from_agreement():
    agreement_frame.pack_forget()  
    verification_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to transition to the Agreement Page (Page 4)
def go_to_agreement_page():
    verification_frame.pack_forget()  
    agreement_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to transition to the Confirmation Page (Page 5)
def go_to_confirmation_page():
    agreement_frame.pack_forget()  
    confirmation_summary_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to transition to the Data Table Page (Page 6)
def go_to_data_table_page():
    confirmation_summary_frame.pack_forget()  
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)  
    refresh_table()  

# Function to go back to the Data Table Page (Page 6)
def go_back_to_data_table_page():
    summary_frame.pack_forget()  
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)  

# Function to transition to the Summary Page (Page 7)
def show_summary_page():
    table_frame.pack_forget()  
    summary_frame.pack(fill="both", expand=True, padx=20, pady=20)  
    show_summary()  

# Function to fetch and display the total individuals in the shelter
def show_summary():
    total = fetch_total_individuals()
    summary_label.config(text=f"Total Individuals in Shelter: {total}")

# Function to fetch the total number of individuals from the database
def fetch_total_individuals():
    conn = create_connection()
    if not conn:
        return 0  

    cursor = conn.cursor()
    query = "SELECT SUM(total_family) FROM Families"
    cursor.execute(query)
    total = cursor.fetchone()[0] or 0  
    cursor.close()
    conn.close()
    return total

#Function to go to data table page
def go_to_data_table_page():
    confirmation_summary_frame.pack_forget()  
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)  
    refresh_table() 

# Function to fetch data from MySQL and populate the table
def fetch_data():
    conn = create_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    query = """
    SELECT f.family_id, f.family_name, f.total_family, c.primary_contact,
           c.email, a.original_address, a.region, a.postal_code, 
           f.shelter_location, s.capacity
    FROM Families f
    LEFT JOIN Contacts c ON f.family_id = c.family_id
    LEFT JOIN Address a ON f.family_id = a.family_id
    LEFT JOIN Shelter s ON f.family_id = s.family_id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data

# Function to populate the table with fetched data
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    data = fetch_data()
    for row in data:
        tree.insert("", tk.END, values=row)

# Function to fetch total individuals and families from the database
def fetch_totals():
    conn = create_connection()
    if not conn:
        return 0, 0  # Return defaults if no connection

    cursor = conn.cursor()
    cursor.execute("SELECT SUM(total_family) FROM Families")
    total_individuals = cursor.fetchone()[0] or 0  # Default to 0 if no result
    cursor.execute("SELECT COUNT(*) FROM Families")
    total_families = cursor.fetchone()[0] or 0  # Default to 0 if no result
    cursor.close()
    conn.close()
    return total_individuals, total_families

# Function to fetch and display summary data
def show_summary():
    total_individuals, total_families = fetch_totals()
    summary_label.config(text=f"TOTAL INDIVIDUALS: {total_individuals}")
    additional_summary.config(text=f"FAMILIES REGISTERED: {total_families}")

# Function to switch frames and show the summary page
def show_summary_page():
    switch_frame(summary_frame)
    show_summary()

# Navigation function to switch between frames
def switch_frame(frame):
    for child in root.winfo_children():  # Hide all frames
        child.pack_forget()
    frame.pack(fill="both", expand=True)

# Create the main window
root = tk.Tk()
root.title("EvacuAid: Disaster Evacuation Management System")
root.geometry("1280x800")
root.config(bg="#FEFAE0")

# --- Page 1: Welcome Page ---
welcome_frame = tk.Frame(root, bg="#FEFAE0")
welcome_frame.pack(fill="both", expand=True)  

logo_image = tk.PhotoImage(file="C:/Users/ALMA OSCA/Downloads/pylogo.png")  
logo_image = logo_image.subsample(1, 1)  

logo_label = tk.Label(welcome_frame, image=logo_image, bg="#FEFAE0")
logo_label.pack(pady=(20, 10)) 

title_label = tk.Label(welcome_frame, text="hi, welcome to", font=("Tahoma", 25, "bold"), fg="#BC6C25", bg="#FEFAE0")
title_label.pack(pady=(50, 10), anchor="center")  

evacu_aid_label = tk.Label(welcome_frame, text="E V A C U A I D!", font=("Tahoma", 60, "bold"), fg="#606C38", bg="#FEFAE0")
evacu_aid_label.pack(pady=(0, 20), anchor="center")  

description_text = "a disaster management system that helps track the evacuation of families during emergencies, please register your family’s details to ensure we can assist you effectively during this evacuation."
description_label = tk.Label(welcome_frame, text=description_text, font=("Tahoma", 15, "bold"), fg="#895D2B", bg="#FEFAE0", wraplength=1000, justify="center")
description_label.pack(side="top", pady=20, anchor="center")  

proceed_button = tk.Button(welcome_frame, text="proceed", command=go_to_registration_page, font=("Poppins", 14, "bold"), fg="white", bg="#BC6025", relief="flat", width=20, height=2)
proceed_button.pack(side="bottom", pady=50)  

# --- Page 2: Family Registration Page ---
registration_frame = tk.Frame(root, bg="#FEFAE0")
registration_frame.pack_forget()  

registration_frame = tk.Frame(root, bg="#FEFAE0")
registration_frame.grid_rowconfigure(0, weight=0) 
registration_frame.grid_rowconfigure(1, weight=0)  
registration_frame.grid_rowconfigure(2, weight=0)  
registration_frame.grid_rowconfigure(3, weight=0)  
registration_frame.grid_rowconfigure(4, weight=0)  
registration_frame.grid_rowconfigure(5, weight=0)  

registration_frame.grid_columnconfigure(0, weight=1)  
registration_frame.grid_columnconfigure(1, weight=2)  


registration_title = tk.Label(registration_frame, text="F A M I L Y  R E G I S T R A T I O N", font=("Tahoma", 32, "bold"), fg="#DDA15E", bg="#606C38", width=50, height=2, anchor="center")
registration_title.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

description_text = """THIS PAGE COLLECTS THE NECESSARY INFORMATION FOR TRACKING DURING THE EVACUATION"""
description_label = tk.Label(registration_frame, text=description_text, font=("Montserrat", 12, "bold", "underline"), fg="#BC6025", bg="#FEFAE0", wraplength=1500, justify="center")
description_label.grid(row=1, column=0, columnspan=2, pady=15, sticky="nsew")  

family_info_label = tk.Label(registration_frame, text="FAMILY INFORMATION", font=("Montserrat", 12, "bold", "italic"), fg="#606C38", bg="#FEFAE0")
family_info_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")  

family_name_label = tk.Label(registration_frame, text="Family Name:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
family_name_label.grid(row=3, column=0, sticky="w", padx=20, pady=5)  
family_name_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
family_name_entry.grid(row=3, column=1, padx=20, pady=5, sticky="ew")  

total_family_label = tk.Label(registration_frame, text="Total Number of Family Members:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
total_family_label.grid(row=4, column=0, sticky="w", padx=20, pady=5)  
total_family_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
total_family_entry.grid(row=4, column=1, padx=20, pady=5, sticky="ew") 

contact_info_label = tk.Label(registration_frame, text="CONTACT INFORMATION", font=("Montserrat", 12, "bold", "italic"), fg="#606C38", bg="#FEFAE0")
contact_info_label.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew") 

primary_contact_label = tk.Label(registration_frame, text="Primary Contact Number:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
primary_contact_label.grid(row=6, column=0, sticky="w", padx=20, pady=5)  
primary_contact_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
primary_contact_entry.grid(row=6, column=1, padx=20, pady=5, sticky="ew")  

email_label = tk.Label(registration_frame, text="Email Address (Optional):", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
email_label.grid(row=8, column=0, sticky="w", padx=20, pady=5)  
email_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
email_entry.grid(row=8, column=1, padx=20, pady=5, sticky="ew") 

address_info_label = tk.Label(registration_frame, text="ADDRESS INFORMATION", font=("Montserrat", 12, "bold", "italic"), fg="#606C38", bg="#FEFAE0")
address_info_label.grid(row=9, column=0, columnspan=2, pady=10, sticky="nsew")  

original_address_label = tk.Label(registration_frame, text="Original Residence Address:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
original_address_label.grid(row=10, column=0, sticky="w", padx=20, pady=5)  
original_address_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
original_address_entry.grid(row=10, column=1, padx=20, pady=5, sticky="ew") 

region_label = tk.Label(registration_frame, text="Region:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
region_label.grid(row=11, column=0, sticky="w", padx=20, pady=5)
region_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
region_entry.grid(row=11, column=1, padx=20, pady=5, sticky="ew")

postal_code_label = tk.Label(registration_frame, text="Postal Code:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
postal_code_label.grid(row=12, column=0, sticky="w", padx=20, pady=5)
postal_code_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
postal_code_entry.grid(row=12, column=1, padx=20, pady=5, sticky="ew")

shelter_location_label = tk.Label(registration_frame, text="Evacuation Shelter Name/Location:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
shelter_location_label.grid(row=13, column=0, sticky="w", padx=20, pady=5)  
shelter_location_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
shelter_location_entry.grid(row=13, column=1, padx=20, pady=5, sticky="ew")  

shelter_capacity_label = tk.Label(registration_frame, text="Shelter Capacity:", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0")
shelter_capacity_label.grid(row=14, column=0, sticky="w", padx=20, pady=5)
shelter_capacity_entry = tk.Entry(registration_frame, font=("Montserrat", 12))
shelter_capacity_entry.grid(row=14, column=1, padx=20, pady=5, sticky="ew")

proceed_button = tk.Button(registration_frame, text="proceed to next", command=go_to_verification_page, font=("Poppins", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=2)
proceed_button.grid(row=18, column=0, columnspan=2, pady=20, sticky="s") 

# --- Page 3: Verification Page ---
verification_frame = tk.Frame(root, bg="#FEFAE0")

verification_title = tk.Label(verification_frame, text="V E R I F I C A T I O N  O F  I N F O R M A T I O N", font=("Tahoma", 32, "bold"), fg="#DDA15E", bg="#606C38", width=65, height=2, anchor="center")
verification_title.pack(pady=20)

description_text = """PLEASE VERIFY THE INFORMATION ENTERED BELOW."""
description_label = tk.Label(verification_frame, text=description_text, font=("Montserrat", 12, "bold", "underline"), fg="#BC6025", bg="#FEFAE0", wraplength=1400, justify="center")
description_label.pack(pady=5)

info_frame = tk.Frame(verification_frame, bg="#FEFAE0")
info_frame.pack(fill="x", padx=40)

family_info_label = tk.Label(info_frame, text="F A M I L Y  I N F O R M A T I O N", font=("Montserrat", 13, "bold"), fg="#FF5733", bg="#FEFAE0")
family_info_label.grid(row=0, column=0, sticky="w", pady=10)
family_info_display = tk.Label(info_frame, text="", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0", anchor="w", justify="left")
family_info_display.grid(row=1, column=0, sticky="w", padx=10, pady=10)

contact_info_label = tk.Label(info_frame, text="C O N T A C T  I N F O R M A T I O N", font=("Montserrat", 13, "bold"), fg="#FF5733", bg="#FEFAE0")
contact_info_label.grid(row=2, column=0, sticky="w", pady=10)
contact_info_display = tk.Label(info_frame, text="", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0", anchor="w", justify="left")
contact_info_display.grid(row=3, column=0, sticky="w", padx=10, pady=10)

address_info_label = tk.Label(info_frame, text="A D D R E S S  I N F O R M A T I O N", font=("Montserrat", 13, "bold"), fg="#FF5733", bg="#FEFAE0")
address_info_label.grid(row=4, column=0, sticky="w", pady=10)
address_info_display = tk.Label(info_frame, text="", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0", anchor="w", justify="left")
address_info_display.grid(row=5, column=0, sticky="w", padx=10, pady=10)

shelter_info_label = tk.Label(info_frame, text="S H E L T E R  I N F O R M A T I O N", font=("Montserrat", 13, "bold"), fg="#FF5733", bg="#FEFAE0")
shelter_info_label.grid(row=6, column=0, sticky="w", pady=10)
shelter_info_display = tk.Label(info_frame, text="", font=("Montserrat", 12, "bold"), fg="#606C38", bg="#FEFAE0", anchor="w", justify="left")
shelter_info_display.grid(row=7, column=0, sticky="w", padx=10, pady=10)

button_frame = tk.Frame(verification_frame, bg="#FEFAE0")
button_frame.pack(pady=30, fill="x", padx=50)  
back_button_verification = tk.Button(button_frame, text="back", command=go_back_to_registration, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=4, padx=30, pady=15).pack(side="left", padx=30)
next_button_verification = tk.Button(button_frame, text="verify", command=verify_and_store_data, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=4, padx=30, pady=15).pack(side="right", padx=30)

# --- Page 4: Agreement Page ---
agreement_frame = tk.Frame(root, bg="#FEFAE0")
tk.Label(agreement_frame, text="T E R M S  O F  A G R E E M E N T", font=("Tahoma", 32, "bold"), fg="#DDA15E", bg="#606C38", width=65, height=2, anchor="center").pack(pady=20)

agreement_text = """
by proceeding with this registration, you confirm that the information you provide is accurate and complete to the best of your knowledge. any false or misleading information may result in disqualification from the evacuation process, delays in receiving assistance, or legal consequences.

the personal details you submit will be used solely for disaster management purposes, including communication with relevant authorities and agencies to coordinate evacuations, provide safety alerts, and facilitate emergency response operations.

you hereby consent to being contacted by the appropriate authorities during emergencies, to receive updates, safety instructions, and necessary communications related to your safety and the evacuation process.

by continuing, you agree to abide by the terms and conditions outlined above, understanding the importance of timely, accurate, and complete information for the success of evacuation efforts and your safety.
"""

agreement_label = tk.Label(agreement_frame, text=agreement_text, font=("Montserrat", 14, "bold", "italic"), fg="#606C38", bg="#FEFAE0", wraplength=900, justify="center")
agreement_label.pack(pady=20)

back_button_agreement = tk.Button(agreement_frame, text="back", command=go_back_to_verification_from_agreement, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=2)
back_button_agreement.pack(side="left", padx=30, pady=20)

agree_button = tk.Button(agreement_frame, text="i agree", command=go_to_confirmation_page, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=2)
agree_button.pack(side="right", padx=30, pady=20)

def go_to_data_table_page():
    confirmation_summary_frame.pack_forget()  
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)  
    refresh_table()  

# --- Page 5: Confirmation Page ---
confirmation_summary_frame = tk.Frame(root, bg="#FEFAE0")
confirmation_title = tk.Label(confirmation_summary_frame, text="S U C C E S S F U L L Y  R E G I S T E R E D!", font=("Tahoma", 32, "bold"), fg="#DDA15E", bg="#606C38", width=65, height=2, anchor="center")
confirmation_title.pack(pady=20)

dots_label = tk.Label(confirmation_summary_frame, text=".   .   .", font=("Montserrat", 35, "bold"), fg="#BC6025", bg="#FEFAE0")
dots_label.pack(pady=10)  

confirmation_summary_frame.grid_rowconfigure(0, weight=1)  
confirmation_summary_frame.grid_rowconfigure(2, weight=0)  
confirmation_summary_frame.grid_columnconfigure(0, weight=1)  
confirmation_summary_frame.grid_rowconfigure(0, weight=1)  
confirmation_summary_frame.grid_rowconfigure(2, weight=0)  
confirmation_summary_frame.grid_columnconfigure(0, weight=1)  

confirmation_text = """
your family evacuation registration has been successfully completed.

your information has been securely stored, and you will be contacted when necessary during emergencies. rest assured that we are committed to ensuring your safety and well-being.

while we hope that disaster events do not affect you directly, we encourage you to stay vigilant and be prepared. please follow official safety protocols and keep your communication lines open for updates. 

together, we can navigate through any challenges that may arise. your preparation and awareness are key to your safety. stay strong, stay safe, and remember that EvacuAid is here for you whenever you need it.

"""
confirmation_label = tk.Label(confirmation_summary_frame, text=confirmation_text, font=("Montserrat", 14, "bold"), fg="#606C38", bg="#FEFAE0", wraplength=750, justify="center")
confirmation_label.pack(pady=20)

next_page_button = tk.Button(confirmation_summary_frame, text="view data", command=go_to_data_table_page, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=25, height=2)
next_page_button.pack(pady=10)

# --- Page 6: Data Table Page ---
table_frame = tk.Frame(root, bg="#FEFAE0")

tree = ttk.Treeview(table_frame, columns=("family_id", "family_name", "total_family", "primary_contact", "email", "original_address", "region", "postal_code", "shelter_location", "shelter_capacity"), show="headings")
tree.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

tree.heading("family_id", text="FAMILY I.D")
tree.heading("family_name", text="FAMILY NAME")
tree.heading("total_family", text="T. MEMBERS")
tree.heading("primary_contact", text="P. CONTACT")
tree.heading("email", text="EMAIL")
tree.heading("original_address", text="O. ADDRESS")
tree.heading("region", text="REGION")
tree.heading("postal_code", text="POSTAL CODE")
tree.heading("shelter_location", text="S. LOCATION")
tree.heading("shelter_capacity", text="CAPACITY")

tree.column("family_id", width=100, anchor="center")
tree.column("family_name", width=150, anchor="w")
tree.column("total_family", width=100, anchor="center")
tree.column("primary_contact", width=150, anchor="center")
tree.column("email", width=200, anchor="w")
tree.column("original_address", width=200, anchor="w")
tree.column("region", width=150, anchor="w")
tree.column("postal_code", width=100, anchor="center")
tree.column("shelter_location", width=150, anchor="w")
tree.column("shelter_capacity", width=100, anchor="center")

exit_button = tk.Button(table_frame, text="exit", command=root.quit, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=20, height=2)
exit_button.grid(row=3, column=1, padx=20, pady=30, sticky="e")  

summary_button = tk.Button(table_frame, text="view total individual", command=show_summary_page, font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", width=20, height=2)
summary_button.grid(row=3, column=0, padx=20, pady=30, sticky="w")  

table_frame.grid_rowconfigure(0, weight=1)  
table_frame.grid_rowconfigure(2, weight=0)  
table_frame.grid_rowconfigure(3, weight=0)  
table_frame.grid_columnconfigure(0, weight=1) 
table_frame.grid_columnconfigure(1, weight=1)
table_frame.pack_forget()

# Page 7: Summary Page
summary_frame = tk.Frame(root, bg="#FEFAE0")

header_frame = tk.Frame(summary_frame, bg="#606C38", pady=30)  
header_frame.pack(pady=(30, 10), fill="x")  

tk.Label(header_frame, text="E V A C U A T I O N  C E N T E R  R E P O R T", font=("Montserrat", 30, "bold"), fg="#DDA15E", bg="#606C38").pack()
tk.Canvas(summary_frame, width=900, height=4, bg="#BC6025", highlightthickness=0).pack(pady=15)

center_frame = tk.Frame(summary_frame, bg="#FEFAE0")
center_frame.pack(expand=True)  

summary_label = tk.Label(center_frame, text="TOTAL INDIVIDUALS: 0", font=("Tahoma", 18, "bold"), fg="#606C38", bg="#FEFAE0")
summary_label.pack(pady=10)

additional_summary = tk.Label(center_frame, text="FAMILIES REGISTERED: --", font=("Tahoma", 18, "bold"), fg="#606C38", bg="#FEFAE0")
additional_summary.pack(pady=10)

tk.Button(summary_frame, text="BACK TO DATA TABLE", command=lambda: switch_frame(table_frame), font=("Montserrat", 12, "bold"), fg="white", bg="#BC6025", relief="flat", padx=10, pady=5).pack(pady=20)

root.mainloop()