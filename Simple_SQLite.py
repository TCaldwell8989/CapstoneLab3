import sqlite3
import sys

def display_menu_get_selection():
    '''Display user menu and handle user selection'''

    print('''
        1. Add Data
        2. Search
        3. Update
        4. Delete
        5. Quit
    ''')
    selection = input('Enter your choice: ')
    return selection

def add_data(cur):
    '''Ask user for information for new record'''
    name = input('Enter Name: ')
    country = input('Enter Country: ')
    catches = int(input('Enter Number of Catches: '))
    cur.execute('insert into chainsaw_juggling VALUES (?, ?, ?)', (name, country, catches))
    print("Successfully Added {} into the database".format(name))

def search_data(cur):
    '''Ask user for information to search by'''
    print('''
            Search By
            1. Name
            2. Country
            3. Number of Catches
        ''')
    selection = input("Enter your choice: ")
    if selection == '1':
        dbname = input('Enter Name: ')
        output = cur.execute('select * from chainsaw_juggling where Name=?', (dbname,))
        for row in output:
            print(row)
    elif selection == '2':
        dbcountry = input('Enter Country: ')
        output = cur.execute('select * from chainsaw_juggling where Country=?', (dbcountry,))
        for row in output:
            print(row)
    elif selection == '3':
        dbcatches = int(input('Enter Catches: '))
        output = cur.execute('select * from chainsaw_juggling where Catches=?', (dbcatches,))
        for row in output:
            print(row)
    else:
        print('Please enter a valid selection')

def update_data(cur):
    '''Updates amount of catches a person has'''
    name = input('Enter Name for Update: ')
    catches = int(input('Enter new amount of catches: '))
    cur.execute('update chainsaw_juggling set Catches=? where Name=?', (catches, name))
    output = cur.execute('select * from chainsaw_juggling where Name=?', (name,))
    for row in output:
        print(row)

def delete_data(cur):
    '''Deletes data from table'''
    name = input('Enter Name to Delete: ')
    country = input('Enter their Country: ')
    cur.execute('delete from chainsaw_juggling where Name=? and Country=?', (name, country))
    print('Successfully deleted {} from {} from the database'.format(name, country))

# Main Entry of Program
def main():

    while True:
        # Creates or opens database file
        db = sqlite3.connect('chainsaw_juggling_records.db')

        # Create a cursor object to handle operations
        cur = db.cursor()

        # Create a table if not exists...
        cur.execute('create table if not exists chainsaw_juggling ("Name" text, Country text, "Catches" int)')

        selection = display_menu_get_selection()

        if selection == '1':
            add_data(cur)
            db.commit()

        elif selection == '2':
            search_data(cur)

        elif selection == '3':
            update_data(cur)
            db.commit()

        elif selection == '4':
            delete_data(cur)
            db.commit()

        elif selection == '5':
            sys.exit()
        else:
            print('Please enter a valid selection')

main()





