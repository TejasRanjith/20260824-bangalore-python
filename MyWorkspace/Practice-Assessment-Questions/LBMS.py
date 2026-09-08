import subprocess
import re
def add_book_entry(catalog,next_id):
    
    try:
        book_title = input("Enter the new book title to add: ").strip().title()
        if len(book_title) == 0:
            raise ValueError
        
        author_name = input("Enter the authors name: ").strip().title()
        if len(author_name) == 0 or re.search(r"[0-9]+",author_name):
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
        return catalog
    else:
        catalog.append(dict(
            id = next_id,
            book_title = book_title,
            author_name = author_name,
            genre = genre,
            price = price,
            copies = copies
            ))
        return catalog
        
        
        
        
def render_catalog(catalog):
    print(catalog)
    return catalog

def  sync_catalog_to_file(filepath,catalog):
    if len(catalog) != 0:
        try:
            with open(filepath,'r') as f1:
                old_content = f1.read()
                if len(old_content) == 0:
                    old_content = '[]'
            with open(filepath,"w") as f2:
                old_catalog = eval(old_content)
                for d in catalog:
                    if d['id'] in [list(book.values())[0] for book in old_catalog]:
                        print(f"Book of id '{d['id']}' already exists.")
                    else:
                        to_add = dict(id = d['id'],book_title=d['book_title'],author_name = d['author_name'],genre=d['genre'],price=d['price'],copies = d['copies'])
                        old_catalog.append(to_add)
                        f2.write(f"{old_catalog}")

                return old_catalog
        except FileNotFoundError:
            with open(filepath,'w') as f:
                f.write(f"{catalog}")
            return catalog
            
    else:
        print("Nothing in catalog to perform sync process.")
        return catalog

def load_catalog_from_file(filepath,catalog):
    if len(catalog) > 0:
        print(f"Loading now, will overwrite the current catalog, \n{render_catalog(catalog)}\nPlease save it to the file before loading again")
        return catalog
    else:
        try:
            with open(filepath,'r') as f:
                output = f.read()
                return eval(output)
        except FileNotFoundError:
            print("Please Add Books to the catalog first.")
            return catalog
        
            
            
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
    file = "books.txt"
    catalog = load_catalog_from_file(file,[])
    if type(catalog) == type(None):
        catalog = []
    counter = len(catalog)
    subprocess.run('cls', shell=True)
    choice = menu()
    while not choice == 8:
        counter = len(catalog)
        if choice == 0:
            subprocess.run('cls', shell=True)
        elif choice == 1:
            catalog = add_book_entry(catalog,counter+1)
        elif choice == 2:
            catalog = render_catalog(catalog)
        elif choice == 6:
            catalog = sync_catalog_to_file(file,catalog)
        elif choice == 7:
            catalog = load_catalog_from_file(file,catalog)
        choice = menu()
    print("*"*92,"\n")
    print("x"*18,"THANK YOU FOR USING THE BOOK CATALOG MANAGEMENT SYSTEM","x"*18)



if __name__ == "__main__":
    main()