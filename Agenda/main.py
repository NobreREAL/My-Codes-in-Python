import mysql.connector as db


class Agenda:

    def __init__(self):
        self.bank = db.connect(host="localhost",
                               database="dbAgenda",
                               user="root",
                               password="")

    def create_contempt(self):
        cursor = self.bank.cursor()
        name = input("Type the name of the contact:")
        email = input("Type the email of the contact:")
        number = input("Type the number of the contact:")

        if len(name) > 12 or len(email) > 50 or len(number) > 15:
            print("Quantity of chars is invalid, please, read up:")
            print("Name limit of char is up to 12 chars")
            print("Email limit of char is up to 50 chars")
            print("Number limit of char is up to 15 chars")
        else:
            cursor.execute(f"insert into tbContato (nome, email, numero) values ('{name}', '{email}', '{number}')")
            self.bank.commit()

            print("Data inserted on table!")

            input("Press enter to continue... ")

    def read_contempt(self):
        cursor = self.bank.cursor()

        cursor.execute("Select * from tbContato")

        result = cursor.fetchall()

        for row in result:
            print(f"ID: {row[0]}, NAME: {row[1]}, EMAIL:  {row[2]}, NUMBER:  {row[3]}\n")

        input("Press enter to continue... ")

    def update_contempt(self):
        cursor = self.bank.cursor()

        verify = False

        id_contact = int(input("Type the ID of the contact to update:"))

        cursor.execute("Select id from tbContato")

        result = cursor.fetchall()

        for ids in result:

            if id_contact == ids[0]:
                verify = True
                break

        if verify:
            print("Id is valid, proceed to the update:")
        else:
            print("Id is invalid, try again!")
            input("Press enter to continue... ")
            return

        name = input("Type the name of the contact:")
        email = input("Type the email of the contact:")
        number = input("Type the number of the contact:")

        if len(name) > 12 or len(email) > 50 or len(number) > 15:
            print("Quantity of chars is invalid, please, read up:")
            print("Name limit of char is up to 12 chars")
            print("Email limit of char is up to 50 chars")
            print("Number limit of char is up to 15 chars")
        else:
            cursor.execute(f"Update tbContato set nome = '{name}', email = '{email}', numero = "
                           f"'{number}' where id = '{id_contact}'")

            self.bank.commit()

            print("Data update!")

            input("Press enter to continue... ")

    def delete_contempt(self):
        cursor = self.bank.cursor()

        verify = False

        id_contact = int(input("Type the id of the contact to delete it up:"))

        cursor.execute("Select id from tbContato")

        result = cursor.fetchall()

        for ids in result:

            if id_contact == ids[0]:
                verify = True
                break

        if verify:
            cursor.execute(f"delete from tbContato where id = '{id}'")
            self.bank.commit()
            print("Contact is deleted!")

            input("Press enter to continue... ")

        else:
            print("Id is invalid, try again!")
            input("Press enter to continue... ")
            return


job = Agenda()
while True:
    print("\n" * 30, end="")
    print("=" * 30)
    print("1- Create contact on bank")
    print("2- Read the contact on bank")
    print("3- Update the contact on bank")
    print("4- Delete the contact on bank")
    print("5- Exit the application")
    print("=" * 30)

    try:
        opt = int(input("\nType the opt of you choice:"))

        if opt == 1:
            job.create_contempt()
        elif opt == 2:
            job.read_contempt()
        elif opt == 3:
            job.update_contempt()
        elif opt == 4:
            job.delete_contempt()
        elif opt == 5:
            break
        else:
            print("Option typed is invalid! try again.")

    except:
        print("You typed a wrong option on input, try again.")
