from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from functools import partial
import customs as cs
import credentials as cr
import pymysql
import hashlib
from tkinter import filedialog
from registerr import registration
from bookk import book


class login(registration,book):
 
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.SingIn()

    def SingIn(self):
        # ========================================================================
        # ============================background image============================
        # ========================================================================

    
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        
        # ========================================================================
        # ============ Left Side Image ===========================================
        # ========================================================================


        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================


        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)


        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================


        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)


        # ========================================================================
        # ============================username====================================
        # ========================================================================


        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entrylog = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entrylog.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)


        # ===== Username icon =========


        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)


        # ========================================================================
        # ============================login button================================
        # ========================================================================


        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.login)
        self.login.place(x=20, y=10)
       


        # =========== Sign Up ==================================================


        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",command=self.Signup)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)



        # ========================================================================
        # ============================password====================================
        # ========================================================================


        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entrylog = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entrylog.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)


        # ======== Password icon ================


        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)


        # ========= show/hide password ==================================================================

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.show_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entrylog.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entrylog.config(show='*')    

    def login(self):

      if self.username_entrylog.get()=="" or self.password_entrylog.get()=="":

         messagebox.showerror("Error","All fields are required")

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='',database='achraf')

            cur=con.cursor()

            cur.execute('select * from register where username=%s and passord=%s',(self.username_entrylog.get(),self.password_entrylog.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password',)

               self.loginclear()

               self.username_entrylog.focus()

            else:

               con.close()
               messagebox.showinfo("Success", "Login successful")
               self.management()
               self.loginclear()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}')

    def loginclear(self):

      self.username_entrylog.delete(0,END)

      self.password_entrylog.delete(0,END)
""" 
class registration(library):
    def Signup(self):
        self.window.title('Signup Page')


        # ========================================================================
        # ============================background image============================
        # ========================================================================


        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')


        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)


        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================


        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign Up", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================Register button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='Register', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.register)
        self.login.place(x=20, y=10)

       # =========== Back button ==================================================

    
        self.sign_label = Label(self.lgn_frame, text='Back to login?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\back.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",command=self.SingIn)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
    
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    
       # ========================================================================
       # ============================connection database=========================
       # ========================================================================
        
    def register(self):
     if self.username_entry.get() == "" or self.password_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
     else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="achraf")
            cur = con.cursor()

            cur.execute("SELECT * FROM register WHERE username=%s", self.username_entry.get())
            row = cur.fetchone()

            if row is not None:
                messagebox.showerror("Error", "User already exists, please try with another username")
                self.regclear()
                self.username_entry.focus()
            else:
                # Hash the password using SHA-256
                hashed_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()
                hashed_username = hashlib.sha256(self.username_entry.get().encode()).hexdigest()

                cur.execute("INSERT INTO register VALUES(%s, %s)", (hashed_username, hashed_password))
                con.commit()
                con.close()

                messagebox.showinfo("Success", "Register successful")
                self.regclear()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")

    def regclear(self):

      self.username_entry.delete(0,END)

      self.password_entry.delete(0,END)





class book:
    def management(self):
       # Left Frame
        self.frame_1 = Frame(self.window, bg=cs.color_1)
        self.frame_1.place(x=0, y=0, width=740, relheight = 1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = cs.color_2)
        self.frame_2.place(x=740,y=0,relwidth=1, relheight=1)

        # A frame inside the right frame
        self.frame_3 = Frame(self.frame_2, bg= cs.color_2)
        self.frame_3.place(x=0, y=300,relwidth=1, relheight=1)

        # All the Buttons in the frame 2
        self.add_book = Button(self.frame_2, text='Add Book', font=(cs.font_1, 12), bd=2, command=self.AddNewBook,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=50,y=40,width=100)
        #self.issue_book = Button(self.frame_2, text='Issue Book', font=(cs.font_1, 12), bd=2, command=self.GetData_for_IssueBook,cursor="hand2", bg=cs.color_7,fg=cs.color_3).place(x=50,y=100,width=100)
        #self.return_book = Button(self.frame_2, text='Return Book', font=(cs.font_1, 12), bd=2, command=self.ReturnBook,cursor="hand2", bg=cs.color_6,fg=cs.color_3).place(x=50,y=160,width=100)
        self.all_book = Button(self.frame_2, text='All Books', font=(cs.font_1, 12), bd=2, command=self.ShowBooks,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=50,y=100,width=100)
        
        self.search_book = Button(self.frame_2, text='Search Book', font=(cs.font_1, 12), bd=2, command=self.GetBookNametoSearch,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=180,y=40,width=100)
        #self.all_borrow_records = Button(self.frame_2, text='Book Holders', font=(cs.font_1, 12), bd=2, command=self.AllBorrowRecords, cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=180,y=100,width=100)
        self.clear = Button(self.frame_2, text='Clear Screen', font=(cs.font_1, 12), bd=2, command=self.ClearScreen,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=180,y=100,width=100)
        self.exit = Button(self.frame_2, text='Exit', font=(cs.font_1, 12), bd=2, command=self.Exit,cursor="hand2", bg=cs.color_5,fg=cs.color_3).place(x=110,y=160,width=100)
    
   
    
    # Function 3: It gets call from 'Function 14' and 'Function 17' when the 
    # user clicks on a record
    def OnSelectedforShowBooks(self, a):
        self.dlt_record = Button(self.frame_3, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteBook,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=50,y=0,width=100)
        self.update_record = Button(self.frame_3, text='Update', font=(cs.font_1, 12), bd=2, command=self.UpdateBookDetails,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=180,y=0,width=100)
        self.update_record = Button(self.frame_3, text='Book image', font=(cs.font_1, 12), bd=2,command=self.display, cursor="hand2", bg=cs.color_6,fg=cs.color_3).place(x=110,y=50,width=100)
    # Function 4: It gets call from 'Function 3', is used to delete a book
    # but there is a conition. If a book is holding by anyone, the user can't
    # delete the book
    def DeleteBook(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')
            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from borrow_record where book_id=%s", row[0])
                var = curs.fetchall()

                if len(var) != 0:
                    messagebox.showwarning("Critical Warning!", "You can't delete this book record")
                else:
                    curs.execute("delete from book_list where book_id=%s",
                    (
                        row[0]
                    ))
                    messagebox.showinfo("Success!", "The book record has been deleted")
                    connection.commit()
                    connection.close()
                    self.ClearScreen()
                    self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)   

    # Function 9: It gets call from 'Function 3', is used to update 
    # a book record(book name, author, edition, price, quantity, etc.)
    def UpdateBookDetails(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220,y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220,y=60, width=300)

        book_name = Label(self.frame_1, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=100)
        self.bookname_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.bookname_entry.insert(0, row[1])
        self.bookname_entry.place(x=220,y=130, width=300)

        author = Label(self.frame_1, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=170)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.insert(0, row[2])
        self.author_entry.place(x=220,y=200, width=300)

        edition = Label(self.frame_1, text="Edition", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=240)
        self.edition_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.edition_entry.insert(0, row[3])
        self.edition_entry.place(x=220,y=270, width=300)

        price = Label(self.frame_1, text="Price", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=310)
        self.price_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.price_entry.insert(0, row[4])
        self.price_entry.place(x=220,y=340, width=300)

        quantity = Label(self.frame_1, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=380)
        self.qty_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.qty_entry.insert(0, row[5])
        self.qty_entry.place(x=220,y=410, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=partial(self.SubmitforUpdateBook, row), cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=310,y=459,width=100)

    # It updates a entry in the 'book_list' table
    def SubmitforUpdateBook(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update book_list set book_name=%s,author=%s,edition=%s,price=%s,qty=%s where book_id=%s",
            (
                self.bookname_entry.get(),
                self.author_entry.get(),
                self.edition_entry.get(),
                self.price_entry.get(),
                self.qty_entry.get(),
                row[0]
            ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def GetBookNametoSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Search Book", font=(cs.font_1, 30, "bold"), bg=cs.color_4).place(x=250, y=40)
        book_name = Label(self.frame_1, text="Enter the Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=140)
        self.book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.book_entry.place(x=220,y=175, width=300)
        
        self.search_bt = Button(self.frame_1, text='Search', font=(cs.font_1, 12), bd=2, command=self.SearchBook,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=310,y=215,width=100)

    # Function 14:
    def ShowBooks(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('book_id', text='Book ID', anchor=W)
        self.tree.heading('book_name', text='Book Name', anchor=W)
        self.tree.heading('author', text='Author', anchor=W)
        self.tree.heading('edition', text='Edition', anchor=W)
        self.tree.heading('price', text='Price', anchor=W)
        self.tree.heading('qty', text='Quantity', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from book_list")
            rows=curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty","There is no data to show",parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list)+1), values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    
    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchBook(self):
        if self.book_entry.get() == "":
            messagebox.showerror("Error!", "Please Enter the Book Name")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from book_list where book_name like %s", ("%" + self.book_entry.get() + "%"))
                rows=curs.fetchall()
                if rows == None:
                    messagebox.showinfo("Database Empty","There is no data to show",parent=self.window)
                    connection.close()
                    self.ClearScreen()
                else:
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
                
            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('book_id', text='Book ID', anchor=W)
            self.tree.heading('book_name', text='Book Name', anchor=W)
            self.tree.heading('author', text='Author', anchor=W)
            self.tree.heading('edition', text='Edition', anchor=W)
            self.tree.heading('price', text='Price', anchor=W)
            self.tree.heading('qty', text='Quantity', anchor=W)
            self.tree.pack()
            # Double click on a row
            self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list)+1), values=(list[0], list[1], list[2], list[3], list[4], list[5]))
    
    
    
    # Function 19: This function displays widgets for adding new books
    def AddNewBook(self):
        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=30)
        self.id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_entry.place(x=220,y=60, width=300)

        book_name = Label(self.frame_1, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=100)
        self.bookname_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.bookname_entry.place(x=220,y=130, width=300)

        author = Label(self.frame_1, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=170)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.place(x=220,y=200, width=300)

        edition = Label(self.frame_1, text="Edition", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=240)
        self.edition_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.edition_entry.place(x=220,y=270, width=300)

        price = Label(self.frame_1, text="Price", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=310)
        self.price_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.price_entry.place(x=220,y=340, width=300)

        quantity = Label(self.frame_1, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,y=380)
        self.qty_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.qty_entry.place(x=220,y=410, width=300)
        self.upload_image_bt_1 = Button(self.frame_1, text='Upload Image', font=(cs.font_1, 12), bd=2,command=self.upload_file, cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=220,y=450,width=150)
        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.Submit,cursor="hand2", bg=cs.color_2,fg=cs.color_3).place(x=220,y=500,width=100)

    
    # Function 21: This function adds a new book record'''
    def Submit(self):
        if self.id_entry.get() == "" or self.bookname_entry.get() == "" or self.author_entry.get() == "" or self.edition_entry.get() == "" or self.price_entry.get() == "" or self.qty_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from book_list where book_id=%s", self.id_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","This book id is already exists, please try again with another one",parent=self.window)
                else:
                    sql="insert into book_list (book_id,book_name,author,edition,price,qty,image) values(%s,%s,%s,%s,%s,%s,%s)"
                    data = (self.id_entry.get(),self.bookname_entry.get(),self.author_entry.get(),self.edition_entry.get(),self.price_entry.get(),self.qty_entry.get(),filename)
                    curs.execute(sql, data)
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    
    # Reset all the entry fields of add new book form
    def reset_fields(self):
        self.id_entry.delete(0, END)
        self.bookname_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.edition_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.qty_entry.delete(0, END)
    
    # Removes all widgets from the frame 1 and frame 3
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

        for widget in self.frame_3.winfo_children():
            widget.destroy()

    '''Exit window'''
    def Exit(self):
        self.window.destroy()

   #function upload image 
    def upload_file (self):
      global filename
      filename=filedialog.askopenfilename( filetypes=[("png file","*.png"),("JPG file", "*.jpg"),("JPEG file", "*.JPEG")])
    #function dispaly image
    def display(self):
        global img
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
        curs = connection.cursor()
        curs.execute("select image from book_list where book_id=%s", row[0])
        var = curs.fetchone()
        img=Image.open(var[0])
        img=img.resize((100,100))
        img=ImageTk.PhotoImage(img)
        Lebelimage=Label(self.frame_2,image=img)
        Lebelimage.place(x=110,y=380)
        print(var[0])
        connection.commit()
        connection.close()
"""
def page():
    window = Tk()
    login(window)
    window.mainloop()


if __name__ == '__main__':
    page()