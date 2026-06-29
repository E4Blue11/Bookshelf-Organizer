import tkinter as tk
from tkinter import messagebox, ttk
from functools import cmp_to_key

# Componments of a Book
class Book:
    def __init__(self, title, author, genre, height, is_standalone, series_name=None, series_order=0):
        self.title = title
        self.author = author          # Format: "Last, First"
        self.genre = genre
        self.height = int(height)     # Has to be int
        self.is_standalone = is_standalone
        self.series_name = series_name or ""
        self.series_order = int(series_order) if series_order else 0

    def __repr__(self):
        type_str = "Standalone" if self.is_standalone else f"Series: {self.series_name} #{self.series_order}"
        return f"'{self.title}' by {self.author} | {self.genre} | {type_str} | Height: {self.height}cm"

# Empty bookshelf that users add books to
bookshelf = []

# The Sorting Algorithm
def make_book_comparator(preferences):
    # compare two books
    def compare(book1, book2):
        # for loop that goes through the different preferences and compares them to organize them
        for criteria, direction in preferences:
            if criteria == "None":
                continue
            
            # The values assigned based on current preference
            val1, val2 = None, None
            if criteria == 'Genre': val1, val2 = book1.genre, book2.genre
            elif criteria == 'Author': val1, val2 = book1.author, book2.author
            elif criteria == 'Height': val1, val2 = book1.height, book2.height
            elif criteria == 'Standalone vs Series': val1, val2 = book1.is_standalone, book2.is_standalone
            # Comparing values
            if val1 != val2:
                if direction == 'Ascending (A-Z / Smallest)':
                    return -1 if val1 < val2 else 1
                else:
                    return -1 if val1 > val2 else 1
                    
            # Tie-breaker for series
            if criteria == 'Standalone vs Series' and not book1.is_standalone and not book2.is_standalone:
                if book1.series_name != book2.series_name:
                    return -1 if book1.series_name < book2.series_name else 1
                if book1.series_order != book2.series_order:
                    return -1 if book1.series_order < book2.series_order else 1
        return 0
    return cmp_to_key(compare)

# GUI Application
class BookshelfSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Bookshelf Maker & Organizer")
        self.root.geometry("900x550")
        
        # Options for sorting
        self.options = ["None", "Genre", "Author", "Height", "Standalone vs Series"]
        self.directions = ["Ascending (A-Z / Smallest)", "Descending (Z-A / Tallest)"]
        
        # Main Layout: Split into Left Control Panel and Right Display Panel
        self.left_panel = tk.Frame(root, padx=15, pady=15, width=400)
        self.left_panel.pack(side="left", fill="y")
        
        self.right_panel = tk.Frame(root, padx=15, pady=15)
        self.right_panel.pack(side="right", fill="both", expand=True)
        
        # --- LEFT PANEL: ADD BOOK FORM ---
        tk.Label(self.left_panel, text="Step 1: Add a New Book", font=("Times", 12, "bold")).pack(anchor="w", pady=(0, 10))
        
        form_frame = tk.Frame(self.left_panel)
        form_frame.pack(fill="x", pady=5)
        
        tk.Label(form_frame, text="Title:").grid(row=0, column=0, sticky="w", pady=2)
        self.ent_title = tk.Entry(form_frame, width=30)
        self.ent_title.grid(row=0, column=1, pady=2)
        
        tk.Label(form_frame, text="Author (Last, First):").grid(row=1, column=0, sticky="w", pady=2)
        self.ent_author = tk.Entry(form_frame, width=30)
        self.ent_author.grid(row=1, column=1, pady=2)
        
        tk.Label(form_frame, text="Genre:").grid(row=2, column=0, sticky="w", pady=2)
        self.ent_genre = tk.Entry(form_frame, width=30)
        self.ent_genre.grid(row=2, column=1, pady=2)
        
        tk.Label(form_frame, text="Height (cm):").grid(row=3, column=0, sticky="w", pady=2)
        self.ent_height = tk.Entry(form_frame, width=10)
        self.ent_height.grid(row=3, column=1, sticky="w", pady=2)
        
        # Standalone vs Series Toggle
        tk.Label(form_frame, text="Type:").grid(row=4, column=0, sticky="w", pady=5)
        self.book_type = tk.StringVar(value="Standalone")
        tk.Radiobutton(form_frame, text="Standalone", variable=self.book_type, value="Standalone", command=self.toggle_series_fields).grid(row=4, column=1, sticky="w")
        tk.Radiobutton(form_frame, text="Part of a Series", variable=self.book_type, value="Series", command=self.toggle_series_fields).grid(row=5, column=1, sticky="w")
        
        # Series Specific Fields (Hidden by default)
        self.lbl_series_name = tk.Label(form_frame, text="Series Name:")
        self.ent_series_name = tk.Entry(form_frame, width=30)
        self.lbl_series_order = tk.Label(form_frame, text="Volume #:")
        self.ent_series_order = tk.Entry(form_frame, width=10)
        
        self.btn_add = tk.Button(self.left_panel, text="Add Book to Shelf", bg="#2196F3", fg="black", font=("Times", 11, "bold"), command=self.add_book)
        self.btn_add.pack(fill="x", pady=15)
        
        # --- LEFT PANEL: SORT CONFIGURATION ---
        tk.Frame(self.left_panel, height=2, bd=1, relief="groove").pack(fill="x", pady=10) # Divider Line
        tk.Label(self.left_panel, text="Step 2: Configure Preferences", font=("Times", 12, "bold")).pack(anchor="w", pady=5)
        
        pref_frame = tk.Frame(self.left_panel)
        pref_frame.pack(fill="x", pady=5)
        
        # Priority 1
        tk.Label(pref_frame, text="1st Rule:").grid(row=0, column=0, sticky="w", pady=2)
        self.pref1 = ttk.Combobox(pref_frame, values=self.options, state="readonly", width=18)
        self.pref1.set("Genre")
        self.pref1.grid(row=0, column=1, pady=2, padx=5)
        self.dir1 = ttk.Combobox(pref_frame, values=self.directions, state="readonly", width=22)
        self.dir1.set("Ascending (A-Z / Smallest)")
        self.dir1.grid(row=0, column=2, pady=2)
        
        # Priority 2
        tk.Label(pref_frame, text="2nd Rule:").grid(row=1, column=0, sticky="w", pady=2)
        self.pref2 = ttk.Combobox(pref_frame, values=self.options, state="readonly", width=18)
        self.pref2.set("Height")
        self.pref2.grid(row=1, column=1, pady=2, padx=5)
        self.dir2 = ttk.Combobox(pref_frame, values=self.directions, state="readonly", width=22)
        self.dir2.set("Descending (Z-A / Tallest)")
        self.dir2.grid(row=1, column=2, pady=2)
        
        self.btn_sort = tk.Button(self.left_panel, text="Sort Bookshelf", bg="#4CAF50", fg="black", font=("Times", 11, "bold"), command=self.run_sorting)
        self.btn_sort.pack(fill="x", pady=15)
        
        # --- RIGHT PANEL: OUTPUT ---
        tk.Label(self.right_panel, text="Your Custom Bookshelf", font=("Times", 14, "bold")).pack(anchor="w")
        self.output_box = tk.Text(self.right_panel, height=25, width=60)
        self.output_box.pack(fill="both", expand=True, pady=10)
        
        self.display_books(bookshelf)

    def toggle_series_fields(self):
        """Shows or hides series entry boxes based on the radio button state."""
        if self.book_type.get() == "Series":
            self.lbl_series_name.grid(row=6, column=0, sticky="w", pady=2)
            self.ent_series_name.grid(row=6, column=1, pady=2)
            self.lbl_series_order.grid(row=7, column=0, sticky="w", pady=2)
            self.ent_series_order.grid(row=7, column=1, sticky="w")
        else:
            self.lbl_series_name.grid_remove()
            self.ent_series_name.grid_remove()
            self.lbl_series_order.grid_remove()
            self.ent_series_order.grid_remove()

    def add_book(self):
        """Validates inputs and creates a new Book instance."""
        title = self.ent_title.get().strip()
        author = self.ent_author.get().strip()
        genre = self.ent_genre.get().strip()
        height_raw = self.ent_height.get().strip()
        
        # Basic validation
        if not title or not author or not genre or not height_raw:
            messagebox.showerror("Error", "Please fill out all primary book fields.")
            return
        
        try:
            height = int(height_raw)
        except ValueError:
            messagebox.showerror("Error", "Height must be a valid whole number (e.g., 22).")
            return
            
        is_standalone = (self.book_type.get() == "Standalone")
        series_name = self.ent_series_name.get().strip() if not is_standalone else ""
        series_order = self.ent_series_order.get().strip() if not is_standalone else 0
        
        if not is_standalone and not series_name:
            messagebox.showerror("Error", "Please provide a Series Name.")
            return

        # Create and add the book
        new_book = Book(title, author, genre, height, is_standalone, series_name, series_order)
        bookshelf.append(new_book)
        
        # Clear fields for the next entry
        self.ent_title.delete(0, tk.END)
        self.ent_author.delete(0, tk.END)
        self.ent_genre.delete(0, tk.END)
        self.ent_height.delete(0, tk.END)
        self.ent_series_name.delete(0, tk.END)
        self.ent_series_order.delete(0, tk.END)
        
        # Update UI text box
        self.display_books(bookshelf)

    def display_books(self, books):
        self.output_box.delete("1.0", tk.END)
        if not books:
            self.output_box.insert(tk.END, "Your bookshelf is currently empty. Add some books on the left!")
            return
        for i, book in enumerate(books, 1):
            self.output_box.insert(tk.END, f"[{i}] {book}\n")

    def run_sorting(self):
        if not bookshelf:
            messagebox.showwarning("Warning", "Add some books to your shelf before sorting!")
            return
            
        user_preferences = [
            (self.pref1.get(), self.dir1.get()),
            (self.pref2.get(), self.dir2.get())
        ]
        
        # Sort globally
        sorted_books = sorted(bookshelf, key=make_book_comparator(user_preferences))
        self.display_books(sorted_books)


if __name__ == "__main__":
    root = tk.Tk()
    app = BookshelfSorterApp(root)
    root.mainloop()
