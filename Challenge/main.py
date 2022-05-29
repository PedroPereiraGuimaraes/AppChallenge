import tkinter as tk
import tkintermapview
from tkinter import font as tkfont
import geocoder
import json
import requests


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
        for F in (Mapa, Login, Empresa):
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
        global imgm0, imgm1, imgm2, imgm3, imgm4

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

        def localizacao(funcao,location):
            if funcao ==1:
                g = geocoder.ip('me')
                address = tkintermapview.convert_address_to_coordinates(g)
                mapa.set_position(address[0], address[1])
            else:
                address = tkintermapview.convert_address_to_coordinates(location)
                mapa.set_position(address[0], address[1])

        def getEstado():
            g = geocoder.ip('me')
            print(g.state)

        # Criando o mapa
        mapa = tkintermapview.TkinterMapView(self, width=450, height=650, corner_radius=0)
        mapa.place(x=10, y=65)
        mapa.set_position(-22.2464046, -45.7063097)
        mapa.set_zoom(13)


        # Adicionando os botões
        # explorar
        tk.Button(self, image=imgm0, bd=0, bg='#24172C', activebackground='#24172C',command=lambda:controller.show_frame("Empresa")).place(x=0, y=650)
        # conversas
        tk.Button(self, image=imgm1, bd=0, bg='#24172C', activebackground='#24172C').place(x=235, y=650)
        # pesquisa botao
        tk.Label(self, image=imgm3, bd=0, bg='#16212D', activebackground='#16212D').place(x=10, y=5)
        location = tk.StringVar(self)
        tk.Entry(self, textvariable=location, width=23, foreground='white', font=controller.title_font, bd=0,
                 bg='#16212D').place(x=40, y=18)
        tk.Button(self, image=imgm2, bd=0, bg='#16212D', activebackground='#16212D',
                  command=lambda: localizacao(2,location.get())).place(x=400, y=17)
        # localizacao
        tk.Button(self, image=imgm4, bd=0, bg='#F2EFE9', activebackground='#F2EFE9',
                  command=lambda: localizacao(1,"")).place(x=390, y=580)

class Login(tk.Frame):

    def __init__(self, parent, controller):
        global imgl0, imgl1

        imgl0 = tk.PhotoImage(file="./images/netx.png")
        imgl1 = tk.PhotoImage(file="./images/goBotao.png")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#16212D')

        # Logo
        tk.Label(self, image=imgl0, bd=0, bg='#16212D', activebackground='#16212D').place(x=160, y=80)

        # Login
        name = tk.StringVar(self)
        name.set("Nome")
        tk.Entry(self, textvariable=name, width=35, foreground='black', font=controller.base_font, bd=0,
                 bg='#FFFFFF').place(x=80, y=330)
        password = tk.StringVar(self)
        password.set("Senha")
        tk.Entry(self, textvariable=password, width=35, foreground='black', font=controller.base_font, bd=0,
                 bg='#FFFFFF').place(x=80, y=380)
        tk.Button(self, image=imgl1, bd=0, bg='#24172C', activebackground='#24172C',
                  command=lambda: controller.show_frame("Mapa")).place(x=210, y=550)

class Empresa(tk.Frame):

    def __init__(self, parent, controller):
        global imge0


        imge0 = tk.PhotoImage(file="./images/seta.png")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#16212D')

        def siglaEstado(estado):
            switch = {
                'Acre': 'AC',
                'Alagoas': 'AL',
                'Amapá': 'AP',
                'Amazonas': 'AM',
                'Bahia': 'BA',
                'Ceará': 'CE',
                'Distrito Federal': 'DF',
                'Espírito Santo': 'ES',
                'Goiás': 'GO',
                'Maranhão': 'MA',
                'Mato Grosso': 'MT',
                'Mato Grosso do Sul': 'MS',
                'Minas Gerais': 'MG',
                'Pará': 'PA',
                'Paraíba': 'PB',
                'Paraná': 'PR',
                'Pernambuco': 'PE',
                'Piauí': 'PI',
                'Rio de Janeiro': 'RJ',
                'Rio Grande do Norte': 'RN',
                'Rio Grande do Sul': 'RS',
                'Rondônia': 'RO',
                'Roraima': 'RR',
                'Santa Catarina': 'SC',
                'São Paulo': 'SP',
                'Sergipe': 'SE',
                'Tocantins': 'TO'
            }
            return switch.get(estado)

        def getLocation():
            g = geocoder.ip('me')
            return siglaEstado(g.state)

        def empresa(estado):
            request = requests.get(f"https://app-challenge-api.herokuapp.com/plans?state={estado}")
            todo = json.loads(request.content)
            lista = []
            for i in range(0, len(todo)):
                lista.insert(1,
                             f"Preço: {todo[i]['id']}  ISP: {todo[i]['isp']} Capacidade: {todo[i]['data_capacity']} Velocidade de download: {todo[i]['download_speed']} |"
                             f" Velocidade de upload: {todo[i]['upload_speed']} Descrição: {todo[i]['description']} Preço mensal: {todo[i]['price_per_month']}"
                             f" Tipo de internet: {todo[i]['type_of_internet']}")
            return lista



        lista = empresa(getLocation())
        langs_var = tk.StringVar(value=lista)
        tk.Button(self, image=imge0, bd=0, bg='#16212D', activebackground='#16212D',
                  command=lambda: controller.show_frame("Mapa")).place(x=20, y=20)
        listbox = tk.Listbox(self, bg='#16212D', width=40, height=20, listvariable=langs_var, foreground='#FFFFFF',font=controller.base_font).place(x=50, y=150)
        tk.Button(self, image=imgl1, bd=0, bg='#24172C', activebackground='#24172C',
                  command=lambda: controller.show_frame("Provedora")).place(x=210, y=600)




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
