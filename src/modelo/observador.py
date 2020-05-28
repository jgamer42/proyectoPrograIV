class Observador():
    def __init__(self,subject):
        self.sujeto = subject
        subject.agregar_observador(self)
    
    def notificar(self):
        print("estado del dato: ",self.sujeto.estado)