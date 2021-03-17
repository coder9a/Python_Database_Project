from Project import DBhelper


def main():
    db = DBhelper()
    while True:
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()

        try:
            choice = int(input())
            if (choice == 1):
                # insert user
                uid = int(input("Enter user id "))
                username = input("Enter user name ")
                userphone = input("Enter user phone ")
                db.insert_user(uid, username, userphone)

            elif (choice == 2):
                # show all user
                db.fetch_all()

            elif (choice == 3):
                # delete user
                userid = int(input("Enter userID to which you want to delete "))
                db.delete_user(userid)

            elif (choice == 4):
                # update user
                uid = int(input("Enter user id "))
                username = input("Enter new user name ")
                userphone = input("Enter new user phone ")
                db.update_user(uid, username, userphone)

            elif choice == 5:
                break
            else:
                print("invalid Input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid details ! Try again")


if __name__ == '__main__':
    main()
