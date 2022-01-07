##################################
##################################
#                       Importing Modules                            #
#                                                                              #
##################################

from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import os
import datetime

##################################

#Defining main screen


#This Is The Login Screen
# This screen Contain 3 Buttons

# 1) Admin Login :
# Admin login Button Will Read The Data From The ''Admin'' file
# and if the password given is correct the user will be able to login and viceversa
# You can change the admin password manually by change it in the file

# 2) User Login:
# user login screen will recive data from ''users'' file if the username exist
# user password will be checked and if both correct user will be able to login

# 3) Exit:
# As from the name this button will Allow you to exit the program

#################################################
#################################################
#                                                                                                                  #
#                                        Main login Screen Started                                      #
#                                                                                                                  #
#################################################

def main_screen():
    global win    #globalinzing window
    win = Tk()
    win.title("Library Management System")
    win.geometry(center(win,799,560))
    win.resizable(0,0)
    bg_image_main_screen()

    win.iconbitmap(r'pics/icon.ico')
    #---------------------Admin login Button Section-------------------#
    
    #Making an admin image object
    admin_btn_img = PhotoImage (file = r"pics/admin.png")
    
    #creating admin login button
    admin_login_btn = Button(
        win,
        image = admin_btn_img,
        border = 0,
        command = open_admin_login_window
        )

    #---------------------------------------------------------------#

    #---------------------User login Button Section-------------------#

    #making User login image object
    user_btn_img = PhotoImage (file = r"pics/login.png")

    #creating user login button
    user_login_btn = Button(
        win,
        image = user_btn_img,
        border = 0,
        command = open_user_login_window
        )
    
    #--------------------------------------------------------------------#

    #---------------------Exit Button Section-------------------#

    #making User Exit image object
    exit_btn_img = PhotoImage (file = r"pics/exit-button.png")

    #creating user Exit button
    exit_login_btn = Button(
        win,
        image = exit_btn_img,
        border = 0,
        command = destroy_mainscreen
        )
    Label(win,text = 'Admin Login', anchor = N,font = ("Arial","15","bold")).grid(row = 2,column = 0 ) #Button 1
    Label(win,text = 'User Login', anchor = N,font = ("Arial","15","bold")).grid(row = 2,column = 1 )    # Button 2
    Label(win,text = 'Exit', anchor = N,font = ("Arial","15","bold")).grid(row = 2,column = 2 )             # Button 3
    #--------------------------------------------------------------------#

    #---------------Aligning all objects of main screen---------------#

    #background image is aligned in the bg_image_main_screen() fuction
    admin_login_btn.grid(row = 1,column = 0)
    user_login_btn.grid(row = 1,column = 1)
    exit_login_btn.grid(row = 1,column = 2)
    
    #--------------------------------------------------------------------#
    
    win.mainloop()

#--------------------------------Function for background image of main screen---------------------------------#

def bg_image_main_screen():
    global main_bg_image  #globalinzing the image so that it apperas in the screen
    
    canvas = Canvas(win, width=799 , height = 399 , bg = "black")   #setting width and height of canvas
    
    canvas.grid(row = 0 ,columnspan = 3)
    main_bg_image = PhotoImage(file = r"pics/Background.png")
    canvas.create_image(0,0,image = main_bg_image, anchor=NW)

#--------------------------------------------------------------------------------------------------------------------#

#####################################
#####################################
#                                                                                     #
#               Commands for buttons of main screen                 #
#####################################


#--------------For admin Button------------------#
    
def open_admin_login_window():
    global admin_login_screen
    global admin_login_page_img
    global admin_login_btn_img
    global admin_pass_entry, admin_pass_entry_var
    
    admin_login_screen = Toplevel(win)
    admin_login_screen.title("Admin login")
    admin_login_screen.geometry(center(admin_login_screen,400,370))
    admin_login_screen.resizable(0,0)
    admin_login_screen.configure(background = "lightblue")
    admin_login_screen.iconbitmap(r'pics/icon.ico')

    admin_login_page_img = PhotoImage(file=r"pics/admin.png")

    Label(
        admin_login_screen,
        image = admin_login_page_img,
        border = 0,
        bg = "lightblue"
        ).pack(pady = 10)

    Label(
        admin_login_screen,
        text = "Admin Login",
        font = ("Helvetica", 20, "bold"),
        bg = "lightblue"
        ).pack()
    
    Label(
        admin_login_screen,
        text = "Enter Password*",
        font = ("Helvetica", 10, "bold"),
        bg = "lightblue"
        ).pack(pady = 20)

    admin_pass_entry_var = StringVar()
    admin_pass_entry = ttk.Entry(
        admin_login_screen,
        font = ("Symbol", 15, "normal"),
        show = "*",
        textvariable = admin_pass_entry_var
        )
    admin_pass_entry.pack(ipady = 2, ipadx = 15)
    admin_pass_entry.focus()  #using so that the cursor is on the entry box
    
    #creating admin login button image object
    admin_login_btn_img = PhotoImage(file = r"pics/login_button.png")

    #------Admin Check Button----------#
    admin_check_btn = Button(
        admin_login_screen,
        image = admin_login_btn_img,
        border = 0,
        bg = "lightblue",
        command = admin_login
        )
    admin_check_btn.pack(pady = 10)
    #-------------------------------------#
        
#---------------------------------------------------#

#---------------------For User Login Button-----------------------#

def open_user_login_window():
    global user_login_screen
    global user_login_page_img
    global user_login_btn_img
    global user_name_login_entry_var , user_pass_login_entry_var
    global user_name_login_entry, user_pass_login_entry
    
    
    user_login_screen = Toplevel(win)
    user_login_screen.title("User login")
    user_login_screen.geometry(center(user_login_screen,400,430))
    user_login_screen.resizable(0,0)
    user_login_screen.configure(background = "lightblue")
    user_login_screen.iconbitmap(r'pics/icon.ico')

    user_login_page_img = PhotoImage(file=r"pics/login.png")

    Label(
    user_login_screen,
    image = user_login_page_img,
    border = 0,
    bg = "lightblue"
    ).pack(pady = 10)

    Label(
    user_login_screen,
    text = "User Login",
    font = ("Helvetica", 20, "bold"),
    bg = "lightblue"
    ).pack()

    Label(
    user_login_screen,
    text = "Enter User Name*",
    font = ("Helvetica", 10, "bold"),
    bg = "lightblue"
    ).pack(pady = 10)

    #------Entry box for user name---------#
    user_name_login_entry_var = StringVar()
    user_name_login_entry = ttk.Entry(
        user_login_screen,
        font = ("Helvetica", 15, "normal"),
        textvariable = user_name_login_entry_var
        )
    user_name_login_entry.pack(ipady=2,ipadx=15)
    user_name_login_entry.focus()     #using so that the cursor is on the entry box
    #----------------------------------------#
    
    Label(
    user_login_screen,
    text = "Enter Password*",
    font = ("Helvetica", 10, "bold"),
    bg = "lightblue"
    ).pack(pady = 10)

    #--------User name password Entrybox---------#
    user_pass_login_entry_var = StringVar()
    user_pass_login_entry = ttk.Entry(
        user_login_screen,
        font = ("Symbol", 15, "normal"),
        show = "*",
        textvariable = user_pass_login_entry_var
        )
    user_pass_login_entry.pack(ipady=2,ipadx=25)
    #---------------------------------------------------#

    #creating User login button image object
    user_login_btn_img = PhotoImage(file = r"pics/login_button.png")

    #------User Check Button----------#
    user_check_btn = Button(
        user_login_screen,
        image = user_login_btn_img,
        border = 0,
        bg = "lightblue",
        command = login
        )
    user_check_btn.pack(pady = 10)
    #-------------------------------------#
    
#-------------------------------------------------------------#



    

#----------------Commands for buttons of user login screen-------------------- #

def login():
    #getting all values from login screen
    username_login = user_name_login_entry_var.get()
    password_login = user_pass_login_entry_var.get()
    #--------------------------------#
    
    users_list = os.listdir(r'users') #list of users

    if username_login in users_list:
        
        #Geting password from file
        with open(r'users/'+username_login,"r") as f:
            user_password = f.readline()
            user_password = user_password.rstrip("\n")
            
        if password_login == user_password:
            messagebox.showinfo("Login Success","Login Successful")
            
            get_username_after_userlogin(username_login)  #This Function store Username So that it is used After User Login
                                                                                  # So the user will not enter his/her username again and agian
            
            destroy_mainscreen()   #Destroying Main Screen
            User_login_screen()     #Open User Login Panel Screen
            
        else:
            messagebox.showerror("Incorrect Password","Incorrect Password")
            user_login_screen_reset()
            
    else:
        messagebox.showerror("Username not found","User name doesn't exist")
        user_login_screen_reset()
        
    

#------------------------------------------------------------------------------------- #

#----------------Commands for buttons of admin login screen-------------------- #

def admin_login():
    admin_login_pass =   admin_pass_entry_var.get()

    admin_pass_path = r'admin/admin_password'
    
    with open(admin_pass_path, "r") as f:
        admin_password = f.readline()
        admin_password = admin_password.rstrip("\n")
        
    if admin_login_pass == admin_password:
        messagebox.showinfo("Login Successful","You are Successfully Login")
        destroy_mainscreen()
        admin_panel()
        
    else :
        messagebox.showerror("Incorrect Password","Incorrect Password")
        admin_login_screen_reset()

    

    
#-------------------------------------------------------------------------------------#        


#---------------------------------------------------------------------------------------------------- #



######################################################
#                                         End of  Main Screen Section                                               #
######################################################  


###################################################################
###################################################################
#                                                                                                                                                              #
#                                                      Making Admin Pannel Window                                                             #
#                                                                                                                                                              #
###################################################################
###################################################################

#Describing Admin Pannel Window Screen
#This Screen Has 9 Button

# 1) Search Book Button:

# In This window you can search Books Also You can see the list of books
# it takes data from file "books" and display it

# 2)Add Book Button:
#In This window you can add Books in the library with Book name auther name and book quantity & book id
# Data of books will be saved in the file name "books"

# 3)Edit Book Record:
# In this window user can Edit Books Data He will first search the data from the entry box
#and then click on the edit button to edit the screen

# 4)Issue book Screen:
#In this Screen Admin can issue Book to the user
#Admin can also reissue the book to the user
#For issueing this program will first check the availability in the library
#if book quantity is less then 1 book will not be issued
#After it will check that how many books user has issued for him self
#If he issued More then 2 books he can't issue more books
#If the user has issued the same book he can't issue the same book again
#for reissing first book will be issued
#You can't reissue the book If the user has fine on him


# 5)show user info:
#In this screen All user info would be displayed
#There would be a list in which all user name would be displayed
#Admin can select a user and can check his/her data
#Like password,Email,Gender,type,and how many books the user has issued for him self

# 6)remove user:
#In this Screen admin can remove a user
#Admin would need to search the user
#If the user has issued book for him self the user can not be removed

# 7)Add User:
#In this Window Admin can add a user
#a username,email,password,gender,and usertype will be required

#If the username is less then 4 caracters an error would be displayed
#If a username enter that is already exist an error would be displayed
#If the password is less then 8 characters an error would be displayed
#If the email is other then yahoo and gmail an error would be displayed


# 8)Return Book:
#In this Window  issued book would be returned
#You can also see all the fine collected by the Library
#admin would search the username of user
#If user has issued book for him self the book would be shown in the list box
# else an error would be displayed that user did'nt issue any book yet
#If user issue the book with in due date the book would be return without any fine collected
#Else a window will be appeared that give fine



# 9)LOGOUT:
#After pressing the button admin panel screen would be destroyed and main screen would be displayed


def admin_panel():
    global admin_panel_screen

    admin_panel_screen = Tk()
    admin_panel_screen.geometry('799x700+0+0')
    admin_panel_screen.title("Admin Panel")
    admin_panel_screen.configure(background = "lightblue")
    admin_panel_screen.resizable(0,0)

    #Adding Icon To The window
    admin_panel_screen.iconbitmap(r'pics/icon.ico')

    #----------Picture For header-----------------#
    admin_header_pic = PhotoImage(file = r"pics/Admin_header.png")
    Label(admin_panel_screen,
          image = admin_header_pic).grid(row = 0,columnspan = 3)
    #------------------------------------------------#

    #-------------Making Buttons for Admin Panel Screen-----------------#

    # Button 1
    #-----Button For search books--------#

    search_book_pic_admin = PhotoImage(file=r"pics/search_books.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           image = search_book_pic_admin,
           command = search_book_for_admin).grid(row = 1,column = 0,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Seach Books",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 2,column = 0)

    #---------------------------------------#

    # Button 2
    #-----Button For add books--------#
    
    add_book_pic = PhotoImage(file=r"pics/add_books.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           image = add_book_pic,
           command = Add_books).grid(row = 1,column = 1,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Add Books",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 2,column = 1)

    #---------------------------------------#

    # Button 3
    #-----Button For edit books--------#

    edit_book_pic = PhotoImage(file=r"pics/Edit_books.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           image = edit_book_pic,
           command = edit_books).grid(row = 1,column = 2,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Edit Books",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 2,column = 2)

    #---------------------------------------#

    # Button 4
    #-----Button For issue books--------#

    issue_book_pic = PhotoImage(file=r"pics/issue_book.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           image = issue_book_pic,
           command = open_issue_book_window).grid(row = 3,column = 0,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Issue Books",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue",).grid(row = 4,column = 0)

    #---------------------------------------#

    # Button 5
    #-----Button For Users Record--------#

    users_record_pic = PhotoImage(file=r"pics/search_users.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           image = users_record_pic,
           command = open_userrecord_window).grid(row = 3,column = 1,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Users Record",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 4,column = 1)

    #---------------------------------------#

    # Button 6
    #-----Button For Remove Users --------#

    remove_user_pic = PhotoImage(file=r"pics/remove_user.png")    
    Button(admin_panel_screen ,
           bg = "lightblue",
           border = 0,
           command = remove_user_screen_button_clicked,
           image = remove_user_pic).grid(row = 3,column = 2,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Remove User",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 4,column = 2)

    #---------------------------------------#

    # Button 7
    #---------------------User signup Button Section-------------------#

    #making User signup image object
    signup_btn_img = PhotoImage (file = r"pics/add-user.png")

    #creating user login button
    signup_login_btn = Button(
        admin_panel_screen,
        image = signup_btn_img,
        bg = "lightblue",
        border = 0,
        command = open_registration_window
        )
    signup_login_btn.grid(row = 5,column = 0,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Add User",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 6,column = 0)

     # Button 8
    #---------------------Book Return Button Section-------------------#

    #making Return image object
    return_book_btn_img = PhotoImage (file = r"pics/book_return.png")

    #creating Return button
    return_book_btn = Button(
        admin_panel_screen,
        image = return_book_btn_img,
        bg = "lightblue",
        border = 0,
        command = return_book_scrn_btn_clicked
        )
    return_book_btn.grid(row = 5,column = 1,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Book Return",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 6,column = 1)
    

    #---------------------------------------#

     # Button 9
    #---------------------logout Button Section-------------------#

    #making logout image object
    logout_btn_img = PhotoImage (file = r"pics/logout_btn.png")

    #creating admin logout button
    logout_book_btn = Button(
        admin_panel_screen,
        image = logout_btn_img,
        bg = "lightblue",
        border = 0,
        command = logout_admin_win
        )
    logout_book_btn.grid(row = 5,column = 2,pady = (10,0) )

    Label(admin_panel_screen,
          text = "Logout",
          font = ('comic sans ms',18,"bold"),
          bg = "lightblue").grid(row = 6,column = 2)
    

    #---------------------------------------#


    #--------------------------------------------------------------------------#
    admin_panel_screen.mainloop()



###########################################
###########################################
#                                                                                                    #
#                 Making Commands for Admin Window Buttons                 #
###########################################

# Button 1
#===========================Command for Search Button===================================#

def search_book_for_admin():
    global search_admin_win
    search_admin_win = Toplevel(admin_panel_screen)
    search_admin_win.geometry(center(search_admin_win,799,550))
    search_admin_win.title("Search Books")
    search_admin_win.configure(background = "lightblue")
    search_admin_win.resizable(0,0)

    #Adding Icon To The window
    search_admin_win.iconbitmap(r'pics/icon.ico')

    global search_book_for_admin_header
    global search_books_for_admin_entrybox_var   #globalizing Entry box
    global search_book_id_label_var
    global search_book_name_label_var
    global search_book_author_name_label_var
    global search_book_quantity_label_var
    global search_books_for_admin_by_name_entrybox_var
    
    
    search_book_for_admin_header = PhotoImage(file = r'pics/search_books header.png')
    Label(search_admin_win,
          image = search_book_for_admin_header ).grid(row = 0, columnspan = 4)

    #Label For Search Entry Box
    Label(search_admin_win,
          text = "Search Books With ID :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 1, column = 0,sticky = "w",pady = "6",)

    #-------Search Books Entry Box--------#

    search_books_for_admin_entrybox_var = StringVar()
    search_books_for_admin_entrybox = ttk.Entry(
          search_admin_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = search_books_for_admin_entrybox_var
          )
    search_books_for_admin_entrybox.focus()
    search_books_for_admin_entrybox.grid(row = 1, column = 1,sticky = "w",pady = "6") 

    #-----------------------------------------#

    #-------Button For search Entry Box------#

    
    search_btn_img = PhotoImage(file = r"pics/Search.png")
    Button(search_admin_win,
           image = search_btn_img,
           bg = 'lightblue',
           border = 0,
               command = search_book_for_admin_clicked
           ).grid(row = 1, column = 2,sticky = "W")
    #--------------------------------------------#

    #Label For Search Entry Box
    Label(search_admin_win,
          text = "Search Books With Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 2, column = 0,sticky = "w",pady = "6",)

    #-------Search Books with name Entry Box--------#

    search_books_for_admin_by_name_entrybox_var = StringVar()
    search_books_for_admin_by_name_entrybox = ttk.Entry(
          search_admin_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = search_books_for_admin_by_name_entrybox_var
          )

    search_books_for_admin_by_name_entrybox.grid(row = 2, column = 1,sticky = "w",pady = "6") 

    #-----------------------------------------#

    #-------Button For search Entry Box------#

    Button(search_admin_win,
           image = search_btn_img,
           bg = 'lightblue',
           border = 0,
               command = search_book_for_admin_by_name_clicked
           ).grid(row = 2, column = 2,sticky = "W")
    #--------------------------------------------#
    

    #-------Button For get books list Entry Box------#

    list_of_books_btn_img = PhotoImage(file = r"pics/List_of_books.png")
    Button(search_admin_win,
           image = list_of_books_btn_img,
           border = 0,
           bg = "lightblue",
               command = show_book_list
           ).grid(row = 3, column = 2,sticky = "W") 

    #--------------------------------------------#

    #Label For heading
    Label(search_admin_win,
          text = "Book Details :",
          font= ('comic sans ms',25,"bold"),
          bg = "lightblue",
          ).grid(row = 3, column = 0,sticky = "w",pady = "6",)

    #------------Section For book Id-------------#
    
    #Book ID Descripter
    Label(search_admin_win,
          text = "Book ID :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 4, column = 0,sticky = "w",pady = "6",)

    #Book Id Label
    search_book_id_label_var = StringVar()
    search_book_id_label = ttk.Entry(search_admin_win,
          textvariable = search_book_id_label_var,
          font= ('comic sans ms',13,"bold"),
          state = 'readonly',
          )
    search_book_id_label.grid(row = 4, column = 1,sticky = "w",pady = "6",ipadx = "45",ipady = "5")
    #---------------------------------------------#

    #------------Section For book Name-------------#
    
    #Book Name Descripter
    Label(search_admin_win,
          text = "Book Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 5, column = 0,sticky = "w",pady = "6",)

    #Book Name Label
    search_book_name_label_var = StringVar()
    search_book_name_label = ttk.Entry(search_admin_win,
          textvariable = search_book_name_label_var,
          font= ('comic sans ms',13,"bold"),
          state = 'readonly'
          )
    search_book_name_label.grid(row = 5, column = 1,sticky = "w",pady = "6",ipadx = "45",ipady = "5")
    #---------------------------------------------#

    #------------Section For Author Name-------------#
    
    #Book Author Name Descripter
    Label(search_admin_win,
          text = "Author Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 6, column = 0,sticky = "w",pady = "6",)

    #Book Author Name Label
    search_book_author_name_label_var = StringVar()
    search_book_author_name_label = ttk.Entry(search_admin_win,
          textvariable = search_book_author_name_label_var,
          font= ('comic sans ms',13,"bold"),
          state = "readonly"
          )
    search_book_author_name_label.grid(row = 6, column = 1,sticky = "w",pady = "6",ipadx = "45",ipady = "5")
    #---------------------------------------------#

    #------------Section For book Quantity-------------#
    
    #Book Name Descripter
    Label(search_admin_win,
          text = "Book Quantity :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 7, column = 0,sticky = "w",pady = "6",)

    #Book Name Label
    search_book_quantity_label_var = StringVar()
    search_book_quantity_label = ttk.Entry(search_admin_win,
          textvariable = search_book_quantity_label_var,
          font= ('comic sans ms',13,"bold"),
          state = 'readonly',
          )
    search_book_quantity_label.grid(row = 7, column = 1,sticky = "w",pady = "6",ipadx = "45",ipady = "5")
    #---------------------------------------------#


    search_admin_win.mainloop()

#Making Book List function helping for search book screen
def show_book_list():
    global book_list_win
    
    book_list_win = Toplevel(search_admin_win)
    book_list_win.geometry(center(book_list_win,400,400))
    book_list_win.title("Books List")

    #Adding Icon To The window
    book_list_win.iconbitmap(r'pics/icon.ico')

    #Making List Box For book Display
    lbx = Listbox(
        book_list_win,
        font= ('comic sans ms',16,"bold"),
        )
    lbx.pack(side = 'left',fill = 'both',expand = True)   

    #For Heading
    lbx.insert(0,"ID  -  Name")

    #Adding data to book
    book_list = os.listdir(r"books_name/")
    for index,data in enumerate(book_list,1):
        with open(r"books_name/"+data ,'r') as f:
            book_id_num = f.readline().strip('\n')
            lbx.insert(index,book_id_num+'- '+data)
        
    #making scrollbar for listbox
        
    sbr = Scrollbar(
        book_list_win,
        )
    sbr.pack(side = 'right' , fill = "y")

    #Making Command So that both Scrollbar and listbox can see each others
    sbr.config(command = lbx.yview)
    lbx.config(yscrollcommand = sbr.set)
    
    book_list_win.mainloop()
#------------------------------------------------------#


# Button 2
#===========================Command for Add Books Button================================#

def Add_books():
    global addbooks_win
    addbooks_win = Toplevel(admin_panel_screen)
    addbooks_win.geometry(center(addbooks_win,799,500))
    addbooks_win.title("Add Books")
    addbooks_win.configure(background = "lightblue")
    addbooks_win.resizable(0,0)

    #Adding Icon To The window
    addbooks_win.iconbitmap(r'pics/icon.ico')

    global addbooks_win_header
    global entry_box_for_addbook_id_var, entry_box_for_addbook_id
    global entry_box_for_addbook_name_var, entry_box_for_addbook_name
    global entry_box_for_addbook_author_name_var,entry_box_for_addbook_author_name
    global entry_box_for_addbook_quantity_var,entry_box_for_addbook_quantity

    #Header For Screen
    addbooks_win_header = PhotoImage(file = r'pics/addbooks_header.png')
    Label(addbooks_win,
          image = addbooks_win_header ).grid(row = 0, columnspan = 2)

    #Descrptive header
    Label(addbooks_win,
          text = "Enter Book Details :",
          font= ('comic sans ms',25,"bold"),
          bg = "lightblue",
          ).grid(row = 1, column = 0,sticky = "w",pady = "6",)

#----------------Section For Book Id----------------------#
    #Label for book Id
    Label(addbooks_win,
          text = "Enter Book ID :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 2, column = 0,sticky = "w",pady = "6",)

    #Entry Box For Enter Book ID
    entry_box_for_addbook_id_var = StringVar()
    entry_box_for_addbook_id = ttk.Entry(addbooks_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = entry_box_for_addbook_id_var                               
          )
    entry_box_for_addbook_id.focus()
    entry_box_for_addbook_id.grid(row = 2, column = 1,sticky = "W",pady = "6")
    
#-----------------------------------------------------------#

#----------------Section For Book Name----------------------#
    #Label for book name
    Label(addbooks_win,
          text = "Enter Book Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 3, column = 0,sticky = "w",pady = "6",)

    #Entry Box For Enter Book name
    entry_box_for_addbook_name_var = StringVar()
    entry_box_for_addbook_name = ttk.Entry(addbooks_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = entry_box_for_addbook_name_var                                 
          )
    entry_box_for_addbook_name.grid(row = 3, column = 1,sticky = "W",pady = "6")
    
#-----------------------------------------------------------#

#----------------Section For Book Author Name----------------------#
    #Label for book author name
    Label(addbooks_win,
          text = "Enter Author Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 4, column = 0,sticky = "w",pady = "6",)

    #Entry Box For Enter Book author name
    entry_box_for_addbook_author_name_var = StringVar()
    entry_box_for_addbook_author_name = ttk.Entry(addbooks_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = entry_box_for_addbook_author_name_var
          )
    entry_box_for_addbook_author_name.grid(row = 4, column = 1,sticky = "W",pady = "6")
    
#-----------------------------------------------------------#

#----------------Section For Book Quantity----------------------#
    #Label for book Quantity
    Label(addbooks_win,
          text = "Enter Book Quantity :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 5, column = 0,sticky = "w",pady = "6",)

    #Entry Box For Enter Book Quantity
    entry_box_for_addbook_quantity_var = StringVar()
    entry_box_for_addbook_quantity = ttk.Entry(addbooks_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = entry_box_for_addbook_quantity_var
          )
    entry_box_for_addbook_quantity.grid(row = 5, column = 1,sticky = "W",pady = "6")
    
#-----------------------------------------------------------#

#----------Making Button For Add Book--------------#
    img_for_btn_of_add_book = PhotoImage(file = r"pics/Add_book_btn.png")
    Button(addbooks_win,
           image = img_for_btn_of_add_book,
           border = 0,
           bg = "lightblue",
           command = add_book).grid(row = 6, column = 1,sticky = "W",pady = "6")
    
#--------------------------------------------------------#
        
#------------------------------------------------------------#
    
    
    addbooks_win.mainloop()
    

#------------------------------------------------------#


# Button 3
#============================Command for Edit Books Button================================#

def edit_books():
    global editbooks_win
    editbooks_win = Toplevel(admin_panel_screen)
    editbooks_win.geometry(center(editbooks_win,799,470))
    editbooks_win.title("Edit Books")
    editbooks_win.configure(background = "lightblue")
    editbooks_win.resizable(0,0)

    #Adding Icon To The window
    editbooks_win.iconbitmap(r'pics/icon.ico')

    global editbooks_win_header
    global search_books_for_edit_entrybox_var
    global search_book_for_edit_name_label_var
    global search_book_for_edit_author_name_label_var
    global search_book_for_edit_quantity_label_var

    #Header for edit books Window
    editbooks_win_header = PhotoImage(file = r'pics/editbooks_header.png')
    Label(editbooks_win,
          image = editbooks_win_header ).grid(row = 0, columnspan = 3)

    #Label For Search Entry Box
    Label(editbooks_win,
          text = "Search Books With ID :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 1, column = 0,sticky = "w",pady = "6",)

    Label(editbooks_win,
          text = "Book Details:",
          font= ('comic sans ms',25,"bold"),
          bg = "lightblue",
          ).grid(row = 2, column = 0,sticky = "w",pady = "6",)

    #-------Search Books Entry Box--------#

    search_books_for_edit_entrybox_var = StringVar()
    search_books_for_edit_entrybox = ttk.Entry(
          editbooks_win,
          font= ('comic sans ms',18,"bold"),
          textvariable = search_books_for_edit_entrybox_var
          )
    search_books_for_edit_entrybox.focus()
    search_books_for_edit_entrybox.grid(row = 1, column = 1,sticky = "w",pady = "6") 

    #-----------------------------------------#
    #-------Button For search Entry Box------#

    search_btn_img = PhotoImage(file = r"pics/Search.png")
    Button(editbooks_win,
           image = search_btn_img,
           bg = "lightblue",
           border = 0,
           command = search_book_for_edit_clicked
           ).grid(row = 1, column = 2,sticky = "W") 

    #--------------------------------------------#

    #------------Section For book Name-------------#
    
    #Book Name Descripter
    Label(editbooks_win,
          text = "Book Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 3, column = 0,sticky = "w",pady = "6",)

    #Book Name Entrybox Display
    search_book_for_edit_name_label_var = StringVar()
    search_book_for_edit_name_label = ttk.Entry(editbooks_win,
          textvariable = search_book_for_edit_name_label_var,
          font= ('comic sans ms',13,"bold"),
          state = 'readonly',
          )
    search_book_for_edit_name_label.grid(row = 3, column = 1,sticky = "w",pady = "6",ipady = "5",ipadx = '45')
    #---------------------------------------------#

    #------------Section For Author Name-------------#
    
    #Book Author Name Descripter
    Label(editbooks_win,
          text = "Author Name :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 4, column = 0,sticky = "w",pady = "6",)

    #Book Author Name Entry box Display
    search_book_for_edit_author_name_label_var = StringVar()
    search_book_for_edit_author_name_label = ttk.Entry(editbooks_win,
          textvariable = search_book_for_edit_author_name_label_var,
          font= ('comic sans ms',13,"bold"),
          state = 'readonly',
          )
    search_book_for_edit_author_name_label.grid(row = 4, column = 1,sticky = "w",pady = "6",ipady = "5",ipadx = '45')
    #---------------------------------------------#

    #------------Section For book Quantity-------------#
    
    #Book Name Descripter
    Label(editbooks_win,
          text = "Book Quantity :",
          font= ('comic sans ms',18,"bold"),
          bg = "lightblue",
          ).grid(row = 5, column = 0,sticky = "w",pady = "6",)

    #Book Name Entrybox Display
    search_book_for_edit_quantity_label_var = StringVar()
    search_book_for_edit_quantity_label = ttk.Entry(editbooks_win,
          textvariable = search_book_for_edit_quantity_label_var,
          font= ('comic sans ms',13,"bold"),
          state = "readonly",
          )
    search_book_for_edit_quantity_label.grid(row = 5, column = 1,sticky = "w",pady = "6",ipady = "5",ipadx = '45')
    #---------------------------------------------#

    #Button To say Edit
    global Button_img_for_edit
    Button_img_for_edit = PhotoImage(file = r"pics/edit_button.png")
    Button(editbooks_win,image = Button_img_for_edit,
           bg = "Lightblue",
           command = book_edit_btn_clicked,
           border = 0).grid(row = 5, column = 2,sticky = "W")

    
    editbooks_win.mainloop()

#function for search Button In edit screen

#---------search button of edit book screen command---------------- #
def search_book_for_edit_clicked():
    try:
        global book_id_for_edit
        
        book_id_for_edit = search_books_for_edit_entrybox_var.get()
        book_list = os.listdir(r'Books')

        if book_id_for_edit in book_list:
            book_name, book_auther_name,book_quantity =  get_book_info(book_id_for_edit)


            search_book_for_edit_name_label_var.set(book_name)
            search_book_for_edit_author_name_label_var.set(book_auther_name)
            search_book_for_edit_quantity_label_var.set(book_quantity)
        else:
            messagebox.showerror("No Book Exits","No Book With ID "+book_id_for_edit+" Exist")

    except PermissionError:
        messagebox.showerror("Error","First search the book in the entry box")

#-----------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------#

# Button 4
#===============================for issue Button=======================================#

def open_issue_book_window():
    global issue_book_win
    issue_book_win = Toplevel(admin_panel_screen)
    issue_book_win.geometry(center(issue_book_win,999,600))
    issue_book_win.configure(background = "lightblue")
    issue_book_win.resizable(0,0)

    #Adding Icon To The window
    issue_book_win.iconbitmap(r'pics/icon.ico')

    #Header For Books Issue Screen
    header_pic_for_issue_book_win = PhotoImage(file = r"pics/issue_book_header.png")
    Label(issue_book_win,image = header_pic_for_issue_book_win).grid(row = 0 ,columnspan = 5)
    
    #---------book detail section --------#

    global book_detail_for_issue_var
    global book_name_for_issue
    global author_name_for_issue
    global book_quantity_for_issue
    
    #Label for Search book Id
    Label(issue_book_win,
          text = "Enter Book Id",
          bg = "lightblue",
          font = ("Arial","12",'bold') ).grid(row = 1,column = 0,pady = ("5","5"),sticky = "W")
    
    #Entry Box For Search Book Detail
    book_detail_for_issue_var = StringVar()
    book_detail_for_issue = ttk.Entry(
              issue_book_win,
              font = ("Arial","12",'bold'),
              textvariable = book_detail_for_issue_var)
    book_detail_for_issue.focus()
    book_detail_for_issue.grid(rowspan = 2,column = 0,sticky = "W")
    

    #Label For Book Details header
    Label(issue_book_win,
          text = "Book Details :",
          bg = "lightblue",
          font = ("Arial","20",'bold') ).grid(row = 4,column = 0,pady = ("20","0"),sticky = "W")

    #-------Book Name Section--------#
    book_name_for_issue = Label(issue_book_win,
          text = "Book name",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    book_name_for_issue.grid(row = 5,column = 0,pady = ("20","0"),sticky = "W")


    #------------------------------------#

    #-------Author Name Section--------#
    author_name_for_issue =  Label(issue_book_win,
          text = "Author name",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    author_name_for_issue.grid(row = 6,column = 0,pady = ("20","0"),sticky = "W")


    #------------------------------------#

    #-------Book Quantity Section--------#
    book_quantity_for_issue = Label(issue_book_win,
          text = "Book Quantity",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    book_quantity_for_issue.grid(row = 7,column = 0,pady = ("20","0"),sticky = "W")


    #----------Button To Search book details---------------#

    search_btn_img = PhotoImage(file = r"pics/Search.png")
    Button(
          issue_book_win,
          image = search_btn_img,
          border = 0,
          bg = "lightblue",
          command = search_book_info_for_issue
          ).grid(row = 8,column = 0,pady = ("30","0"),sticky = "W",)
    
    #---------------Book Detail Section End------------------------#

    #--------------User Detail Section------------#

    global User_detail_for_issue_var
    global user_email_for_issue
    global user_gender_for_issue
    global user_type_for_issue
    global Issue_date_for_issue_var
    global due_date_for_issue_var


    #Label for Search user Details
    Label(issue_book_win,
          text = "Enter User Name",
          bg = "lightblue",
          font = ("Arial","12",'bold') ).grid(row = 1,column = 1,pady = ("5","5"),sticky = "W")
    
    #Entry Box For Search User Detail
    User_detail_for_issue_var = StringVar()
    User_detail_for_issue = ttk.Entry(
              issue_book_win,
              font = ("Arial","12",'bold'),
              textvariable = User_detail_for_issue_var)
    User_detail_for_issue.grid(row = 2,column = 1,sticky = "W")

    
    #Label For User Details header
    Label(issue_book_win,
          text = "User Details :",
          bg = "lightblue",
          font = ("Arial","20",'bold') ).grid(row = 4,column = 1,pady = ("20","0"),sticky = "W")


    #------Label For user Email---------#
    user_email_for_issue = Label(issue_book_win,
          text = "User Email",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    user_email_for_issue.grid(row = 5,column = 1,pady = ("20","0"),sticky = "W")
    #-------------------------------------#
    
    #------Label For user Gender---------#
    user_gender_for_issue = Label(issue_book_win,
          text = "User Gender",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    user_gender_for_issue.grid(row = 6,column = 1,pady = ("20","0"),sticky = "W")
    #-------------------------------------#

    #------Label For user type---------#
    user_type_for_issue = Label(issue_book_win,
          text = "User Type",
          bg = "lightblue",
          font = ("Arial","12",'bold') )
    user_type_for_issue.grid(row = 7,column = 1,pady = ("20","0"),sticky = "W")
    #-------------------------------------#

    #Button For search user data
    Button(
          issue_book_win,
          image = search_btn_img,
          border = 0,
          bg = "lightblue",
          command = search_user_info_for_issue
          ).grid(row = 8,column = 1,pady = ("30","0"),sticky = "W",)


    #Button For issue Book
    image_for_issue_Button = PhotoImage(file=r"pics/issue_book_btn.png")
    Button(issue_book_win,
           image = image_for_issue_Button,
           bg = "lightblue",
           border = 0,
           command = issue_btn_clicked
           ).grid(row = 4,column = 3)


    #Button for reissue book
    image_for_reissue_Button = PhotoImage(file=r"pics/reissue_book_btn.png")
    Button(issue_book_win,
           image = image_for_reissue_Button,
           bg = "lightblue",
           border = 0,
           command = reissue_btn_clicked
           ).grid(row = 4,column = 4)
    
    #Issue Date Label


    #Label For Issue Date Display
    Label(issue_book_win,
          text = '''Issue Date
(yyyy,mm,dd)''',
          bg = 'lightblue',
          font = ("Arial","12",'bold') ).grid(row = 6,column = 3,pady = ("20","0"),sticky = "W")


    Issue_date_for_issue_var = StringVar()
    Issue_date_for_issue= ttk.Entry(issue_book_win,
          font = ("Arial","12",'bold'),
                                 state = "readonly",
                                 textvariable = Issue_date_for_issue_var)
    Issue_date_for_issue.grid(row = 6,column = 4,pady = ("5","0"),sticky = "W")

    #Label For Due Date Display
    Label(issue_book_win,
          text = '''Due Date
(yyyy,mm,dd)''',
          bg = "lightblue",
          font = ("Arial","12",'bold') ).grid(row = 7,column = 3,pady = ("20","0"),sticky = "W")

    due_date_for_issue_var = StringVar()
    due_date_for_issue = ttk.Entry(issue_book_win,
          font = ("Arial","12",'bold'),
          state = "readonly",
          textvariable = due_date_for_issue_var)
    due_date_for_issue.grid(row = 7,column = 4,pady = ("5","0"),sticky = "W")

    #---------------User Detail Section End------------------------#
    issue_book_win.mainloop()

    #------supporting command for issue book screen---#

#Command to get detail of book for issue
def search_book_info_for_issue():
    try:
        bookname,authername,bookquantity = get_book_info(book_detail_for_issue_var.get())
        
        book_name_for_issue.config(text = bookname)
        author_name_for_issue.config(text = authername)
        book_quantity_for_issue.config(text = bookquantity)

    except FileNotFoundError:
        messagebox.showerror("book doesn't exist","No Book With This ID exit")
    except PermissionError:
        messagebox.showerror("Enter Book Id","First Enter The book id")

        
def search_user_info_for_issue():
    try:
        user_name = User_detail_for_issue_var.get()
        password,email,gender,u_type = get_student_info(user_name)

        user_email_for_issue.config(text =email)
        user_gender_for_issue.config(text =gender)
        user_type_for_issue.config(text =u_type)
    except FileNotFoundError:
        messagebox.showerror("Usernot found","No user with this username exist")
    except PermissionError:
        messagebox.showerror("Enter username","First Enter The username")    
    
    
    #--------------------------------------------------------#

#---------------------------------------------------------------------#

# Button 5
#=============================for userrecord Button===================================#
def open_userrecord_window():

    global label_for_user_password_var
    global label_for_user_email_var
    global label_for_user_gender_var
    global label_for_user_type_var
    global label_for_user_type_var
    global label_for_user_issuedbooks_var
    global lbx_for_userdetails_admin
    global user_record_screen

    
    user_record_screen = Toplevel(admin_panel_screen)
    user_record_screen.title("Users Record")
    user_record_screen.geometry(center(user_record_screen,799,600))
    user_record_screen.resizable(0,0)
    user_record_screen.configure(background = "lightblue")

    #Adding Icon To The window
    user_record_screen.iconbitmap(r'pics/icon.ico')

    #Seting Header for Window############################
    user_detal_header_pic = PhotoImage(file = r"pics/usersdata_header.png")
    Label(user_record_screen,
          image = user_detal_header_pic).grid(row = 0 , columnspan = 5)
    #############################################

    #Making Frame for User List Box
    frame_for_userlist = Frame(user_record_screen,bg = "lightblue")
    frame_for_userlist.grid(rowspan = 10,column = 0 , sticky = "W")
    
    #----------Creating A listBox for User name display------#
    Label(frame_for_userlist,
          text = "Users List",
          font = ("calibri","25","bold"),
      bg = 'lightblue').grid(row = 0,column = 0 , sticky = "W",pady = "10")
    
    lbx_for_userdetails_admin = Listbox(
        frame_for_userlist,
        font = ("calibri","16","bold")
        )
    lbx_for_userdetails_admin.grid(row = 1,column = 0 , sticky = "W",ipady = "15")

    #creating scrollbar for list
    sbr = Scrollbar(
    frame_for_userlist)
    sbr.grid(row = 1,column = 0,sticky = "E",ipady="125")

    # Making Command for scrollbar for list
    sbr.config(command = lbx_for_userdetails_admin.yview )
    lbx_for_userdetails_admin.config(yscrollcommand = sbr.set)

    #-------- Making Button To get User Detail --------#

    Button_image = PhotoImage(file = r"pics/more_details_button.png")
    Button(frame_for_userlist,
               image = Button_image,
               bg = "lightblue",
               border = 0,
               font = ("calibri","15","bold"),
               command = see_details_admin_clicked
               ).grid(row = 2,column = 0,pady = 10)
        
    #--------------------------------------------------#
    #-------------------------------------------------------------#

    #--------------------user detail section----------------------#

    #Label for user detail heading
    Label(user_record_screen,
          text = "Users Details",
          font = ("calibri","25","bold"),
      bg = 'lightblue').grid(row = 1,column = 1 , sticky = "W",pady = "10")

#------section for user password-----------#
    
    Label(user_record_screen,
          text = "User's Password :",
          font = ("calibri","16","bold"),
      bg = 'lightblue').grid(row = 2,column = 1 , sticky = "W")


    label_for_user_password_var = StringVar()
    label_for_user_password = ttk.Entry(user_record_screen,
          font = ("calibri","13","bold"),
          textvariable = label_for_user_password_var,
          state = 'readonly',)
    label_for_user_password.grid(row = 2,column = 2 , sticky = "W",ipadx = '15')
    #-----------------------------------#

#------section for user email-----------#
    
    Label(user_record_screen,
          text = "User's Email :",
          font = ("calibri","16","bold"),
      bg = 'lightblue').grid(row = 3,column = 1 , sticky = "W")


    label_for_user_email_var = StringVar()
    label_for_user_email = ttk.Entry(user_record_screen,
          font = ("calibri","13","bold"),
          textvariable = label_for_user_email_var,
          state = "readonly")
    label_for_user_email.grid(row = 3,column = 2 , sticky = "W",ipadx = '15')
    
    #-----------------------------------#

#------section for Gender-----------#
    
    Label(user_record_screen,
          text = "User's Gender :",
          font = ("calibri","16","bold"),
      bg = 'lightblue').grid(row = 4,column = 1 , sticky = "W")

    label_for_user_gender_var = StringVar()
    label_for_user_gender = ttk.Entry(user_record_screen,
          font = ("calibri","13","bold"),
          state = "readonly",
          textvariable = label_for_user_gender_var)
          
    label_for_user_gender.grid(row = 4,column = 2 , sticky = "W",ipadx = '15')
    
    #-----------------------------------#

#------section for user type-----------#
    
    Label(user_record_screen,
          text = "User's Type :",
          font = ("calibri","16","bold"),
      bg = 'lightblue').grid(row = 5,column = 1 , sticky = "W")

    label_for_user_type_var = StringVar()
    label_for_user_type = ttk.Entry(user_record_screen,
          font = ("calibri","13","bold"),
          textvariable = label_for_user_type_var,
          state = "readonly",)
    label_for_user_type.grid(row = 5,column = 2 , sticky = "W",ipadx = '15')
    
    #-----------------------------------#

#------section for user book issued-----------#
    
    Label(user_record_screen,
          text = "Books issue:",
          font = ("calibri","16","bold"),
      bg = 'lightblue').grid(row = 6,column = 1 , sticky = "W")


    label_for_user_issuedbooks_var = StringVar()
    label_for_user_issuedbooks = ttk.Entry(user_record_screen,
          font = ("calibri","13","bold"),
          textvariable = label_for_user_issuedbooks_var,
          state = "readonly",)
    label_for_user_issuedbooks.grid(row = 6,column = 2 , sticky = "W",ipadx = '15')
    
    #-----------------------------------#

    #-------Adding Data in User List----------#

    user_list = os.listdir(r"users/")

    for index,data in enumerate(user_list):
        lbx_for_userdetails_admin.insert(index,data)
    
#--------------------------------------------------#
                
    user_record_screen.mainloop()                                              
                                                                                            
#---------------------------------------------------------------------#


# Button 6    
#==============================for Remove User Button===============================#

def remove_user_screen_button_clicked():
    global remove_user_scrn
    remove_user_scrn = Toplevel(admin_panel_screen)
    remove_user_scrn.title("Signup")
    remove_user_scrn.geometry(center(remove_user_scrn,799,450))
    remove_user_scrn.resizable(0,0)
    remove_user_scrn.configure(background = "lightblue")

    #Adding Icon To The window
    remove_user_scrn.iconbitmap(r'pics/icon.ico')
    
    global search_user_for_remove_var
    global  user_type_for_remove_var
    global user_gender_for_remove_var
    global user_email_for_remove_var

    #setting header for scrn
    header_pic = PhotoImage(file = r"pics/remove users_header.png")
    Label(remove_user_scrn,image = header_pic).grid(row = 0,columnspan =3 )

    #Making Heading Label
    Label(
        remove_user_scrn,
        text = "Enter User Name :",
        font = ("Calibri","20","bold"),
        bg = "lightblue"
        ).grid(row = 1,column = 0,pady = '5')

    #Making Entry box for search user
    
    search_user_for_remove_var = StringVar()
    search_user_for_remove = ttk.Entry(remove_user_scrn,
                                       font = ("Calibri","20","bold"),
                                       textvariable = search_user_for_remove_var
                                        )
    search_user_for_remove.focus()
    search_user_for_remove.grid(row = 1,column = 1,sticky = 'w',pady = '5')

    #Making Button to search User Data
    search_btn_img = PhotoImage(file = r"pics/Search.png")
    Button(remove_user_scrn,
           image =search_btn_img,
           border = 0,
           bg = "lightblue",
           command = search_user_for_remove_clicked
           ).grid(row = 1,column = 2,sticky = 'w',ipady = "7",ipadx = "7",pady = '5')

    #Label Heading
    Label(
        remove_user_scrn,
        text = "User Details :",
        font = ("Calibri","25","bold"),
        bg = "lightblue"
        ).grid(row = 2,column = 0,sticky = 'w')

    #-----------User Email Section-------------#

    Label(
        remove_user_scrn,
        text = "User Email :",
        font = ("Calibri","20","bold"),
        bg = "lightblue"
        ).grid(row = 3,column = 0,sticky = 'w',pady = "5")

    user_email_for_remove_var = StringVar()
    user_email_for_remove = ttk.Entry(
        remove_user_scrn,
        font = ("Calibri","13","bold"),
        textvariable = user_email_for_remove_var,
        state = "readonly",
        )
    user_email_for_remove.grid(row = 3,column = 1,sticky = 'w',pady = "5",ipady = "5",ipadx = "45")

    #--------------------------------------------#

    #-----------User gender Section-------------#

    Label(
        remove_user_scrn,
        text = "User Gender :",
        font = ("Calibri","20","bold"),
        bg = "lightblue"
        ).grid(row = 4,column = 0,sticky = 'w',pady = "5")


    user_gender_for_remove_var = StringVar()
    user_gender_for_remove = ttk.Entry(
        remove_user_scrn,
        font = ("Calibri","13","bold"),
        textvariable = user_gender_for_remove_var,
        state = "readonly",
        )
    user_gender_for_remove.grid(row = 4,column = 1,sticky = 'w',pady = "5",ipady = "5",ipadx = "45")
    #--------------------------------------------#

    #-----------User Type Section-------------#

    Label(
        remove_user_scrn,
        text = "User Type :",
        font = ("Calibri","20","bold"),
        bg = "lightblue"
        ).grid(row = 5,column = 0,sticky = 'w',pady = "5")

    user_type_for_remove_var = StringVar()
    user_type_for_remove = ttk.Entry(
        remove_user_scrn,
        font = ("Calibri","13","bold"),
        textvariable = user_type_for_remove_var,
        state = "readonly"
        )
    user_type_for_remove.grid(row = 5,column = 1,sticky = 'w',pady = "5",ipady = "5",ipadx = "45")


    #--------------------------------------------#

    #Button For Delete User
    btn_pic_to_remove_user = PhotoImage(file = r"pics/remove_user_btn_pic.png")
    Button(remove_user_scrn,
           image = btn_pic_to_remove_user,
           border= 0,
           bg = "lightblue",
           command = delete_user).grid(row = 5,column= 2,pady = "5",sticky = 'w')
    
    remove_user_scrn.mainloop()

def search_user_for_remove_clicked():

    try:
        user_name = search_user_for_remove_var.get()
        password , email, gender , u_type = get_student_info(user_name)
        user_type_for_remove_var.set(u_type)
        user_gender_for_remove_var.set(gender)
        user_email_for_remove_var.set(email)
        
    except PermissionError:
        messagebox.showerror("Error","First Enter The User Name!!!")
    except FileNotFoundError:
        messagebox.showerror("Error","No User With this Username Exist")
    except:
        messagebox.showerror("Error","An Error Occured")

#---------------------------------------------------------------------#
    

# Button 7
#===============================for Registration Button=================================#

def open_registration_window():
    global reg_page_img
    global reg_btn_img
    global reg_user_entry_var , reg_user_entry   #globalizing username entry box and the container
    global reg_pass_entry_var, reg_pass_entry    #globalizing password entry box and the container
    global reg_email_entry, reg_email_entry_var #globalizing email entry box and the container
    global gender_var
    global usertype_var
    global reg_screen
    
    reg_screen = Toplevel(admin_panel_screen)
    reg_screen.title("Signup")
    reg_screen.geometry(center(reg_screen,400,630))
    reg_screen.resizable(0,0)
    reg_screen.configure(background = "lightblue")

    #Adding Icon To The window
    reg_screen.iconbitmap(r'pics/icon.ico')

    reg_page_img = PhotoImage(file=r"pics/add-user.png")

    Label(
    reg_screen,
    image = reg_page_img,
    border = 0,
    bg = "lightblue"
    ).pack(pady = 10)

    Label(
    reg_screen,
    text = "Add User",
    font = ("Helvetica", 20, "bold"),
    bg = "lightblue"
    ).pack()

    Label(
    reg_screen,
    text = "Enter User Name*",
    font = ("Helvetica", 10, "bold"),
    bg = "lightblue"
    ).pack(pady = 10)

    #-------username entrybox--------#
    
    reg_user_entry_var = StringVar()
    reg_user_entry = ttk.Entry(
        reg_screen,
        font = ("Helvetica", 15, "normal"),
        textvariable = reg_user_entry_var
        )
    reg_user_entry.pack(ipadx=15,ipady=2)

    reg_user_entry.focus()  #using so that the cursor is on the entry box

    #-----------------------------------#

    Label(
    reg_screen,
    text = "Enter Password*",
    font = ("Helvetica", 10, "bold"),
    bg = "lightblue"
    ).pack(pady = 10)

    #-------password entrybox--------#

    reg_pass_entry_var = StringVar()
    reg_pass_entry = ttk.Entry(
        reg_screen,
        font = ("Helvetica", 15, "normal"),
        textvariable = reg_pass_entry_var
        )
    reg_pass_entry.pack(ipadx=15,ipady=2)

    #-----------------------------------#
    
    Label(
    reg_screen,
    text = "Enter Email Address*",
    font = ("Helvetica", 10, "bold"),
    bg = "lightblue"
    ).pack(pady = 10)

    #-------email entrybox--------#


    reg_email_entry_var = StringVar()
    reg_email_entry = ttk.Entry(
        reg_screen,
        font = ("Helvetica", 15, "normal"),
        textvariable = reg_email_entry_var
        )
    reg_email_entry.pack(ipadx=15,ipady=2)

    #-----------------------------------#

    Label (
        reg_screen,
        font = ("Helvetica", 10, "bold"),
        text = "Select Your Gender",
        bg = "lightblue"
        ).pack(pady = 10)

    
    #-------Gender Combo Box--------#
    gender_var = StringVar()
    gender_box = ttk.Combobox(reg_screen,
                              width = 13,
                              textvariable = gender_var ,
                              font = ("Helvetica", 15, "normal"),
                              state = "readonly")
    gender_box["value"] = ("Male","Female","Others")
    gender_box.current(0)
    gender_box.pack(ipadx=15,ipady= 2)
    #------------------------------------#

    #-----User type combo Box-------#
    Label (
        reg_screen,
        font = ("Helvetica", 10, "bold"),
        text = "Select User Type",
        bg = "lightblue"
        ).pack(pady = 10)


    usertype_var = StringVar()
    usertype_1 = ttk.Combobox(reg_screen,
                              width = 13,
                              textvariable = usertype_var ,
                              font = ("Helvetica", 15, "normal"),
                              state = "readonly")
    
    usertype_1["value"] = ("Student","Teacher")
    usertype_1.current(0)
    usertype_1.pack(ipadx=15,ipady= 2)
    
    #------------------------------------#

    
    reg_btn_img = PhotoImage(file=r"pics/reg_btn_img.png")

    #------reg submit Button--------#
    user_check_btn = Button(
        reg_screen,
        image = reg_btn_img,
        border = 0,
        bg = "lightblue",
        command = registration
        )
    user_check_btn.pack(pady = 15)
    
    reg_screen.mainloop()
    #---------------------------------#

# Button 8
#===============================for Return Book Screen=================================#

def return_book_scrn_btn_clicked():
    global return_book_win
    global get_user_issue_book_data_for_return_var
    global list_box_for_recive_books
    global label_for_issue_date_return_var
    global label_for_due_date_return_var

    return_book_win = Toplevel()
    return_book_win.config(bg = "lightblue")
    return_book_win.resizable(0,0)
    return_book_win.geometry(center(return_book_win,799,600))

    #Adding Icon To The window
    return_book_win.iconbitmap(r'pics/icon.ico')

    #Seting Header For screen###############
    header_pic_for_return_book_screen = PhotoImage(file = r"pics/bookreturn_header.png")
    Label(return_book_win,image = header_pic_for_return_book_screen).grid(row=0,columnspan = 4)
    ##############################

    #--------------Search User section-----------#

    #Label For Search Entry Box
        
    Label(return_book_win ,
          text = "Enter UserName :",
          font = ("Calibri","18","bold"),
          bg = "lightblue").grid(row = 1 ,column = 0)

    #Making Entry Box For Search user issue books

    get_user_issue_book_data_for_return_var = StringVar()
    get_user_issue_book_data_for_return = ttk.Entry(return_book_win,
              font = ("Calibri","18","bold"),
              textvariable = get_user_issue_book_data_for_return_var
              )
    get_user_issue_book_data_for_return.focus()
    get_user_issue_book_data_for_return.grid(row = 1 ,column = 1,sticky ='W')

    #Making Button For Search user issue books
    
    search_btn_img = PhotoImage(file = r"pics/Search.png")
    Button(return_book_win,
               image = search_btn_img,
           border=0,
           bg = "lightblue",
           command = add_data_to_book_recive_list
            ).grid(row = 1 ,column = 2,sticky ='W',pady = '4')
    
    #----------------------------------------------------------#

    #--------------Making Frame For Books List-------------#
    
    frame_for_recive_book_list = Frame(return_book_win,bg = 'lightblue')
    frame_for_recive_book_list.grid(rowspan = 10 ,column= 0)

    #Frame Items
    #Label for list heading
    
    Label(frame_for_recive_book_list ,
          text = "Issued Books By User :",
          font = ("Calibri","18","bold"),
          bg = "lightblue").grid(row = 0 ,column = 0)

    #List for Books Display
    list_box_for_recive_books = Listbox(
        frame_for_recive_book_list,
        font = ("Calibri","16","bold")
        )
    list_box_for_recive_books.grid(row = 1 ,column = 0)

    #Adding Scrolbar to the list
    sbr = Scrollbar(
        frame_for_recive_book_list,
        )
    sbr.grid(row = 1 ,column = 0,sticky = "e",ipady ="110" )

    #Adding Command In scrollbar so that it perform scrolling
    sbr.config(command = list_box_for_recive_books.yview )
    list_box_for_recive_books.config(yscrollcommand = sbr.set)

    #Making Button To see Books Details
    btn_image_for_book_detail_submit = PhotoImage(file = r"pics/proceed_btn.png")
    Button(frame_for_recive_book_list,
           image =btn_image_for_book_detail_submit,
           bg = 'lightblue',
           border = 0 ,
           command = read_the_book_for_return
           ).grid(row = 2,column = 0,pady = "5")

    #Making 2 label for due date and issue date
    

    #Label For Display Heading
    Label(return_book_win,
          text = "See Book Details :",
          font = ("Calibri","20","bold"),
          bg = "lightblue").grid(row = 3 ,column = 1)

    #Label for issue Date
    Label(return_book_win,
          text = '''Issue Date
(yyyy,mm,dd):''',
          font = ("Calibri","15","bold"),
          bg = "lightblue").grid(row = 4 ,column = 1)

    label_for_issue_date_return_var = StringVar()
    label_for_issue_date_return = ttk.Entry(return_book_win,
          text = "Issue Date",
          font = ("Calibri","18","bold"),
          state = "readonly",
          textvariable = label_for_issue_date_return_var)
    label_for_issue_date_return.grid(row = 4 ,column = 2,sticky = 'W')
    #--------------------------------#

    #Label For due date
    Label(return_book_win,
          text = '''Due Date
(yyyy,mm,dd):''',
          font = ("Calibri","15","bold"),
          bg = "lightblue").grid(row = 5 ,column = 1)

    label_for_due_date_return_var = StringVar()
    label_for_due_date_return = ttk.Entry(return_book_win,
          text = "Due Date",
          font = ("Calibri","18","bold"),
          state = "readonly",
          textvariable = label_for_due_date_return_var)
    label_for_due_date_return.grid(row = 5 ,column = 2,sticky = 'W')
    #--------------------------------#

    #Making Button For Book Reciving

    img_for_book_reciving_button = PhotoImage(file = r"pics/recive_book_btn.png")
    Button(return_book_win,
            image = img_for_book_reciving_button,
            bg = "lightblue",
            border = 0,
           command = recive_book_btn_clicked
            ).grid(row = 8 ,column = 1)

    #Making Button to see Collectedfine
    img_for_see_fine_details = PhotoImage(file = r"pics/Collected_fine.png")
    Button(return_book_win,
            image = img_for_see_fine_details,
            bg = "lightblue",
            border = 0,
           command = see_collectd_fine
            ).grid(row = 8 ,column = 2)

    
    return_book_win.mainloop()

#Supporting Function For window To open 
def add_data_to_book_recive_list():
    try:
        username = get_user_issue_book_data_for_return_var.get()
        if len(username) < 1:
            messagebox.showerror("Error","Search username first")

        else:
            books_list_taken_by_user = os.listdir(r"issued-books/"+username)

            if len(books_list_taken_by_user) < 1:
                messagebox.showerror("Error","User didn't issue any book yet")
            else:
                for index,data in enumerate(books_list_taken_by_user):
                    with open(r'books/'+data,'r')as f:
                        data = f.readline().strip()
                        list_box_for_recive_books.insert(index,data)
                
    except FileNotFoundError:
        messagebox.showerror("Error","User doesnot exist")


        
def read_the_book_for_return():
    #global due_date_for_returning_book
    try:
        username = get_user_issue_book_data_for_return_var.get()
        issued_book_name = list_box_for_recive_books.get('active')

        #getting issued book id
        with open(r'books_name/'+issued_book_name ,'r')as f:
            issued_book_id = f.readline().strip("\n")
        
        with open(r"issued-books/"+username+"/"+issued_book_id, 'r') as f:
            issuedate = f.readline()
            duedate = f.readline()

            issuedate = issuedate.strip()
            duedate = duedate.strip()

            label_for_issue_date_return_var.set(issuedate)
            label_for_due_date_return_var.set(duedate)
    except PermissionError:
        messagebox.showerror("Error","Search Username First")



#Command for Button to see collected fine 
def see_collectd_fine():
    with open(r"fine_collection/total-fine-recieved","r") as f:
        fine = f.readline()
        fine = fine.strip()
        messagebox.showinfo("info","Total collected fine is '"+fine+"' R.s")
    

#-------------------------------------------------------------------- #



###########################################
###########################################


#######################################################
#######################################################
#                                                                                                                                 #
#              Commands for buttons of toplevel screen of admin pandel screen                        #
#                                                                                                                                 #
#######################################################
#######################################################


#=====================command for button of search book screen================================#
def search_book_for_admin_clicked():
    book_id = search_books_for_admin_entrybox_var.get().strip("\n")
    book_list = os.listdir(r'Books')

    if len(book_id) < 1:
        messagebox.showerror("Error","Please enter the book id first")
        
    elif book_id in book_list:
        book_name, book_auther_name, book_quantity = get_book_info(book_id)


        search_book_id_label_var.set(book_id)
        search_book_name_label_var.set(book_name)
        search_book_author_name_label_var.set(book_auther_name)
        search_book_quantity_label_var.set(book_quantity)
    else:
        messagebox.showerror("No Book Exits","No Book With ID "+book_id+" Exist")

#-----------------------------------------------------------------------------#

def search_book_for_admin_by_name_clicked():

    book_name = search_books_for_admin_by_name_entrybox_var.get().strip("\n")
    get_books_name_list = os.listdir('books_name')
    book_name_list =[]

    if len(book_name) == 0:
        messagebox.showerror("Error","First enter the book name")
        
    else:   
        for x in get_books_name_list:
            book_name_list.append(x.lower())
                
        if book_name.lower() in book_name_list:
            with open(r"books_name/"+book_name,"r") as f:
                book_id = f.readline().strip("\n")
            
            book_name, book_auther_name, book_quantity = get_book_info(book_id)

            search_book_id_label_var.set(book_id)
            search_book_name_label_var.set(book_name)
            search_book_author_name_label_var.set(book_auther_name)
            search_book_quantity_label_var.set(book_quantity)
        else :
            messagebox.showerror("No Book Exits","No Book With Name Exist")

        
    
#=======================command for button of Add book screen==============================#

def add_book():
    book_id = entry_box_for_addbook_id_var.get().strip("\n")
    book_name = entry_box_for_addbook_name_var.get().strip("\n")
    author_name = entry_box_for_addbook_author_name_var.get().strip("\n")
    book_quantity = entry_box_for_addbook_quantity_var.get().strip("\n")

    book_list = os.listdir(r'Books')
    book_name_list = os.listdir(r'books_name')

    for x in book_name_list:
        if x.lower() == book_name.lower():
            messagebox.showerror("Books Already Exist","Book with this title is already exist if you want to add the same book \
you can edit the book quantity")
            break
        
    else:
        if book_id in book_list:
            messagebox.showerror("Id Already Exist","A book With This ID already Exist")
        elif len(book_id) < 1:
            messagebox.showerror("Book Id Missing","Please Enter Book Id")
        elif len(book_name) < 1:
            messagebox.showerror("Book name Missing","Please Enter Book Name")
        elif len(author_name) < 1:
            messagebox.showerror("Author name Missing","Please Enter Author Name")
        elif len(book_quantity) < 1:
            messagebox.showerror("Book Quantity Missing","Please Enter Book Quantity")

        else:
            with open(r'Books/'+book_id,'w') as f:
                f.write(book_name+'\n')
                f.write(author_name+'\n')
                f.write(book_quantity+'\n')
                
            with open(r'books_name/'+book_name,'w') as f:
                f.write(book_id)
                
                entry_box_for_addbook_id.delete(0,END)
                book_name = entry_box_for_addbook_name.delete(0,END)
                author_name = entry_box_for_addbook_author_name.delete(0,END)
                book_quantity = entry_box_for_addbook_quantity.delete(0,END)

                messagebox.showinfo("Congrats!!","The Book Has Added Successfully")
            
#-----------------------------------------------------------------------------#

#=========================command for button of Edit book screen===============================#
def book_edit_btn_clicked():
    try:
        book_id = book_id_for_edit

        if len(book_id) < 1:  #If the entry box is empty donot proceed
             messagebox.showerror("Error","First search the book in the entry box")
        else:
            global edit_book_scrn
            edit_book_scrn = Toplevel(editbooks_win)
            edit_book_scrn.geometry(center(edit_book_scrn,400,600))
            edit_book_scrn.configure(background = "lightblue")
            edit_book_scrn.title("Edit Record")
            edit_book_scrn.resizable(0,0)

            #Adding Icon To The window
            edit_book_scrn.iconbitmap(r'pics/icon.ico')

            #Label For Screen Logo
            head_pic_for_edit_bookrecord = PhotoImage(file = r"pics/Edit_books.png")
            Label(edit_book_scrn,
                  image=head_pic_for_edit_bookrecord,
                  background = "lightblue").pack(pady = ("20","0"))

            #globalizing all entry variables 
            global edit_bookname_var , edit_bookname
            global edit_book_authorname_var, edit_book_authorname
            global edit_bookquantity_var, edit_bookquantity
            
            Label(edit_book_scrn,
                    text = "Edit Record",
                    font= ('comic sans ms',25),
                    bg = "lightblue",
                    ).pack()
            
            #------Book Name Section-----#
            
            Label(edit_book_scrn,
                    text = "Edit Book Name",
                    font= ('comic sans ms',15),
                    bg = "lightblue",
                    ).pack(pady = ("20","0"))
            
            edit_bookname_var = StringVar()
            edit_bookname= ttk.Entry(edit_book_scrn,
                    font= ('comic sans ms',15),
                    textvariable = edit_bookname_var
                    )
            edit_bookname.pack()
            #--------------------------------#

            #------Author Name Section-----#
            Label(edit_book_scrn,
                    text = "Edit Author Name",
                    font= ('comic sans ms',15),
                    bg = "lightblue",
                    ).pack(pady = ("20","0"))

            edit_book_authorname_var = StringVar()
            edit_book_authorname = ttk.Entry(edit_book_scrn,
                    font= ('comic sans ms',15),
                    textvariable = edit_book_authorname_var
                    )
            edit_book_authorname.pack()
            #--------------------------------#

            #------book Quantity Section-----#
            Label(edit_book_scrn,
                    text = "Edit Book Quantity",
                    font= ('comic sans ms',15),
                    bg = "lightblue",
                    ).pack(pady = ("20","0"))

            edit_bookquantity_var = StringVar()
            edit_bookquantity = ttk.Entry(edit_book_scrn,
                    font= ('comic sans ms',15),
                    textvariable = edit_bookquantity_var
                    )
            edit_bookquantity.pack()
            #--------------------------------#
            book_name, book_auther_name,book_quantity =  get_book_info(book_id_for_edit)

            edit_bookname_var.set(book_name) 
            edit_book_authorname_var.set(book_auther_name)
            edit_bookquantity_var.set(book_quantity)

            #Button
            blue_btn_edit_pic = PhotoImage(file = r"pics/edit_button_blue.png")

            Button(edit_book_scrn,
                   image = blue_btn_edit_pic,
                   bg = "lightblue",
                   command = edit_the_record_of_books,
                   border = 0).pack(pady = ("30","0"))
            
            
            edit_book_scrn.mainloop()
    except NameError:
        messagebox.showerror("search book","First search the book you want to edit")
    

def edit_the_record_of_books():
    book_id = book_id_for_edit

    book_name = edit_bookname_var.get()
    author_name = edit_book_authorname_var.get()
    book_quantity = edit_bookquantity_var.get()

    book_id = book_id_for_edit
    book_list = os.listdir(r'Books')

    if len(book_name) < 1:
        messagebox.showerror("Book Name Missing","Kindly Enter Book Name")
    elif len(author_name) < 1:
        messagebox.showerror("Author Name Missing","Kindly Enter Author Name")
    elif len(book_quantity) < 1:
        messagebox.showerror("Book Quantity Missing","Kindly Enter Book Quantity")
    else:
        #renamming the book

        #first getting the book name
        with open(r'books/'+book_id)as f:
                old_book_name = f.readline().strip("\n")
                os.chdir(r"books_name")
                os.rename(old_book_name,book_name)
                os.chdir("..")
                
        with open(r'Books/'+book_id,'w') as f:
                f.write(book_name+'\n')
                f.write(author_name+'\n')
                f.write(book_quantity+'\n')

                
                search_book_for_edit_name_label_var.set(book_name)
                search_book_for_edit_author_name_label_var.set(author_name)
                search_book_for_edit_quantity_label_var.set(book_quantity)

                messagebox.showinfo("Book record Editted","Book record Editted successfully")
                #Setting the Book id search box to empty
                search_books_for_edit_entrybox_var.set("")


                
#---------------------------------------------------------------------------------------------------- #

#====================command for button of issue book screen==================================#

def issue_btn_clicked():
    try:
        book_id = book_detail_for_issue_var.get()
        username = User_detail_for_issue_var.get()


        check_quantity = check_book_quantity(book_id)

        book_list = os.listdir(r'issued-books/'+username)

        max_book_issue_limit = 2
        
        if book_id in book_list:
            messagebox.showerror("Error","The user has already taken the same Book")

        elif check_quantity < 1:
            messagebox.showerror("Error","The Book Is Unavailable in the library")
            
        elif len(username) < 1:
            messagebox.showerror("Error","Enter The User Name")

        elif len(book_list) == max_book_issue_limit:
            messagebox.showerror("Error","Already issued 2 books Can't issue more")

        else:
            issue_the_book_to_user(username,book_id)
            messagebox.showinfo("info","Book Has Been Issued Successfully")
            
    except PermissionError:
        messagebox.showerror("Error","First enter the username and book id")
    except FileNotFoundError:
        messagebox.showerror("Error","Don't Enter Anything in search box after searching")


#Making Function so that The book quantity can be reduce after publishing
def reduce_book_quantity(book_id):   #healping function for issue book
    with open(r'Books/'+book_id, 'r') as f:
        bookname = f.readline()
        authername = f.readline()
        bookquantity = f.readline()
        bookquantity = int(bookquantity) - 1
       
    with open(r'Books/'+book_id, 'w') as f:    #healping function for issue book
        f.write(bookname)
        f.write(authername)
        f.write(str(bookquantity))


# Making function for check book quantity
# So that if quantity is 0 so the book will not be Published
def check_book_quantity(book_id):
    with open(r'Books/'+book_id, 'r') as f:
        bookname = f.readline()
        authername = f.readline()
        bookquantity = f.readline()
        bookquantity = int(bookquantity)

        return bookquantity        


#function to issue the book to the user
def issue_the_book_to_user(username,book_id):
    with open(r'issued-books/'+username+'/'+book_id,"w") as f:
                date = datetime.date.today()
                duedate = datetime.timedelta(days = 17)#17 days are the minimum critera to take book
                duedate = (date+duedate)
                f.write(str(date)+'\n')
                f.write(str(duedate)+"\n")
                reduce_book_quantity(book_id)

                Issue_date_for_issue_var.set(str(date))
                due_date_for_issue_var.set(str(duedate))
                
                book_detail_for_issue_var.set("")
                User_detail_for_issue_var.set("")


#command for reissue btn
def reissue_btn_clicked():
    try:
        book_id = book_detail_for_issue_var.get()
        username = User_detail_for_issue_var.get()
        book_list = os.listdir(r'issued-books/'+username)

        if book_id in book_list:
            fine = check_fine_on_user_reissue()
            if fine == True:
                messagebox.showerror("Error","This user has fine on this book can't reissue the book first submit fine")
            else:
                issue_the_book_to_user(username,book_id)
                messagebox.showinfo("info","Book reissued successfully")
        else:
            messagebox.showerror("Error","User didn't issue the book first issue the book")
        
    except PermissionError:
        messagebox.showerror("Error","First enter the username and book id")


#Making funtion to see fine on user
def check_fine_on_user_reissue():
        book_id = book_detail_for_issue_var.get()
        username = User_detail_for_issue_var.get()

        #First Reading The issued book file to get due date
        with open(r"issued-books/"+username+"/"+book_id, 'r') as f:
            issuedate = f.readline()
            duedate = f.readline()

            issuedate = issuedate.strip()
            duedate = duedate.strip()

        #Converting Date str in to int
        year,month,day = conver_srt_to_date(duedate)

        #Checking days on issue book if greater then 18 days will be return would be true
        #else false
        #If return is true book will not be reissued
        borrow_day_for_reissue = check_fine_for_reciving_book(year,month,day)
        if borrow_day_for_reissue < 1:
            return False
        return True
        
#---------------------------------------------------------------------------------------------------- #
    
#=========================command for button of see user data screen============================#

def see_details_admin_clicked():
    user_name = lbx_for_userdetails_admin.get(ACTIVE)
    password,email,gender,usertype = get_student_info(user_name)
    issued_books = get_book_issue(user_name)

    label_for_user_password_var.set(password)
    label_for_user_email_var.set(email)
    label_for_user_gender_var.set(gender)
    label_for_user_type_var.set(usertype)
    label_for_user_issuedbooks_var.set(issued_books )


#function to get issued books by user
def get_book_issue(user_name):  #supporting function for see_details_admin_clicked
    
    issued_book_list_of_user = os.listdir(r'issued-books/'+user_name)
    return(len(issued_book_list_of_user))
#---------------------------------------------------------------------------------------------------- #


#=======================command for button of Remove user  screen=============================#

def delete_user():
    user_name = search_user_for_remove_var.get()
    if len(user_name) < 1:
        messagebox.showerror("Error","First Search the Username")
    else:
        #If the user didn't search the book so there will be an error
            #Thats why we user try and except
        try:
            os.chdir(r"issued-books")
            listt = os.listdir(user_name)

            if len (listt) > 0:
                os.chdir(r"..")
                messagebox.showerror("Error","This User Has Issued Books For him Self Can't Remove This User")    
            else:
                os.rmdir(user_name)
                os.chdir(r"..")
                os.chdir(r"users")
                os.remove(user_name)
                os.chdir("..")

                #clearing the entry boxes of display data
                user_type_for_remove_var.set("")
                user_gender_for_remove_var.set("")
                user_email_for_remove_var.set("")
                
                messagebox.showinfo("removed","User Has Been Removed Successfully")
                search_user_for_remove_var.set("")
        except FileNotFoundError:
            messagebox.showerror("Error","First Search the Username")
        


#--------------------------------------------------------------------------#

#=======================Command for buttons of Registration screen==============================#

def registration():
    #getting all values from registration screen
    username_reg = reg_user_entry_var.get()
    password_reg = reg_pass_entry_var.get()
    email_reg = reg_email_entry_var.get()
    gender_reg = gender_var.get()
    usertype_reg = usertype_var.get()

    # spliting email for checking validitory
    email_check = email_reg.split('@')
    #--------------------------------#

    users_list = os.listdir(r'users') #list of users

    #all conditions for errors

    if username_reg in users_list:
        messagebox.showerror("User Already Exist","Username Already Exist")
        reg_screen_reset()
        
    elif len(username_reg) < 4 or len(username_reg) > 25:
        messagebox.showerror("Invalid Username","Username must be in between 4 to 25 characters")
        #If username is incorrect data will be erased
        reg_user_entry_var.set("")
        
    elif len(password_reg) < 8:
        messagebox.showerror("Invalid Password","Password must be atleast 8 characters")
        reg_pass_entry_var.set("")
        
    elif email_check[-1] != 'gmail.com' and email_check[-1] != 'yahoo.com':
        messagebox.showerror("Invalid Email","We only support gmail and yahoo emails")
        reg_email_entry_var.set("")

    elif len(email_check[0]) < 4 :
        messagebox.showerror("Invalid Email","Invalid Email")
        reg_email_entry_var.set("")
    
    else:
        with open("users//"+username_reg, "w") as f:
            
            f.write(password_reg+"\n")
            f.write(email_reg+"\n")
            f.write(gender_reg+"\n")
            f.write(usertype_reg+"\n")

        #making directory for issued books with the name of user
        makedir(username_reg)

        destroy_registration_screen()
        messagebox.showinfo("Congrats!!","Congrats!!! you are Registered")

        

        
# function for make directory with the name of user in issued book directory
def makedir(username_reg):
    os.chdir(r"issued-books")
    os.mkdir(username_reg)
    os.chdir(r'..')

#------------------------------------------------------------------------------------- #


#==========================Command for buttons of Return Book Screen======================================#

def recive_book_btn_clicked():
    global borrow_days
    
    username = get_user_issue_book_data_for_return_var.get()
    issued_book_name = list_box_for_recive_books.get('active')

        #getting issued book id
    with open(r'books_name/'+issued_book_name ,'r')as f:
            issued_book_id = f.readline().strip("\n")

    if len(username) < 1 or len(issued_book_id) < 1:
        messagebox.showerror("Error","First Search The user name and select the book")

    else:
        due_date = label_for_due_date_return_var.get()
        
        if len(due_date)< 1:
            messagebox.showerror("Error","First See the book Details")

        else:
                
            #Converting due_date str in int so that we can collect fine
            year,month,day = conver_srt_to_date(due_date)

            #Cheking if there is any fine
            borrow_days = check_fine_for_reciving_book(year,month,day)

            #If borrow days are less then 18 then
            #don't collect fine
            #else
            #Open a window And Collect Fine

            if borrow_days < 1:

                #Function For adding book in the library
                add_the_book_in_the_library(issued_book_id)

                #Function for removing book from the user account
                deleting_book_from_user_account(username,issued_book_id)

                #for displaying message
                messagebox.showinfo("info","Book Has been recived Successfully")

                #Destroying The Screen After Fine Collection
                destroy_returnbook_screen()
            
            else:
                open_fine_collection_win()

#function to Converting str in to int so that wo can collect fine
def conver_srt_to_date(date):
    try:
        date = date.split("-")

        #Converting All of them in int so we can further proceed
        #because they were str before
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        
        return year,month,day
    except ValueError:
        messagebox.showerror("Error","First See the book Details")

#Function For checking Fine on the book
def check_fine_for_reciving_book(year,month,day):

    #Subtracting issue_date from today date
    
    due_date = datetime.date(year,month,day)
    today_date = datetime.date.today()

    
    calculate_days = today_date - due_date#Answer 

    
    #Performing This Step because we get date not int so we are converting this in to
    #Simple int
    try:
        day = str(calculate_days)
        day = day.split(" ")
        day = int(day[0])#converting it into int because it is type str
        return day
    except ValueError:
        day = 0 #Performing this step because if the user return book on the duedate
        return day  #If this step is not performed we will get a value error
                        


#Function For adding book back in to the library
def add_the_book_in_the_library(book_id):
            
    with open(r"Books/"+book_id , 'r') as f:
        book_name = f.readline()
        author_name = f.readline()
        book_quantity = f.readline()

        #Adding Book in the library
        book_quantity = int(book_quantity) + 1

    with open(r"Books/"+book_id , 'w') as f:   
        f.write(book_name)
        f.write(author_name)
        f.write(str(book_quantity)+"\n")


#Function for Deleting Book From the user data
def deleting_book_from_user_account(user_id,book_id):
    os.chdir("issued-books/"+user_id)
    os.remove(book_id)
    os.chdir('..')
    os.chdir('..')



#Fuction For fine collection if user is fined it will be called
def open_fine_collection_win():
    global fine_collection_win
    fine_collection_win = Toplevel(return_book_win)
    fine_collection_win.config(bg = "lightblue")
    fine_collection_win.title("Collect Fine")
    fine_collection_win.geometry(center(fine_collection_win,400,400))
    fine_collection_win.resizable(0,0)

    #Adding Icon To The window
    fine_collection_win.iconbitmap(r'pics/icon.ico')


    # Header For the screen ######## 
    header_pic_for_fine_collection = PhotoImage(file = r"pics/recive_fine.png")
    Label(fine_collection_win,image = header_pic_for_fine_collection,bg = 'lightblue').pack(pady = ("5","0"))
    ######################

    #Label for heading Display
    Label(fine_collection_win,
          font = ("comic sans ms",20,"bold"),
          text = "Collect Fine",
          bg = "lightblue").pack()

    #Globalizing the fine variable so that it can be used by other fuctions
    
    global add_fine_in_record

    #Fine will be stroed in this variable
    add_fine_in_record = Calculate_fine(borrow_days)

    #Label to Display how many days user is late
    Label(fine_collection_win,
          text = 'The user is "'+str(borrow_days)+'" days late!!',

          font = ("comic sans ms",16,"bold"),
          bg = "lightblue").pack(pady = ("15","0"))

    #The Total fine ammount is +str(fine),

    #Label for displaying fine amount
    Label(fine_collection_win,
          text = 'fine ammount is "'+str(add_fine_in_record)+'" R.s',

          font = ("comic sans ms",16,"bold"),
          bg = "lightblue").pack(pady = ("0","15"))


    #Button To collect fine
    collect_fine_btn_img = PhotoImage(file = r"pics/Collect_fine_btn.png")
    Button(fine_collection_win,
           image = collect_fine_btn_img,
           border = 0,
           command = collect_fine_btn_cmd,
           bg = "lightblue").pack(pady = ("15","0"))

    
    fine_collection_win.mainloop()

#After clicking the fine collect button
#This fucton wil add book in library and remove the book from user account
#And add the fine in the fine collection file
def collect_fine_btn_cmd():
    #this is to get username    
    username = get_user_issue_book_data_for_return_var.get()
    #This is to get issued_book id
    issued_book_id = list_box_for_recive_books.get('active')

    
    action_for_fine_btn(issued_book_id,username)
    fine_collection(add_fine_in_record)
    messagebox.showinfo("info","fine has been collected and book has been return successfully")

    #Destroying The screen after fine collection
    destroy_returnbook_screen()   

#This function Add the issued book in the libray
#And delete the book from user account
def action_for_fine_btn(book_id,user_id):
    add_the_book_in_the_library(book_id)
    deleting_book_from_user_account(user_id,book_id)
    


#This function calculate the fine on user
def Calculate_fine(days):
    Fine = 2
    return days * Fine


#This Function collect the fine and save it in the fine collecton
def fine_collection(fine):
    with open(r"fine_collection/total-fine-recieved",'r') as f:
        amount = f.readline()
        fine += int(amount)
    with open(r"fine_collection/total-fine-recieved",'w') as f:
        f.write(str(fine))
    
#==========================Command for buttons of Logout======================================#


def logout_admin_win():
    messagebox.showinfo("logout","Logout Successful")
    destroy_adminscreen()
    main_screen()
    


#######################################################
#######################################################
#                                            End of admin Panel Screen

#######################################################
#######################################################

###################################################################
###################################################################
#                                                                                                                                                              #
#                                                      Making User Login Window                                                                 #
#                                                                                                                                                              #
###################################################################
###################################################################

#Details
#In this screen there are 4 Buttons

# 1)Search books:

# In This window you can search Books Also You can see the list of books
# it takes data from file "books" and display it


# 2)Check issued Books Details
# In this window issued books details would be displayed
#if the didn't issue any book the screen would not be oppened
#if the user has issued the book a screen would be open
# All issued books would be display in the list box
#User can see info about the issued book
#like Book Name,Author name,BookId ,IssueDate,DueDate etc.


# 3)Edit Details
#By clicking this btn A user can edit his/her info
#to edit info admin password would be required without admin Password no info would be change
#you can edit password,email,gender,type in this window
#password must be atleast 8 characters long
#email must be not otherthan gmail.com or yahoo.com


# 4)Logout:
#By clicking this button user panel screen would be destroyed and mainscreen would be opend




#This function store the username of user during the login
#So that user won't need to enter his email again and agian
def get_username_after_userlogin(username):
    global username_to_use_after_login
    username_to_use_after_login = username
    
    
def User_login_screen():
    global user_login_win
    user_login_win= Tk()
    user_login_win.geometry(center(user_login_win,799,370))
    user_login_win.resizable(0,0)
    user_login_win.config(bg = "lightblue")
    user_login_win.title("User Panel")

    #Adding Icon To The window
    user_login_win.iconbitmap(r'pics/icon.ico')
    

    #Seting Header For the Screen#####################
    header_pic_for_user_panel_win = PhotoImage(file = r"pics/user_header.png")
    Label(user_login_win,
          image = header_pic_for_user_panel_win).grid(row = 0, columnspan = 4)
    #######################################


    #Button 1
    #-----------Section For search Books------------#

    pic_for_btn_of_search_books_user = PhotoImage(file = r"pics/search_books.png")
    Button(user_login_win,
           image =  pic_for_btn_of_search_books_user,
           border = 0,
           bg = "lightblue",
           command = open_search_book_for_user
           ).grid(row = 1,column = 0,pady = ("20","0"))

    Label(user_login_win,
          text = "Search Books",
          font = ("comic sans ms","18","bold"),
          bg = "lightblue").grid(row = 2,column = 0)

    #--------------------------------------------------#

    #Button 2
    #-----------Section For See issued books------------#

    pic_for_btn_of_isuue_books_detail_user = PhotoImage(file = r"pics/issue_books_details_for_user.png")
    Button(user_login_win,
           image =  pic_for_btn_of_isuue_books_detail_user,
           border = 0,
           bg = "lightblue",
           command = check_issued_books_btn_clicked
           ).grid(row = 1,column = 1,pady = ("20","0"))

    Label(user_login_win,
          text = "issued Books",
          font = ("comic sans ms","18","bold"),
          bg = "lightblue").grid(row = 2,column = 1)

    #--------------------------------------------------#


    #Button 3
    #-----------Section For Edit User Details------------#

    pic_for_btn_of_user_edit_details = PhotoImage(file = r"pics/edit_User_Details.png")
    Button(user_login_win,
           image =  pic_for_btn_of_user_edit_details,
           border = 0,
           bg = "lightblue",
           command = User_editinfo_btn_clicked,
           ).grid(row = 1,column = 2,pady = ("20","0"))

    Label(user_login_win,
          text = "Edit Details",
          font = ("comic sans ms","18","bold"),
          bg = "lightblue",
          ).grid(row = 2,column = 2)

    #--------------------------------------------------#

    #Button 4
    #-----------Section For logout------------#

    pic_for_btn_of_user_logout = PhotoImage(file = r"pics/logout_btn.png")
    Button(user_login_win,
           image =  pic_for_btn_of_user_logout,
           border = 0,
           bg = "lightblue",
           command = User_logout_btn_clicked).grid(row = 1,column = 3,pady = ("20","0"))

    Label(user_login_win,
          text = "Logout",
          font = ("comic sans ms","18","bold"),
          bg = "lightblue").grid(row = 2,column = 3)

    #--------------------------------------------------#
    
    
    user_login_win.mainloop()



###################################################
###################################################
###################################################

#                           Command  For Button of userpanel Screen

###################################################
###################################################



#Button 1

#==============================Section for Search book Screen=========================================#

def open_search_book_for_user():
    global search_book_for_user_win
    
    search_book_for_user_win = Toplevel(user_login_win)
    search_book_for_user_win.config(bg = "lightblue")
    search_book_for_user_win.geometry(center(search_book_for_user_win,799,520))
    search_book_for_user_win.resizable(0,0)
    search_book_for_user_win.title("Search Books")

    global Seach_Book_for_user_entry_box_var
    global get_book_id_for_user_var
    global get_book_name_for_user_var
    global get_book_author_name_for_user_var
    global get_book_quantity_for_user_var
    global Seach_Book_for_user_by_name_entry_box_var
    
    #Adding Icon To The window
    search_book_for_user_win.iconbitmap(r'pics/icon.ico')

    #Header For Search Book Screen
    pic_for_header_of_user_search_book_win = PhotoImage(file = r"pics/search_books header.png")
    Label(search_book_for_user_win ,
          image = pic_for_header_of_user_search_book_win).grid(row = 0,columnspan = 3)
    ##############################


    #----------Search Book Entry Box Area ------------#

    Label(search_book_for_user_win,
          text = "Search Book With ID:",
          font = ("Arial","16","bold"),
          bg = "lightblue").grid(row = 1,column = 0,pady = "5")


    Seach_Book_for_user_entry_box_var = StringVar()
    Seach_Book_for_user_entry_box = ttk.Entry(search_book_for_user_win,
          textvariable = Seach_Book_for_user_entry_box_var,
          font = ("Arial","16","bold"))
    Seach_Book_for_user_entry_box.grid(row = 1,column = 1,sticky = 'w',ipady = "5",ipadx = "5",pady = "5")

    #Button For Search Books
    pic_for_btn_of_search_book_of_user = PhotoImage(file = r"pics/Search.png")
    Button(search_book_for_user_win ,
          image = pic_for_btn_of_search_book_of_user,
           bg = "lightblue",
           border = 0,
           command = search_book_for_user_clicked,
           ).grid(row = 1,column = 2,sticky = 'w',pady = "5")

    #------------------------------------------------------#

    #----------Search Book by name Entry Box Area ------------#

    Label(search_book_for_user_win,
          text = "Search Book With name:",
          font = ("Arial","16","bold"),
          bg = "lightblue").grid(row = 2,column = 0,pady = "5")


    Seach_Book_for_user_by_name_entry_box_var = StringVar()
    Seach_Book_for_user_by_name_entry_box = ttk.Entry(search_book_for_user_win,
          textvariable = Seach_Book_for_user_by_name_entry_box_var,
          font = ("Arial","16","bold"))
    Seach_Book_for_user_by_name_entry_box.grid(row = 2,column = 1,sticky = 'w',ipady = "5",ipadx = "5",pady = "5")

    #Button For Search Books
    Button(search_book_for_user_win ,
          image = pic_for_btn_of_search_book_of_user,
           bg = "lightblue",
           border = 0,
           command = search_book_for_user_by_name_clicked,
           ).grid(row = 2,column = 2,sticky = 'w',pady = "5")

    #------------------------------------------------------#


    #Label For details book
    Label(search_book_for_user_win,
          text = "Book Details:",
          font = ("Arial","25","bold"),
          bg = "lightblue").grid(row = 3,column = 0,sticky = 'w')


    #---------------Button for list book Screen --------------------#

    pic_for_btn_of_book_list_for_user = PhotoImage(file = r"pics/List_of_books.png")
    Button(search_book_for_user_win ,
          image = pic_for_btn_of_book_list_for_user,
           bg = "lightblue",
           border = 0,
           command = show_book_list_to_user,
           ).grid(row = 3,column = 2,sticky = 'w',pady = "5")    

    #-----------------------------------------------------------------#


    #----------- Section For Book ID --------- #
    
    Label(search_book_for_user_win,
          text = "Book ID :",
          font = ("Arial","18","bold"),
          bg = "lightblue").grid(row = 5,column = 0,sticky = 'w',pady = "5")

    get_book_id_for_user_var = StringVar()
    get_book_id_for_user = ttk.Entry(search_book_for_user_win,
          textvariable = get_book_id_for_user_var,
          font = ("Arial","16","bold"),
              state = 'readonly')
    get_book_id_for_user.grid(row = 5,column = 1,sticky = 'w',ipady = "5",ipadx = "5")

    #-------------------------------------------#


    #----------- Section For Book Name --------- #
    
    Label(search_book_for_user_win,
          text = "Book Name :",
          font = ("Arial","18","bold"),
          bg = "lightblue").grid(row = 6 ,column = 0,sticky = 'w',pady = "5")


    get_book_name_for_user_var = StringVar()
    get_book_name_for_user = ttk.Entry(search_book_for_user_win,
          textvariable = get_book_name_for_user_var,
          font = ("Arial","16","bold"),
              state = 'readonly')
    get_book_name_for_user.grid(row = 6,column = 1,sticky = 'w',ipady = "5",ipadx = "5")

    #-------------------------------------------#

    #----------- Section For Book Authername --------- #
    
    Label(search_book_for_user_win,
          text = "Book Authername :",
          font = ("Arial","18","bold"),
          bg = "lightblue").grid(row = 7,column = 0,sticky = 'w',pady = "5")


    get_book_author_name_for_user_var = StringVar()
    get_book_author_name_for_user = ttk.Entry(search_book_for_user_win,
          textvariable = get_book_author_name_for_user_var,
          font = ("Arial","16","bold"),
              state = 'readonly')
    get_book_author_name_for_user.grid(row = 7,column = 1,sticky = 'w',ipady = "5",ipadx = "5")

    #-------------------------------------------#


    #----------- Section For Book Quantity --------- #
    
    Label(search_book_for_user_win,
          text = "Book Quantity : ",
          font = ("Arial","18","bold"),
          bg = "lightblue").grid(row = 8,column = 0,sticky = 'w',pady = "5")

    get_book_quantity_for_user_var =StringVar()
    get_book_quantity_for_user = ttk.Entry(search_book_for_user_win,
          textvariable = get_book_quantity_for_user_var,
          font = ("Arial","16","bold"),
              state = 'readonly')
    get_book_quantity_for_user.grid(row = 8,column = 1,sticky = 'w',ipady = "5",ipadx = "5")

    #-------------------------------------------#
    search_book_for_user_win.mainloop()


#Button 2
#===========================Section for Check Issued Book Screen=========================================#

def open_check_issued_book_screen():
    username =  username_to_use_after_login

    global check_issued_book_win
    check_issued_book_win = Toplevel(user_login_win)
    check_issued_book_win.config(bg = "lightblue")
    check_issued_book_win.geometry(center(check_issued_book_win,799,530))
    check_issued_book_win.resizable(0,0)
    check_issued_book_win.title("Issued Books")

    global list_box_for_show_issue_books
    global get_issued_book_by_user_id_var
    global get_issued_book_by_user_name_var
    global get_issued_book_by_user_author_name_var
    global get_issued_book_by_user_issue_date_var
    global get_issued_book_by_user_due_date_var
    
    #Adding Icon To The window
    check_issued_book_win.iconbitmap(r'pics/icon.ico')

    #Header For Check Issued Books----------#
    header_pic_for_check_issued_book_win = PhotoImage(file = r"pics/check_issued_books_header.png")
    Label(check_issued_book_win,
          image = header_pic_for_check_issued_book_win,
          ).grid(row = 0 , columnspan = 4)
    #--------------------------------------------#

    
    #--------------Making Frame For Books List-------------#
    
    frame_for_show_issue_book_list = Frame(check_issued_book_win,bg = 'lightblue')
    frame_for_show_issue_book_list.grid(rowspan = 10 ,column= 0,sticky = "w",pady = "5")

    #Frame Items
    #Label for list heading
    
    Label(frame_for_show_issue_book_list ,
          text = "Issued books by you:",
          font = ("Calibri","18","bold"),
          bg = "lightblue").grid(row = 0 ,column = 0)

    #List for Books Display
    list_box_for_show_issue_books = Listbox(
        frame_for_show_issue_book_list,
        font = ("Calibri","16","bold")
        )
    list_box_for_show_issue_books.grid(row = 1 ,column = 0,pady = "5")

    #Adding Scrolbar to the list
    sbr = Scrollbar(
        frame_for_show_issue_book_list,
        )
    sbr.grid(row = 1 ,column = 0,sticky = "e",ipady ="110" )

    #Adding Command In scrollbar so that it perform scrolling
    sbr.config(command = list_box_for_show_issue_books.yview )
    list_box_for_show_issue_books.config(yscrollcommand = sbr.set)

    #Making Button To see Books Details
    btn_image_for_book_detail_submit = PhotoImage(file = r"pics/more_details_button.png")
    Button(frame_for_show_issue_book_list,
           image =btn_image_for_book_detail_submit,
           bg = 'lightblue',
           border = 0 ,
           command = get_issued_books_by_user_details
           ).grid(row = 2,column = 0,pady = "5")

    #Add Data to List
    book_borrw_by_user_list = os.listdir(r"issued-books/"+username)
    
    for index,data in enumerate(book_borrw_by_user_list):
        with open(r'books/'+data,'r')as f:
            data = f.readline().strip('\n')            
            list_box_for_show_issue_books.insert(index,data)
    #--------------------------------------------------------------#

    #Label For Heading
    Label(check_issued_book_win,
          text = "Book Details :",
          font = ("Arial","20","bold"),
          bg = "lightblue").grid(row = 1,column = 1,sticky = 'w')
    
    #-----------------------------------#

    #--------------Section For Book ID -------------#

    Label(check_issued_book_win,
          text = "Book ID",
          font = ("Arial","16","bold"),
          bg = "lightblue").grid(row = 2,column = 1,sticky = 'w')


    get_issued_book_by_user_id_var = StringVar()
    get_issued_book_by_user_id = ttk.Entry(check_issued_book_win,
              font = ("Arial","13","bold"),
              state = 'readonly',
              textvariable = get_issued_book_by_user_id_var,
              )
    get_issued_book_by_user_id.grid(row = 2,column = 2,sticky = 'w',ipady = '5',ipadx = '45')

    #------------------------------------------------------#

    #--------------Section For Book Name -------------#

    Label(check_issued_book_win,
          text = "Book Name",
          font = ("Arial","16","bold"),
          bg = "lightblue").grid(row = 3,column = 1,sticky = 'w')


    get_issued_book_by_user_name_var = StringVar()
    get_issued_book_by_user_name = ttk.Entry(check_issued_book_win,
              font = ("Arial","13","bold"),
              state = 'readonly',
              textvariable = get_issued_book_by_user_name_var,
              )
    get_issued_book_by_user_name.grid(row = 3,column = 2,sticky = 'w',ipady = '5',ipadx = '45')

    #------------------------------------------------------#
    
    #--------------Section For Author Name -------------#

    Label(check_issued_book_win,
          text = "Author Name",
          font = ("Arial","16","bold"),
          bg = "lightblue").grid(row = 4,column = 1,sticky = 'w')


    get_issued_book_by_user_author_name_var = StringVar()
    get_issued_book_by_user_author_name = ttk.Entry(check_issued_book_win,
              font = ("Arial","13","bold"),
              state = 'readonly',
              textvariable = get_issued_book_by_user_author_name_var,
              )
    get_issued_book_by_user_author_name.grid(row = 4,column = 2,sticky = 'w',ipady = '5',ipadx = '45')

    #------------------------------------------------------#

    #--------------Section For issue date -------------#

    Label(check_issued_book_win,
          text = '''Issue Date
(yyyy,mm,dd)''',
          font = ("Arial","13","bold"),
          bg = "lightblue").grid(row = 5,column = 1,sticky = 'w')

    get_issued_book_by_user_issue_date_var = StringVar()
    get_issued_book_by_user_issue_date = ttk.Entry(check_issued_book_win,
              font = ("Arial","13","bold"),
              state = 'readonly',
              textvariable = get_issued_book_by_user_issue_date_var,
              )
    get_issued_book_by_user_issue_date.grid(row = 5,column = 2,sticky = 'w',ipady = '5',ipadx = '45')

    #------------------------------------------------------#

    #--------------Section For duedate -------------#

    Label(check_issued_book_win,
          text = '''Due Date
(yyyy,mm,dd)''',
          font = ("Arial","13","bold"),
          bg = "lightblue").grid(row = 6,column = 1,sticky = 'w')

    get_issued_book_by_user_due_date_var = StringVar()
    get_issued_book_by_user_due_date = ttk.Entry(check_issued_book_win,
              font = ("Arial","13","bold"),
              state = 'readonly',
              textvariable = get_issued_book_by_user_due_date_var,
              )
    get_issued_book_by_user_due_date.grid(row = 6,column = 2,sticky = 'w',ipady = '5',ipadx = '45')

    #------------------------------------------------------#

    check_issued_book_win.mainloop()









def check_issued_books_btn_clicked():
    books_borrow_by_user = check_user_issued_books()
    if len(books_borrow_by_user) < 1:
        messagebox.showerror("Error","You didn't issue any book yet")

    else:
        open_check_issued_book_screen()


#Function To check If there is any book issued to user or not
#If no book issued window will not opend
def check_user_issued_books():
    username = username_to_use_after_login
    list_of_books = os.listdir(r"issued-books/"+username)
    return list_of_books

#Button 3
#================================Command for edit info Button===================================================#
def User_editinfo_btn_clicked():
    messagebox.showinfo("info","Following Steps woulld be required \n\n\n1Admin Access Will Required To change your Details\
\n2)Password Must Be atleast 8 characters\n3)We only Accept Gmail And Yahoo Emails")


    global user_edit_info_win
    user_edit_info_win = Toplevel(user_login_win)
    user_edit_info_win.geometry(center(user_edit_info_win,370,570))
    user_edit_info_win.resizable(0,0)
    user_edit_info_win.config(bg = "lightblue")
    user_edit_info_win.title("Edit Info")
    
    #Adding Icon To The window
    user_edit_info_win.iconbitmap(r'pics/icon.ico')

    global password_box_for_edit_var
    global email_box_for_edit_var
    global gender_box_for_edit_var
    global usertype_box_for_edit_var


    #----------------Header Section---------------------#
    #Setting Header
    pic_for_user_edit_info_win_header = PhotoImage(file = r"pics/edit_User_Details.png")
    Label(user_edit_info_win,
          image = pic_for_user_edit_info_win_header,
          bg = "lightblue").pack(pady = ("5","0"))
    #Header Label
    Label(user_edit_info_win,
          text = "Edit Details",
          font = ("Calibri",22,"bold"),
          bg = "lightblue").pack()

    #---------------------------------------------------#


    #--------------Password Section-------------------#
    
    Label(user_edit_info_win,
          text = "Edit Password",
          font = ("Calibri",13,"bold"),
          bg = "lightblue").pack(pady = ("25","0"))


    password_box_for_edit_var = StringVar()
    password_box_for_edit = ttk.Entry(user_edit_info_win,
                                      textvariable = password_box_for_edit_var,
              font = ("Calibri",13,"bold"),)
    password_box_for_edit.pack(ipady = "5",ipadx = "45")

    #---------------------------------------------------#

    #--------------Email Section-------------------#
    
    Label(user_edit_info_win,
          text = "Edit Email",
          font = ("Calibri",13,"bold"),
          bg = "lightblue").pack(pady = ("10","0"))

    email_box_for_edit_var = StringVar()
    email_box_for_edit = ttk.Entry(user_edit_info_win,
              textvariable = email_box_for_edit_var,
              font = ("Calibri",13,"bold"),)
    email_box_for_edit.pack(ipady = "5",ipadx = "45")

    #---------------------------------------------------#

    #--------------Gender Section-------------------#
    
    Label(user_edit_info_win,
          text = "Edit Gender",
          font = ("Calibri",13,"bold"),
          bg = "lightblue").pack(pady = ("10","0"))


    gender_box_for_edit_var = StringVar()
    gender_box_for_edit = ttk.Combobox(user_edit_info_win,
                              width = 13,
                              textvariable = gender_box_for_edit_var,
                              font = ("Helvetica", 15, "normal"),
                              state = "readonly")
    gender_box_for_edit["value"] = ("Male","Female","Others")
    gender_box_for_edit.pack(ipadx=15,ipady= 2)

    #---------------------------------------------------#

    #--------------Type Section-------------------#
    
    Label(user_edit_info_win,
          text = "Edit User Type",
          font = ("Calibri",13,"bold"),
          bg = "lightblue").pack(pady = ("10","0"))


    usertype_box_for_edit_var = StringVar()
    usertype_box_for_edit = ttk.Combobox(user_edit_info_win,
                              width = 13,
                              textvariable = usertype_box_for_edit_var,
                              font = ("Helvetica", 15, "normal"),
                              state = "readonly")
    usertype_box_for_edit["value"] = ("Student","Teacher")
    usertype_box_for_edit.pack(ipadx=15,ipady= 2)

    #---------------------------------------------------#

    #----------------Button Section--------------------#
    pic_for_edit_user_record_btn = PhotoImage(file = r"pics/edit_button.png")
    Button(user_edit_info_win,
           image = pic_for_edit_user_record_btn,
           border = 0,
           command = edit_details_of_user_clicked,
           bg = "lightblue").pack(ipady= 20)

    #---------------------------------------------------#

    #Adding prewritten data to entry boxes
    add_data_to_edit_entry_box()

    
    user_edit_info_win.mainloop()


#This Function Add data to the Entry Boxes of edit user details screen
#To help The User
    
def add_data_to_edit_entry_box():
    username =  username_to_use_after_login

    with open(r"users/"+username, "r") as f:
        password = f.readline()
        email = f.readline()
        gender = f.readline()
        usertype = f.readline()

        password = password.strip()
        email = email.strip()
        gender = gender.strip()
        usertype = usertype.strip()
        
    
    password_box_for_edit_var.set(password)
    email_box_for_edit_var.set(email)
    gender_box_for_edit_var.set(gender)
    usertype_box_for_edit_var.set(usertype)


#Button 4
#================================Command for logout Button===================================================#
def User_logout_btn_clicked():
    messagebox.showinfo('logout','Logout Successful')
    destroy_userpanel_screen()
    main_screen()



#############################################
#############################################

#                   Commands for top level Screen user Panel Screen

#############################################

#Button 1
#================================Command for search books screen===================================================#


def search_book_for_user_clicked():
    book_id = Seach_Book_for_user_entry_box_var.get()
    if len(book_id) == 0:
        messagebox.showerror("Error","Enter Book Id First")
        
    book_list = os.listdir(r'Books')   #List of Books

    if book_id in book_list:  #If book id is in the book list available in library
        book_name, book_auther_name, book_quantity = get_book_info(book_id)


        get_book_id_for_user_var.set(book_id)
        get_book_name_for_user_var.set(book_name)
        get_book_author_name_for_user_var.set(book_auther_name)
        get_book_quantity_for_user_var.set(book_quantity)
    else:
        messagebox.showerror("No Book Exits","No Book With ID "+book_id+" Exist")


def search_book_for_user_by_name_clicked():

    book_name = Seach_Book_for_user_by_name_entry_box_var.get()
    get_books_name_list = os.listdir('books_name')
    book_name_list =[]

    if len(book_name) == 0:
        messagebox.showerror("Error","First enter the book name")
        
    else:   
        for x in get_books_name_list:
            book_name_list.append(x.lower())
                
        if book_name.lower() in book_name_list:
            with open(r"books_name/"+book_name,"r") as f:
                book_id = f.readline().strip("\n")
            
            book_name, book_auther_name, book_quantity = get_book_info(book_id)

            get_book_id_for_user_var.set(book_id)
            get_book_name_for_user_var.set(book_name)
            get_book_author_name_for_user_var.set(book_auther_name)
            get_book_quantity_for_user_var.set(book_quantity)
        else :
            messagebox.showerror("No Book Exits","No Book With Name Exist")
            
    

#Making Book List function helping for search book screen
def show_book_list_to_user():
    global book_list_win
    
    book_list_win = Toplevel(search_book_for_user_win)
    book_list_win.geometry(center(book_list_win,400,400))
    book_list_win.title("Books List")
    
    #Adding Icon To The window
    book_list_win.iconbitmap(r'pics/icon.ico')

    #Making List Box For book Display
    lbx = Listbox(
        book_list_win,
        font= ('comic sans ms',18,"bold"),
        )
    lbx.pack(side = 'left',expand = True,fill = 'both')   

    #heading
    lbx.insert(0,'id - Name')
    

    #Adding data to list
    book_list = os.listdir(r"books_name/")
    for index,data in enumerate(book_list,1):
        with open(r"books_name/"+data ,'r') as f:
            book_id_num = f.readline().strip('\n')
            lbx.insert(index,book_id_num+'- '+data)

        
    #making scrollbar for listbox
        
    sbr = Scrollbar(
        book_list_win,
        )
    sbr.pack(side = 'right' , fill = "y")

    #Making Command So that both Scrollbar and listbox can see each others
    sbr.config(command = lbx.yview)
    lbx.config(yscrollcommand = sbr.set)

    
    book_list_win.mainloop()
#------------------------------------------------------#

#Button 2
#=============================Command for check issue book screen===================================================#

def get_issued_books_by_user_details():
    
    book_name = list_box_for_show_issue_books.get('active')
    #getting book id
    with open(r'books_name/'+book_name,"r") as f:
        book_id = f.readline().strip("\n")
    
    bookname, authorname , book_quantity = get_book_info(book_id)  
    issued_date,due_name = get_issued_book_dates_for_user(book_id)

    
    get_issued_book_by_user_id_var.set(book_id)
    get_issued_book_by_user_name_var.set(bookname)
    get_issued_book_by_user_author_name_var.set(authorname)
    get_issued_book_by_user_issue_date_var.set(issued_date)
    get_issued_book_by_user_due_date_var.set(due_name)


def get_issued_book_dates_for_user(book_id):
    username =  username_to_use_after_login
    
    with open(r'issued-books/'+username+"/"+book_id , "r") as f:
        issued_date = f.readline()
        due_name = f.readline()

        issued_date = issued_date.strip()
        due_name = due_name.strip()

    return issued_date,due_name


#Button 3
#=============================Command for edit details screen===================================================#


#Screen for admin authentication
def edit_details_of_user_clicked():
    editted_password = password_box_for_edit_var.get()
    editted_email = email_box_for_edit_var.get()
    editted_gender = gender_box_for_edit_var.get()
    editted_usertype = usertype_box_for_edit_var.get()

    email_check = editted_email.split("@")

    if len(editted_password) < 8:
        messagebox.showerror("Error","Password Must Be atleast 8 characters")
        password_box_for_edit_var.set("")
        
    elif email_check[-1] != 'gmail.com' and email_check[-1] != 'yahoo.com':
        messagebox.showerror("Error","Sorry!! We only Accept Gmail and Yahoo mails")
        email_box_for_edit_var.set("")

    elif len(email_check[0]) < 4:
        messagebox.showerror("Error","Incorrect Password")
        email_box_for_edit_var.set("")

    else:
        global admin_pass_check_win
        global pic_for_admin_pass_check_for_edit_win_header
        global admin_authentiction_btn_img
        global admin_pass_entry_for_authentication, admin_pass_entry_for_authentication_var
        
        admin_pass_check_win = Toplevel(user_edit_info_win)
        admin_pass_check_win.title("Admin Authentication")
        admin_pass_check_win.geometry(center(admin_pass_check_win,400,370))
        admin_pass_check_win.resizable(0,0)
        admin_pass_check_win.configure(background = "lightblue")
        
        #Adding Icon To The window
        admin_pass_check_win.iconbitmap(r'pics/icon.ico')

        #Header Image
        pic_for_admin_pass_check_for_edit_win_header = PhotoImage(file=r"pics/admin.png")

        Label(
            admin_pass_check_win,
            image = pic_for_admin_pass_check_for_edit_win_header,
            border = 0,
            bg = "lightblue"
            ).pack(pady = ("10","0"))

        #Header Label
        Label(
            admin_pass_check_win,
            text = "Admin Authentication",
            font = ("Helvetica", 20, "bold"),
            bg = "lightblue"
            ).pack()

        #--------------------------------------------------------------------#
        
        Label(
            admin_pass_check_win,
            text = "Enter Password*",
            font = ("Helvetica", 10, "bold"),
            bg = "lightblue"
            ).pack(pady = ("20","0"))

        admin_pass_entry_for_authentication_var = StringVar()
        admin_pass_entry_for_authentication = ttk.Entry(
            admin_pass_check_win,
            font = ("Symbol", 15, "normal"),
            show = "*",
            textvariable = admin_pass_entry_for_authentication_var
            )
        admin_pass_entry_for_authentication.pack(ipady = 2, ipadx = 15)
        admin_pass_entry_for_authentication.focus()  #using so that the cursor is on the entry box
        
        #creating admin login button image object
        admin_authentiction_btn_img = PhotoImage(file = r"pics/login_button.png")

        #------Admin Check Button----------#
        admin_check_btn = Button(
            admin_pass_check_win,
            image = admin_authentiction_btn_img,
            border = 0,
            bg = "lightblue",
            command = check_admin_authentication
            )
        admin_check_btn.pack(pady = 30)
        #-------------------------------------#

        admin_pass_check_win.mainloop()
    #---------------------------------------------------#


#Function To Check Admin Password For Authentication

def check_admin_authentication():
    password = admin_pass_entry_for_authentication_var.get()

    with open(r"admin/admin_password", "r")as f: #Opening Admin File to read password for authentication
        admin_pass = f.readline()
        admin_pass = admin_pass.strip()

    if password == admin_pass:
        edit_user_details_for_edit()
    else:
        messagebox.showerror("Error","Incorrect Password")
        admin_pass_entry_for_authentication_var.set("")

        

#Function To Edit User Details
def edit_user_details_for_edit():
    username =  username_to_use_after_login

        
    with open(r'users/'+username, "w")as f:
        f.write(editted_password+"\n")
        f.write(editted_email+"\n")
        f.write(editted_gender+"\n")
        f.write(editted_usertype+"\n")

    messagebox.showinfo("Info","User Details Are Editted Successfully")

    user_edit_info_win.destroy()

    

############################################################################
############################################################################

                                                                    #End Of user panel Screen

############################################################################


    



#####################################################
#####################################################

#               Making Functions that are used most and several time in program

#####################################################






#making function to get data of book

def get_book_info(book_id):
    with open(r"Books/"+book_id,"r") as f:
        bookname = f.readline()
        bookname = bookname.strip()
        authorname = f.readline()
        authorname = authorname.strip()
        bookquantity = f.readline()
        bookquantity = bookquantity.strip()

    return bookname,authorname,bookquantity

#making function to get data of student

def get_student_info(user_name):
    with open(r"users/"+user_name,"r") as f:
        password = f.readline()
        password = password.strip()        
        email = f.readline()
        email = email.strip()        
        gender = f.readline()
        gender = gender.strip()
        usertype = f.readline()
        usertype = usertype.strip()

    return password,email,gender,usertype


######################################################################
######################################################################

#-----------------functions for reseting screen---------------------#

#-----------reseting registration screen----------#
    
def reg_screen_reset():
    reg_user_entry.delete(0,END)
    reg_pass_entry.delete(0,END)
    reg_email_entry.delete(0,END)

#-----------------------------------------------#


#-----------reseting userlogin screen----------#
    
def user_login_screen_reset():
    user_name_login_entry.delete(0,END)
    user_pass_login_entry.delete(0,END)

#-----------------------------------------------#

#-----------reseting admin login screen----------#
    
def admin_login_screen_reset():
    admin_pass_entry.delete(0,END)

#-----------------------------------------------#


#--------Functions For destroying Screens----------#

def destroy_mainscreen():
    win.destroy()

def destroy_adminscreen():
    admin_panel_screen.destroy()

def destroy_returnbook_screen():
    return_book_win.destroy()

def destroy_registration_screen():
    reg_screen.destroy()

def destroy_userpanel_screen():
    user_login_win.destroy()
    
#-------------------------------------------------------#        


#making function so that window opens in the middel of screen
def center(screen_name,width,height):
    sw = screen_name.winfo_screenwidth()
    sh = screen_name.winfo_screenheight()

    x = sw//2 - width//2
    y = sh//2 - height// 2

    data = str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y)

    return data


# main Function    
def main():
    main_screen()


#Calling Main Function
main()

#--------------------------------------------------------------------------The End----------------------------------------------------------------------------------------#
