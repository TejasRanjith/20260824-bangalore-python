import subprocess
import os

def add_book_entry(catalog,next_id):
    
    try:
        
        book_title = input("Enter the new book title to add: ").strip().title()
        if len(book_title) == 0:
            raise ValueError
        author_name = input("Enter the authors name: ").strip().title()
        if len(author_name) == 0:
            raise ValueError
        genre = input("Enter the genre name to which the book belongs to: ").strip().title()
        if len(genre) == 0:
            raise ValueError
        price = float(input("Enter the price value to assign for the book: "))
        if price <= float(0):
            raise ValueError
        copies = int(input("Enter the number of copies of book to add: "))
        if copies <0:
            raise ValueError
    except ValueError:
        print("Try again with proper input values.\n GOING BACK TO MENU.......")
        return -1
    else:
        catalog.append(dict(
            id = next_id,
            book_title = book_title,
            author_name = author_name,
            genre = genre,
            price = price,
            copies = copies
            ))
        
        
        
        
def render_catalog(catalog):
    pass
    

def load_catalog_from_file():
    return []
        
        
        
        
        
        


def menu():
    while True:
        print("\n","*"*92,"\n")
        print("="*30,"BOOK CATALOG MANAGEMENT SYSTEM","="*30)
        print('''\n  1. Add Book  \n  2. View Catalog  \n  3. Search Books  \n  4. Update Details  \n  5. Delete Book  \n  6. Save to File  \n  7. Load from File  \n  8. Exit''')
        try:
            choice = int(input("Enter Your Preferred Choice: "))
            if choice < 0 or choice > 8 :
                raise ValueError
            else:
                return choice
        except ValueError:
            print("Retry again with a valid option shown from the menu.")
            continue
            
        

def main():
    catalog = load_catalog_from_file()
    if len(catalog) == 0:
        catalog = []
    counter = len(catalog)
    subprocess.run('cls', shell=True)
    choice = menu()
    while not choice == 8:
        if choice == 0:
            subprocess.run('cls', shell=True)
        elif choice == 1:
            catalog = add_book_entry(catalog,counter+1)
        elif choice == 2:
            catalog = render_catalog(catalog)
        choice = menu()
    print("*"*92,"\n")
    print("x"*18,"THANK YOU FOR USING THE BOOK CATALOG MANAGEMENT SYSTEM","x"*18)



if __name__ == "__main__":
    main()