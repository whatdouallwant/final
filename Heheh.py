from PyQt5 import QtCore
from PyQt5.QtWidgets import *
ap = QApplication([])
wind = QWidget()

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('X vs 0')
        self.setGeometry(800, 350, 300, 300)
        self.setStyleSheet('''background-color: #FFF8DC
''')

        self.board = [' '] * 9
        self.current_player = 'X'
        self.buttons = []

        for i in range(9):
            button = QPushButton('', self)
            button.clicked.connect(lambda _, i=i: self.make_move(i))
            self.buttons.append(button)

        self.r_but = QPushButton('Reset', self)
        self.r_but.clicked.connect(self.reset_game)
        self.r_but.setStyleSheet('''background-color: #FFDEAD
''')

        L = QVBoxLayout()
        grid = [self.buttons[i:i+3] for i in range(0,9,3)]

        for k in grid:
            k_l = QHBoxLayout()
            for button in k:
                k_l.addWidget(button)
            L.addLayout(k_l)

        L.addWidget(self.r_but)
        self.setLayout(L)

        self.update_ui()

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.update_ui()
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.current_player = '0' if self.current_player == 'X' else 'X'

    def update_ui(self):
        for i in range(9):
            self.buttons[i].setText(self.board[i])

    def check_winner(self):
        win_combo = [(0, 1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for combo in win_combo:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None
    
    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.update_ui()
        win_label = self.findChild(QLabel)
        if win_label:
            win_label.deleteLater()

    def show_winner(self, winner):
        message = QMessageBox(wind, text = f'Winner : {winner}' if winner != 'Tie' else 'Its a tie!')
        message.setWindowTitle('WIN')
        message.show()
        message.setStyleSheet('''background-color: #b3e9b7
''')

if __name__ == '__main__':
    app = QApplication([])
    ex = Game()
    ex.show()
    app.exec_()