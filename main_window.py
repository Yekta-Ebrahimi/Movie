# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #0B1220;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #7DD3FC;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Main Title */\n"
"QLabel#label_title {\n"
"    color: #4DA3FF;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Subtitle */\n"
"QLabel#label_subtitle {\n"
"    color: #94A3B8;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"/* Line Edits */\n"
"QLineEdit {\n"
"    background-color: #162238;\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #263B5A;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4DA3FF;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radi"
                        "us: 10px;\n"
"    padding: 9px 18px;\n"
"}\n"
"\n"
"QPushButton#pushButton_add {\n"
"    background-color: #1976D2;\n"
"}\n"
"\n"
"QPushButton#pushButton_add:hover {\n"
"    background-color: #2196F3;\n"
"}\n"
"\n"
"QPushButton#pushButton_edit {\n"
"    background-color: #1565C0;\n"
"}\n"
"\n"
"QPushButton#pushButton_edit:hover {\n"
"    background-color: #1E88E5;\n"
"}\n"
"\n"
"QPushButton#pushButton_delete {\n"
"    background-color: #D84343;\n"
"}\n"
"\n"
"QPushButton#pushButton_delete:hover {\n"
"    background-color: #EF5350;\n"
"}\n"
"\n"
"QPushButton#pushButton_refresh {\n"
"    background-color: #0088CC;\n"
"}\n"
"\n"
"QPushButton#pushButton_refresh:hover {\n"
"    background-color: #00A6F4;\n"
"}\n"
"\n"
"/* Table */\n"
"QTableWidget {\n"
"    background-color: #111C2E;\n"
"    color: #EAF2FF;\n"
"    border: 2px solid #263B5A;\n"
"    border-radius: 10px;\n"
"    gridline-color: #263B5A;\n"
"    selection-background-color: #1976D2;\n"
"    selection-color: #FFFFFF;\n"
"    font-family: \"Segoe UI\";\n"
""
                        "    font-size: 13px;\n"
"}\n"
"\n"
"/* Table Header */\n"
"QHeaderView::section {\n"
"    background-color: #172A46;\n"
"    color: #7DD3FC;\n"
"    padding:")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_edit = QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.gridLayout.addWidget(self.pushButton_edit, 6, 2, 1, 1)

        self.label_genre = QLabel(self.centralwidget)
        self.label_genre.setObjectName(u"label_genre")

        self.gridLayout.addWidget(self.label_genre, 4, 0, 1, 1)

        self.lineEdit_author = QLineEdit(self.centralwidget)
        self.lineEdit_author.setObjectName(u"lineEdit_author")

        self.gridLayout.addWidget(self.lineEdit_author, 2, 1, 1, 2)

        self.lineEdit_year = QLineEdit(self.centralwidget)
        self.lineEdit_year.setObjectName(u"lineEdit_year")

        self.gridLayout.addWidget(self.lineEdit_year, 3, 1, 1, 2)

        self.label_rating = QLabel(self.centralwidget)
        self.label_rating.setObjectName(u"label_rating")

        self.gridLayout.addWidget(self.label_rating, 5, 0, 1, 1)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout.addWidget(self.pushButton_add, 6, 0, 1, 2)

        self.lineEdit_rating = QLineEdit(self.centralwidget)
        self.lineEdit_rating.setObjectName(u"lineEdit_rating")

        self.gridLayout.addWidget(self.lineEdit_rating, 5, 1, 1, 2)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.gridLayout.addWidget(self.pushButton_delete, 6, 3, 1, 1)

        self.lineEdit_genre = QLineEdit(self.centralwidget)
        self.lineEdit_genre.setObjectName(u"lineEdit_genre")

        self.gridLayout.addWidget(self.lineEdit_genre, 4, 1, 1, 2)

        self.tableWidget_movies = QTableWidget(self.centralwidget)
        if (self.tableWidget_movies.columnCount() < 6):
            self.tableWidget_movies.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_movies.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_movies.setObjectName(u"tableWidget_movies")

        self.gridLayout.addWidget(self.tableWidget_movies, 7, 0, 1, 5)

        self.label_year = QLabel(self.centralwidget)
        self.label_year.setObjectName(u"label_year")

        self.gridLayout.addWidget(self.label_year, 3, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 2)

        self.pushButton_refresh = QPushButton(self.centralwidget)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.gridLayout.addWidget(self.pushButton_refresh, 6, 4, 1, 1)

        self.label_author = QLabel(self.centralwidget)
        self.label_author.setObjectName(u"label_author")

        self.gridLayout.addWidget(self.label_author, 2, 0, 1, 1)

        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_genre.setText(QCoreApplication.translate("MainWindow", u"Genre:", None))
        self.label_rating.setText(QCoreApplication.translate("MainWindow", u"Rating:", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget_movies.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget_movies.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem2 = self.tableWidget_movies.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        ___qtablewidgetitem3 = self.tableWidget_movies.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        ___qtablewidgetitem4 = self.tableWidget_movies.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        ___qtablewidgetitem5 = self.tableWidget_movies.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
    # retranslateUi

