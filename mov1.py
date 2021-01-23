from tkinter import *
#pip install imdbpy
import imdb


def search():
    #create a window on top of other window
    root2=Toplevel()

    root2.geometry('890x600+200+50')
    root2.title('Movie Information')





    backpic=PhotoImage(file='black.png')
    backpicLabel= Label(root2, image=backpic).place(x=0,y=0)

    titleLabel = Label(root2, text='Title',font=('cooper black',30,'bold'),fg='#000000')
    titleLabel.place(x=60,y=30)

    titlenameLabel = Label(root2,font=('cooper black', 30, 'bold'), fg='#000000')
    titlenameLabel.place(x=300, y=30)

    directorLabel = Label(root2, text='Director', font=('cooper black', 30, 'bold'), fg='#000000')
    directorLabel.place(x=60, y=100)

    directornameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000')
    directornameLabel.place(x=300, y=100)

    yearLabel = Label(root2, text = 'Year',font=('cooper black', 30, 'bold'), fg='#000000')
    yearLabel.place(x=60, y=170)

    yearnameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000')
    yearnameLabel.place(x=300, y=170)

    durationLabel = Label(root2,text='Duration', font=('cooper black', 30, 'bold'), fg='#000000')
    durationLabel.place(x=60, y=240)

    durationnameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000')
    durationnameLabel.place(x=300, y=240)

    genreLabel = Label(root2,text='Genre', font=('cooper black', 30, 'bold'), fg='#000000')
    genreLabel.place(x=60, y=310)

    genrenameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000')
    genrenameLabel.place(x=300, y=310)

    ratingLabel = Label(root2,text = 'Rating', font=('cooper black', 30, 'bold'), fg='#000000')
    ratingLabel.place(x=60, y=380)

    ratingnameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000')
    ratingnameLabel.place(x=300, y=380)

    castLabel = Label(root2,text='Cast', font=('cooper black', 30, 'bold'), fg='#000000')
    castLabel.place(x=60, y=450)

    castnameLabel = Label(root2, font=('cooper black', 30, 'bold'), fg='#000000',wraplength=615, justify=LEFT)
    castnameLabel.place(x=300, y=450)
 # importing from imdb
    test=imdb.IMDb()
    movie_name=movieentry.get()
# searching movies
    movies =test.search_movie(movie_name)
    index = movies[0].getID()
    film=test.get_movie(index)

# updating text variables for root2 tab
    title = film['title']
    titlenameLabel.config(text=title)

    year=film['year']
    yearnameLabel.config(text=year)

    rating=film['rating']
    ratingnameLabel.config(text=rating)

    genre=film['genre']
    genrenameLabel.config(text=genre)

# rest are lists which needs to be printed using for loop
    for director in film['directors']:
        directornameLabel.config(text=director)

 # converting duration i.e, minutes to hours
    for duration in film['runtimes']:
        h = int(duration) // 60
        m= int(duration) % 60
        durationnameLabel.config(text=str(h)+'h '+str(m)+' m')
# displaying cast
    cast=film['cast']
    list_of_cast=(',').join(map(str,cast))
    castlist=list_of_cast.split(',')
    listitem=castlist[0:4]
    strr=''

    for i in listitem:
        if i == listitem[3]:
            strr=strr+i+'.'
        else:
            strr=strr+i+','
    castnameLabel.config(text=strr)

    root2.mainloop()


root= Tk()

root.geometry('1057x650+100+40')

root.title('Movie Description created by Sai Chaitanya')

bgpic = PhotoImage(file='pic.png')
bgLabel = Label(root, image=bgpic).place(x=0, y=0)

movieLabel=Label(root, text='Movie Name:',font=('algerian',30,'bold'),bg='#DEDCDD',fg='gray20')
movieLabel.place(x=200, y=570)

movieentry = Entry(root, font=('FELEX TITLING',20,'bold'),border=5,relief=GROOVE,justify=CENTER)
movieentry.place(x=490, y=575)


moviesearchbutton = Button(root, text ='SEARCH', font=('FELEX TITLING',20,'bold'),border=5,relief=GROOVE,bg='#D9D7D9',command=search)
moviesearchbutton.place(x=880, y=565)

root.mainloop()
