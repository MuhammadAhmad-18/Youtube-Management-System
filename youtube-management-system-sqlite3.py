import sqlite3

# database connecction
conn = sqlite3.connect("youtube.db")
cursor = conn.cursor()

# creation of table
cursor.execute("""create table if not exists vedios_list(
               id integer primary key autoincrement,
               vedio_title varchar(50) not null, 
               vedio_duration varchar(20) not null,
               vedio_link varchar(100) not null,
               vedio_author varchar(20) not null
               )""")

# function to list the table


def list_vedios():
    cursor.execute("select * from vedios_list")
    rows = cursor.fetchall()
    for rows in rows:
        print(rows)


def list_titles():
    cursor.execute("select vedio_title from vedios_list")
    rows = cursor.fetchall()
    return rows

# function to add vedio to the table


def add_vedio(vedio_name, vedio_time, vedio_link, vedio_author):
    cursor.execute(
        "insert into vedios_list(vedio_title,vedio_duration, vedio_link, vedio_author) values (?,?,?,?)", (vedio_name, vedio_time, vedio_link, vedio_author))
    conn.commit()
    print("Vedio Added Successfully!")

# function to update values in the table


def update_vedio():
    updating_vedio_name = input("Enter Vedio Title you want to CHANGE: ")

# Checks if vedio is present or not
    isPresent = False

    list_of_titles = list_titles()

    for i in list_of_titles:
        if (i[0] == updating_vedio_name):
            isPresent = True
            break

    if (isPresent):
        while (True):
            print("What you want to change?")
            print("[1] Name")
            print("[2] Time")
            print("[3] Link")
            print("[4] Author")
            input_choice = input("Enter your choice: ")

            match input_choice:
                case '1':
                    new_name = input("Enter new name: ")
                    cursor.execute(
                        '''update vedios_list set vedio_title = ? where vedio_title = ?''', (new_name, updating_vedio_name))
                    conn.commit()

                case '2':
                    new_time = input("Enter new time duration: ")
                    cursor.execute(
                        '''update vedios_list set vedio_duration = ? where vedio_title = ?''', (new_time, updating_vedio_name))
                    conn.commit()
                case '3':
                    new_link = input("Enter new link: ")
                    cursor.execute(
                        '''update vedios_list set vedio_link = ? where vedio_title = ?''', (new_link, updating_vedio_name))
                    conn.commit()
                case '4':
                    new_author = input("Enter new author: ")
                    cursor.execute(
                        '''update vedios_list set vedio_author = ? where vedio_title = ?''', (new_author, updating_vedio_name))
                    conn.commit()

            print("===| Updated Successfully |===")
            break
    else:
        print("Vedio Title Not Found!")

# function to delete vedio(row) from the table


def delete_vedio():
    deleting_vedio_name = input("Enter Vedio Title you want to DELETE: ")

# Checks if vedio is present or not
    isPresent = False

    list_of_titles = list_titles()

    for i in list_of_titles:
        if (i[0] == deleting_vedio_name):
            isPresent = True
            break

    if (isPresent):
        cursor.execute("delete from vedios_list where vedio_title = ?",
                       (deleting_vedio_name,))
        conn.commit()
        print("Vedio Deleted Successfully!")
    else:
        print("Vedio Not Found!")

# main function


def main():

    while (True):
        print("\t======| YOUTUBE MANAGER APP |=====")
        print("\t[1] LIST ALL THE VEDIOS")
        print("\t[2] ADD VEDIO")
        print("\t[3] UPDATE VEDIO")
        print("\t[4] DELETE VEDIO")
        print("\t[5] EXIT")

        usersChoice = input("Enter your choice: ")

        match usersChoice:
            case '1':
                list_vedios()
            case '2':
                vedio_name = input("Enter vedio name: ")
                vedio_time = input("Enter vedio time: ")
                vedio_link = input("Enter vedio link: ")
                vedio_author = input("Enter vedio author: ")
                add_vedio(vedio_name, vedio_time, vedio_link, vedio_author)
            case '3':
                update_vedio()
            case '4':
                delete_vedio()
            case '5':
                break
            case _:
                print("WARNING! --> Invalid Input")


# calling the main function
main()
