import tkinter as tk
import tkintermapview
from functions import *
from tkinter import font as tkfont
import geocoder

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global arqname
        self.title_font = tkfont.Font(family='Righteous', size=18)
        self.base_font = tkfont.Font(family='Righteous', size=13)
        self.geometry("472x750+600+15")
        self.title("AppChallenge")


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (Mapa,Login,Empresa):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Empresa")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Mapa(tk.Frame):


    def __init__(self, parent, controller):

        global imgm0,imgm1,imgm2,imgm3,imgm4

        imgm0 = tk.PhotoImage(file="./images/downExplorar.png")
        imgm1 = tk.PhotoImage(file="./images/downConversas.png")
        imgm2 = tk.PhotoImage(file="./images/pesquisa.png")
        imgm3 = tk.PhotoImage(file="./images/pesquisaMapa.png")
        imgm4 = tk.PhotoImage(file="./images/botaoLocalizacao.png")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.attributes()
        self.configure(bg='#16212D')

        def addMarcador(coords):
            new_marker = mapa.set_marker(coords[0], coords[1], text="")

        def click(polygon):
            print(f"polygon clicked - text: {polygon.name}")

        def localizacao():
            g = geocoder.ip('me')
            address = tkintermapview.convert_address_to_coordinates(g)
            mapa.set_position(address[0],address[1])

        #Criando o mapa
        mapa = tkintermapview.TkinterMapView(self, width=450, height=650, corner_radius=0)
        mapa.place(x=10, y=65)
        mapa.set_position(-22.2464046, -45.7063097)  # Santa Rita do Sapucai
        mapa.set_zoom(13)
        mapa.add_right_click_menu_command(label="Add Marker",
                                                command=addMarcador,
                                                pass_coords=True)


        # Adicionando os botões
        # explorar
        tk.Button(self, image=imgm0, bd=0, bg='#24172C', activebackground='#24172C').place(x=0, y=650)
        # conversas
        tk.Button(self, image=imgm1, bd=0, bg='#24172C', activebackground='#24172C').place(x=235, y=650)
        # pesquisa botao
        tk.Label(self, image=imgm3, bd=0, bg='#16212D', activebackground='#16212D').place(x=10, y=5)
        tk.Button(self, image=imgm2, bd=0, bg='#16212D', activebackground='#16212D').place(x=400, y=17)
        # pesquisa label
        location = tk.StringVar(self)
        tk.Entry(self, textvariable=location, width=23, foreground='white', font=controller.title_font, bd=0,
                 bg='#16212D').place(x=40, y=18)
        # localizacao
        tk.Button(self, image=imgm4, bd=0, bg='#F2EFE9', activebackground='#F2EFE9',command= lambda: localizacao()).place(x=390, y=580)

class Login(tk.Frame):

    def __init__(self, parent, controller):

        global imgl0,imgl1

        imgl0 = tk.PhotoImage(file="./images/netx.png")
        imgl1 = tk.PhotoImage(file="./images/goBotao.png")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#16212D')

        # Logo
        tk.Label(self, image=imgl0, bd=0, bg='#16212D', activebackground='#16212D').place(x=160, y=80)

        #Login
        name = tk.StringVar(self)
        name.set("Nome")
        tk.Entry(self, textvariable=name, width=35, foreground='black', font=controller.base_font, bd=0,
                 bg='#FFFFFF').place(x=80, y=330)
        password = tk.StringVar(self)
        password.set("Senha")
        tk.Entry(self, textvariable=password, width=35, foreground='black', font=controller.base_font, bd=0,
                 bg='#FFFFFF').place(x=80, y=380)
        tk.Button(self, image=imgl1, bd=0, bg='#24172C', activebackground='#24172C', command=lambda: controller.show_frame("Mapa")).place(x=210, y=550)

class Empresa(tk.Frame):

    def __init__(self, parent, controller):

        global imge0,imge1,imge2,imge3,imge4,imge5,imge6

        imge0 = tk.PhotoImage(file="./images/planos.png")
        imge1 = tk.PhotoImage(file="./images/contratar.png")
        imge2 = tk.PhotoImage(file="./images/fundoEmpresa.png")
        imge3 = tk.PhotoImage(file="./images/celularBotao.png")
        imge4 = tk.PhotoImage(file="./images/casaBotao.png")
        imge5 = tk.PhotoImage(file="./images/empresaBotao.png")
        imge6 = tk.PhotoImage(file="./images/seta.png")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#16212D')

        tk.Label(self, image=imge2, bd=0, bg='#16212D').place(x=0, y=20)
        tk.Label(self, text="TIM", bd=0, bg='#16212D', foreground='#FFFFFF', font=controller.title_font).place(x=215, y=210)
        tk.Button(self, image=imge6, bd=0, bg='#16212D', activebackground='#16212D', command=lambda: controller.show_frame("Mapa")).place(x=20, y=20)

        tk.Button(self, image=imge3, bd=0, bg='#16212D', activebackground='#16212D').place(x=100, y=265)
        tk.Button(self, image=imge4, bd=0, bg='#16212D', activebackground='#16212D').place(x=220, y=265)
        tk.Button(self, image=imge5, bd=0, bg='#16212D', activebackground='#16212D').place(x=340, y=265)

        # Planos
        tk.Label(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D').place(x=30, y=310)
        tk.Label(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D').place(x=30, y=350)
        tk.Label(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D').place(x=30, y=390)
        tk.Label(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D').place(x=30, y=430)
        tk.Label(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D').place(x=30, y=470)

        tk.Button(self, image=imge1, bd=0, bg='#16212D', activebackground='#16212D').place(x=350, y=310)
        tk.Button(self, image=imge1, bd=0, bg='#16212D', activebackground='#16212D').place(x=350, y=350)
        tk.Button(self, image=imge1, bd=0, bg='#16212D', activebackground='#16212D').place(x=350, y=390)
        tk.Button(self, image=imge1, bd=0, bg='#16212D', activebackground='#16212D').place(x=350, y=430)
        tk.Button(self, image=imge1, bd=0, bg='#16212D', activebackground='#16212D').place(x=350, y=470)







if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()