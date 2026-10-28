# PROJECT 10: LIBRARY RECORD MANAGER
# Student: Upender Parakala
# Description: Manages local catalog of library books,
# tracking lending status and circulation records.
# ==========================================

# 1. Catalog Storage using a Dictionary of Dictionaries
library_catalog = {
    "B01": {
        "title": "Clean Code", 
        "author": "Robert C. Martin", 
        "status": "Available"
    },
    "B02": {
        "title": "Fluent Python", 
        "author": "Luciano Ramalho", 
        "status": "Borrowed"
    },
    "B03": {
        "title": "The Pragmatic Programmer", 
        "author": "Andrew Hunt", 
        "status": "Available"
    }
}

def display_catalog():
    """Displays the updated library catalog after every transaction[span_4](start_span)[span_4](end_span)."""
    if not library_catalog:
        print("\n[!] Error: Library catalog is empty[span_5](start_span)[span_5](end_span).")
        return
        
    print("\nCatalog:")
    # Formats and prints all books in a single line as requested in sample I/O[span_6](start_span)[span_6](end_span)
    catalog_items = []
    for book_id, details in library_catalog.items():
        item_str = f"[{book_id}] {details['title']} — {details['status']}"
        catalog_items.append(item_str)
    
    print(" | ".join(catalog_items))
    print("-" * 65)

def borrow_book():
    """Handles checking out an available book and toggles status[span_7](start_span)[span_7](end_span)."""
    display_catalog()
    book_id = input("Action: Borrow ").strip().upper()
    
    # Edge Case: Searching or transacting with a non-existent Book ID[span_8](start_span)[span_8](end_span)
    if book_id not in library_catalog:
        print(f"-> ERROR: Book ID '{book_id}' does not exist.")
        return
        
    selected_book = library_catalog[book_id]
    
    # Edge Case: Borrowing an already borrowed book[span_9](start_span)[span_9](end_span)
    if selected_book["status"] == "Borrowed":
        print(f"-> ERROR: '{selected_book['title']}' is currently borrowed by another reader[span_10](start_span)[span_10](end_span)!")
    else:
        # Toggle status to unavailable/borrowed
        selected_book["status"] = "Borrowed"
        print(f"-> SUCCESS: '{selected_book['title']}' checked out successfully[span_11](start_span)[span_11](end_span).")
        
    display_catalog()

def return_book():
    """Handles returning a checked-out book and toggles status back[span_12](start_span)[span_12](end_span)."""
    display_catalog()
    book_id = input("Action: Return ").strip().upper()
    
    # Edge Case: Non-existent ID check[span_13](start_span)[span_13](end_span)
    if book_id not in library_catalog:
        print(f"-> ERROR: Book ID '{book_id}' does not exist.")
        return
        
    selected_book = library_catalog[book_id]
    
    # Edge Case: Returning a book that was never borrowed or already available[span_14](start_span)[span_14](end_span)
    if selected_book["status"] == "Available":
        print(f"-> ERROR: '{selected_book['title']}' is already marked available.")
    else:
        # Toggle status back to available
        selected_book["status"] = "Available"
        print(f"-> SUCCESS: '{selected_book['title']}' returned and ready for circulation[span_15](start_span)[span_15](end_span).")
        
    display_catalog()

def main():
    """Main execution flow with a while loop and menu options[span_16](start_span)[span_16](end_span)."""
    while True:
        print("\n=== Library Record Manager Menu ===")
        print("1. View Catalog")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            display_catalog()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("Exiting application. Have a great day!")
            break
        else:
            print("-> ERROR: Invalid action or choice. Please try again[span_17](start_span)[span_17](end_span).")

if __name__ == "__main__":
    main()