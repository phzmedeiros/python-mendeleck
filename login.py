import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFrame, QLabel,
    QLineEdit, QPushButton, QFormLayout, QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import Qt

class CreateAccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Login")
        self.setFixedSize(800, 500)
        self.init_ui()

    def init_ui(self):
        # Define um gradiente de fundo para a janela principal
        self.setStyleSheet("""
        QMainWindow {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #36D1DC, stop: 1 #5B86E5);
        }
        """)

        # Cria um widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)
        # Ajusta as margens para posicionar o cartão mais centralizado
        main_layout.setContentsMargins(0, 50, 0, 50)

        # Cria um "cartão" branco
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
            }
        """)

        # Layout interno do cartão
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(30, 30, 30, 30)

        # Título
        title_label = QLabel("Login")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #333;
        """)
        form_layout.addWidget(title_label)

        form_layout.addSpacing(20)  # Espaçamento entre título e campos

        # Layout de formulário para Name, E-mail e Password
        fields_layout = QFormLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nome")
        self.name_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5B86E5;
            }
        """)

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("E-mail")
        self.email_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5B86E5;
            }
        """)

        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Senha")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5B86E5;
            }
        """)

        fields_layout.addRow(self.name_edit)
        fields_layout.addRow(self.email_edit)
        fields_layout.addRow(self.password_edit)
        form_layout.addLayout(fields_layout)

        form_layout.addSpacing(20)  # Espaçamento entre campos e botões

        # Layout horizontal para os botões
        buttons_layout = QHBoxLayout()

        signup_button = QPushButton("Cadastrar")
        signup_button.setStyleSheet("""
            QPushButton {
                background-color: #5B86E5;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #4a75c4;
            }
        """)

        signin_button = QPushButton("Entrar")
        signin_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #5B86E5;
                border: 2px solid #5B86E5;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5B86E5;
                color: white;
            }
        """)

        buttons_layout.addWidget(signup_button)
        buttons_layout.addWidget(signin_button)
        form_layout.addLayout(buttons_layout)

        # Adiciona o "cartão" ao layout principal
        main_layout.addWidget(form_frame, alignment=Qt.AlignCenter)

        # Conecta sinais (caso queira tratar eventos de clique)
        signup_button.clicked.connect(self.sign_up)
        signin_button.clicked.connect(self.sign_in)

    def sign_up(self):
        # Lógica para criar conta (exemplo)
        name = self.name_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        print(f"Sign Up com: {name}, {email}, {password}")

    def sign_in(self):
        # Lógica para ir para tela de login (exemplo)
        print("Sign In clicado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateAccountWindow()
    window.show()
    sys.exit(app.exec())
