from tkinter import *
import backend

window = Tk()

window.wm_title("Cadastro Livros")

""" funções back X front """

def view_command():
    backend.create_table()
    listagem.delete(0,END)
    for row in backend.view():
        listagem.insert(END, row)


def search_command():
    backend.create_table()
    listagem.delete(0,END)
    for row in backend.search(booktittle.get(), bookyear.get(), bookauthor.get(), bookisbn.get()):
        listagem.insert(END, row)


def insert_command():
    backend.create_table()
    backend.addbook(titulo.get(), autor.get(), ano.get(), isbn.get())
    listagem.delete(0, END)
    listagem.addbook(END,(titulo.get(), autor.get(), ano.get(), isbn.get()))


def get_selected_row(event):
    global selected_tuple
    index=listagem.curselection()[0]
    selected_tuple = listagem.get(index)
    booktittle.delete(0,END)
    booktittle.insert(END,selected_tuple[1])
    bookyear.delete(0,END)
    bookyear.insert(END,selected_tuple[2])
    bookauthor.delete(0,END)
    bookauthor.insert(END,selected_tuple[3])
    bookisbn.delete(0,END)
    bookisbn.insert(END,selected_tuple[4])


def delete_command():
    backend.create_table()
    backend.delete(selected_tuple[0])


def update_command():
    backend.create_table()
    backend.update(selected_tuple[0], titulo.get(), autor.get(), ano.get(), isbn.get())


""" caixas de texto e labels das mesmas """

booktittle = StringVar()
booktittle = Entry(window, textvariable=booktittle)
booktittle.grid(row=0, column=1)

tittlelabel = Label(window, text= "Titulo")
tittlelabel.grid(row = 0, column=0)


bookyear = StringVar()
bookyear = Entry(window, textvariable=bookyear)
bookyear.grid(row=1, column=1)

bookyearlabel = Label(window, text= "Ano")
bookyearlabel.grid(row = 1, column=0)


bookauthor = StringVar()
bookauthor = Entry(window, textvariable=bookauthor)
bookauthor.grid(row=0, column=3)

bookauthorlabel = Label(window, text= "Autor")
bookauthorlabel.grid(row = 0, column=2)


bookisbn = StringVar()
bookisbn = Entry(window, textvariable=bookisbn)
bookisbn.grid(row=1, column=3)

bookisbnlabel = Label(window, text= "ISBN")
bookisbnlabel.grid(row = 1, column=2)

""" botoes """

botaoviewall = Button(window, text = "Listar Todos", width=12, command = view_command)
botaoviewall.grid(row=2, column = 3)

botaosearch = Button(window, text = "Buscar", width=12, command = search_command)
botaosearch.grid(row = 3, column = 3)

botaoadd = Button(window, text = "Adicionar", width=12, command = insert_command)
botaoadd.grid(row=4, column = 3)

botaoupdate = Button(window, text = "Atualizar", width=12, command=update_command)
botaoupdate.grid(row = 5, column = 3)

botaodelete = Button(window, text = "Apagar", width=12, command =delete_command)
botaodelete.grid(row = 6, column = 3)

botaoclose = Button(window, text = "Fechar", width=12, command=window.destroy)
botaoclose.grid(row = 7, column = 3)

""" listagem itens """

listagem = Listbox(window, height = 6, width = 35)
listagem.grid(row = 2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

listagem.configure(yscrollcommand=scroll.set)
scroll.configure(command=listagem.yview)

listagem.bind('<<ListBoxSelect>>', get_selected_row)

window.mainloop()
