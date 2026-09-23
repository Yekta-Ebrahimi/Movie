import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from main_window import Ui_MainWindow
from sql import Database

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.selected_id = 0

        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_edit.clicked.connect(self.edit)
        self.ui.pushButton_delete.clicked.connect(self.delete)
        self.ui.pushButton_refresh.clicked.connect(self.show_movies)

        self.ui.tableWidget_movies.itemClicked.connect(self.select)
        self.show_movies()

    def add(self):

        name = self.ui.lineEdit_name.text()
        author = self.ui.lineEdit_author.text()
        year = self.ui.lineEdit_year.text()
        genre = self.ui.lineEdit_genre.text()
        rating = self.ui.lineEdit_rating.text()

        self.db.add_movie(name, author, year, genre, rating)
        self.show_movies()


    def show_movies(self):

        movies = self.db.get_movies()
        self.ui.tableWidget_movies.setRowCount(0)

        for movie in movies:
            row = self.ui.tableWidget_movies.rowCount()
            self.ui.tableWidget_movies.insertRow(row)
            for column in range(6):
                self.ui.tableWidget_movies.setItem( row, column,QTableWidgetItem(str(movie[column])))

    def select(self, item):

        row = item.row()

        self.selected_id = int( self.ui.tableWidget_movies.item(row, 0).text())
        
        self.ui.lineEdit_name.setText(self.ui.tableWidget_movies.item(row, 1).text())

        self.ui.lineEdit_author.setText(self.ui.tableWidget_movies.item(row, 2).text())

        self.ui.lineEdit_year.setText(self.ui.tableWidget_movies.item(row, 3).text())

        self.ui.lineEdit_genre.setText(self.ui.tableWidget_movies.item(row, 4).text())

        self.ui.lineEdit_rating.setText( self.ui.tableWidget_movies.item(row, 5).text())

    def edit(self):

        name = self.ui.lineEdit_name.text()
        author = self.ui.lineEdit_author.text()
        year = self.ui.lineEdit_year.text()
        genre = self.ui.lineEdit_genre.text()
        rating = self.ui.lineEdit_rating.text()

        self.db.edit_movie(
            self.selected_id,
            name,
            author,
            year,
            genre,
            rating
        )

        self.show_movies()

    def delete(self):

        self.db.delete_movie(self.selected_id)
        self.show_movies()

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()