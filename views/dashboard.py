from views.media_type_view import view_media_type
choice=-1

while(choice!=0):
    print("Press 1 to deal with media types...")
    print("Press 2 to deal with media tracks...")
    print("Press 3 to deal with media genre...")
    print("Press 99 to Exit...")
    choice=int(input("Enter Your Choice"))
    if choice==1:
        media_type_menu()
    elif choice==2:
        print("media tracks coming soon")
    elif choice==3:
        print("genre coming soon")
    elif choice==99:
        choice=0
    else:
        print("enter a valid choice")
                        
def media_type_menu():
        menu_choice=-1
        while menu_choice!=0:
            print("Press 1 to get media type list...")
            print("Press 2 to get media type by id...")
            print("Press 3 to create media type...")
            print("Press 4 to update media type...")
            print("Press 5 to delete media type...")
            print("Press 6 to go to main menu...")
            menu_choice=int(input("Enter Your mendia type Choice"))
            if menu_choice==1:
                view_media_type()
            elif menu_choice==2:
                print("get media type feature coming soon...")
            elif menu_choice==3:
                print("create media type feature coming soon...")
            elif menu_choice==4:
                print("update media type feature coming soon...")
            elif menu_choice==5:
                print("delete media type feature coming soon...")
            elif menu_choice==6:
                menu_choice=0
            else:
                print("please enter a valid menu choice...")            