# Este código copia o conteúdo da área de transferência (clipboard)
#
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QPlainTextEdit, QApplication
from PyQt6.QtCore import QSize

class Janela_Exemplo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))    
        self.setWindowTitle("Área de Transferência") 

        # Cria widget de texto e acrescenta texto explicativo
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Os textos copiados para a área de transferência de qualquer aplicação aparecerão aqui.\n\n")
        # posiciona e dimensiona o widget
        self.b.move(10,10)
        self.b.resize(400,200)

        QApplication.clipboard().dataChanged.connect(self.Mudou_area_transferencia)

    # Obtém conteúdo da área de transferência
    def Mudou_area_transferencia(self):
        text = QApplication.clipboard().text()
        self.b.insertPlainText(text + '\n' + '\n')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = Janela_Exemplo()
    janela.show()
    sys.exit( app.exec() )