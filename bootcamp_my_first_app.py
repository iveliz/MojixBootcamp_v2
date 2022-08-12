import streamlit as st 

class textoGuia(st):
    def init(self):
        super().textoGuia()
        
        self.inicializar_gua()
    
    def inicializar_gua(self):
        self.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
        self.geometry('300x3000')

        texto = ""
        self.lb1_texto = st.Label(self, text=texto)

        self.fuente = st.StringVar()
        self.fuente.trace('w', self.cambiar_fuente)

        fuentes = ('Courier', 'Times')
        opt_fuentes = st.OptionMenu(self, self.fuente, *fuentes)
        self.tamgnio = tk.StringVar(self)
        self.tamgnio.trace('w', self.cambiar_fuente)
        spx_tamagnio = st.Spinbox(self, from=10, textvariable=self.tamagnio)

        self.lb1_texto.pack(padx=20, pady=20)
        opt_fuentes.pack(side=st.LEFT, fill=st.BOTH, expand=true)
        spx_tamagnio.pack(side=st.LEFT, fill=st.BOTH, expand=true)
     


