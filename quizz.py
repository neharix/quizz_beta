import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuizzWindow(object):
    def setupUi(self, QuizzWindow):
        QuizzWindow.setObjectName("QuizzWindow")
        QuizzWindow.setFixedSize(1276, 796)
        QuizzWindow.setStyleSheet("background-color: #2e2d45;")
        self.quizzwidget = QtWidgets.QWidget(QuizzWindow)
        self.quizzwidget.setObjectName("quizzwidget")
        self.next_btn = QtWidgets.QPushButton(self.quizzwidget)
        self.next_btn.setGeometry(QtCore.QRect(860, 20, 111, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #4bca64;\n"
            "border-radius: 25px;\n"
            "color: white"
        )
        self.next_btn.setObjectName("next_btn")
        self.next_btn.setText("Indiki")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.quizzwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 640, 1121, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.answer_btn_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.answer_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.answer_btn_layout.setObjectName("answer_btn_layout")
        self.answer1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer1.sizePolicy().hasHeightForWidth())
        self.answer1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.answer1.setFont(font)
        self.answer1.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #514bca;\n"
            "border-radius: 50px;\n"
            "color: white;\n"
            ""
        )
        self.answer1.setObjectName("answer1")
        self.answer_btn_layout.addWidget(self.answer1)
        self.answer2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer2.sizePolicy().hasHeightForWidth())
        self.answer2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.answer2.setFont(font)
        self.answer2.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #514bca;\n"
            "border-radius: 50px;\n"
            "color: white"
        )
        self.answer2.setObjectName("answer2")
        self.answer_btn_layout.addWidget(self.answer2)
        self.answer3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer3.sizePolicy().hasHeightForWidth())
        self.answer3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.answer3.setFont(font)
        self.answer3.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #514bca;\n"
            "border-radius: 50px;\n"
            "color: white;"
        )
        self.answer3.setObjectName("answer3")
        self.answer_btn_layout.addWidget(self.answer3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.quizzwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 80, 1121, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.question_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.question_layout.setContentsMargins(0, 0, 0, 0)
        self.question_layout.setObjectName("question_layout")
        self.question = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.question.setFont(font)
        self.question.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #514bca;\n"
            "padding-left: 20px;\n"
            "border-radius: 50px;\n"
            "color: white"
        )
        self.question.setText("")
        self.question.setObjectName("question")
        self.question_layout.addWidget(self.question)
        self.quizz_id = QtWidgets.QLabel(self.quizzwidget)
        self.quizz_id.setGeometry(QtCore.QRect(580, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quizz_id.setFont(font)
        self.quizz_id.setStyleSheet("color: white;")
        self.quizz_id.setObjectName("quizz_id")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.quizzwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(79, 240, 1121, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.answer_labels_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.answer_labels_layout.setContentsMargins(0, 0, 0, 0)
        self.answer_labels_layout.setObjectName("answer_labels_layout")
        self.answer_label1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_label1.setFont(font)
        self.answer_label1.setStyleSheet("color: white")
        self.answer_label1.setObjectName("answer_label1")
        self.answer_labels_layout.addWidget(self.answer_label1)
        self.answer_label2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_label2.setFont(font)
        self.answer_label2.setStyleSheet("color: white")
        self.answer_label2.setObjectName("answer_label2")
        self.answer_labels_layout.addWidget(self.answer_label2)
        self.answer_label3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_label3.setFont(font)
        self.answer_label3.setStyleSheet("color: white")
        self.answer_label3.setObjectName("answer_label3")
        self.answer_labels_layout.addWidget(self.answer_label3)
        self.restart_btn = QtWidgets.QPushButton(self.quizzwidget)
        self.restart_btn.setGeometry(QtCore.QRect(990, 20, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart_btn.sizePolicy().hasHeightForWidth())
        self.restart_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restart_btn.setFont(font)
        self.restart_btn.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #ca4b4b;\n"
            "border-radius: 25px;\n"
            "color: white"
        )
        self.restart_btn.setObjectName("restart_btn")
        self.start_btn = QtWidgets.QPushButton(self.quizzwidget)
        self.start_btn.setGeometry(QtCore.QRect(480, 570, 341, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_btn.setFont(font)
        self.start_btn.setText("Testa başla")
        self.start_btn.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #514bca;\n"
            "border-radius: 50px;\n"
            "color: white"
        )
        self.start_btn.setObjectName("start_btn")

        self.false_legend = QtWidgets.QFrame(self.quizzwidget)
        self.false_legend.setGeometry(QtCore.QRect(300, 510, 20, 20))
        self.false_legend.setStyleSheet(
            "background-color: #cb3f3f;\n"
            "border: 1px solid white;\n"
            "border-radius: 10px;"
        )
        self.false_legend.setObjectName("false_legend")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.false_legend)
        self.verticalLayout.setObjectName("verticalLayout")
        self.true_legend = QtWidgets.QFrame(self.quizzwidget)
        self.true_legend.setGeometry(QtCore.QRect(300, 550, 20, 20))
        self.true_legend.setStyleSheet(
            "background-color: #1da241;\n"
            "border: 1px solid white;\n"
            "border-radius: 10px;"
        )
        self.true_legend.setObjectName("true_legend")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.true_legend)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.false_legend_label = QtWidgets.QLabel(self.quizzwidget)
        self.false_legend_label.setGeometry(QtCore.QRect(340, 500, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.false_legend_label.setFont(font)
        self.false_legend_label.setStyleSheet("color: white;")
        self.false_legend_label.setObjectName("false_legend_label")
        self.true_legend_label = QtWidgets.QLabel(self.quizzwidget)
        self.true_legend_label.setGeometry(QtCore.QRect(340, 540, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.true_legend_label.setFont(font)
        self.true_legend_label.setStyleSheet("color: white;")
        self.true_legend_label.setObjectName("true_legend_label")
        self.results_layout = QtWidgets.QWidget(self.quizzwidget)
        self.results_layout.setGeometry(QtCore.QRect(660, 240, 341, 331))
        self.results_layout.setStyleSheet(
            "QLabel {\n" "    padding: 10px;\n" "    color: white;\n" "}"
        )
        self.results_layout.setObjectName("results_layout")
        self.result_widget = QtWidgets.QVBoxLayout(self.results_layout)
        self.result_widget.setContentsMargins(0, 0, 0, 0)
        self.result_widget.setObjectName("result_widget")
        self.false_answer_count = QtWidgets.QLabel(self.results_layout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.false_answer_count.setFont(font)
        self.false_answer_count.setObjectName("false_answer_count")
        self.result_widget.addWidget(self.false_answer_count)
        self.true_answer_count = QtWidgets.QLabel(self.results_layout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.true_answer_count.setFont(font)
        self.true_answer_count.setObjectName("true_answer_count")
        self.result_widget.addWidget(self.true_answer_count)
        self.percent = QtWidgets.QLabel(self.results_layout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.result_widget.addWidget(self.percent)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.quizzwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 70, 421, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chart_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setObjectName("chart_layout")
        self.chart = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.chart.setObjectName("chart")
        self.chart_layout.addWidget(self.chart)
        QuizzWindow.setCentralWidget(self.quizzwidget)

        self.start_btn.clicked.connect(self.start_test)
        self.restart_btn.clicked.connect(self.restart_test)
        self.answer1.clicked.connect(self.tap_a)
        self.answer2.clicked.connect(self.tap_b)
        self.answer3.clicked.connect(self.tap_c)
        self.next_btn.clicked.connect(self.next_question)

        self.retranslateUi(QuizzWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizzWindow)

        self.toggle_quizz_display(False)
        self.toggle_results(False)

        self.true_style = "background-color: #48475d; border: 2px solid #4bca64; border-radius: 50px; color: white"
        self.false_style = "background-color: #48475d; border: 2px solid #ca4b4b; border-radius: 50px; color: white"
        self.default_style = "background-color: #48475d; border: 2px solid #514bca; border-radius: 50px; color: white;"

        self.true_answers = 0

        self.quizz_data = {
            "questions": [
                {
                    "question": "Okatmagyň we bilim bermegiň nazaryýeti haýsy sözde jemlenýär?",
                    "variants": ("Metodika", "Pedagogika", "Dioletika"),
                    "true": "3",
                },
                {
                    "question": "Androgogika nähili pedagogikadyr?",
                    "variants": (
                        "Mekdebe çenli ýaşly çagalaryň pedogogikasy",
                        "Uly ýaşly adamlaryň pedagogikasy",
                        "Ýokary okuw jaýlarynyň pedagogikasy",
                    ),
                    "true": "2",
                },
                {
                    "question": "Jenaýat endikleri üçin azatlykdan mahrum edilen adamlaryň saklanýan,\nolary gaýtadan terbiýelemek bilen meşgullanýan pedagogika haýsy?",
                    "variants": (
                        "Düzediş-zähmet pedagogikasy",
                        "Konfessional pedagogika",
                        "Sosial pedagogika",
                    ),
                    "true": "1",
                },
                {
                    "question": "Pedagogikanyň metodologiýasy haýsy wezipeleri(funksiýalary) ýerine ýetirýär?",
                    "variants": (
                        "Tankydy, akyl ýetirmek, refleksiýa",
                        "Tankydy terbiýe okatmak",
                        "Refleksiýa, akyl ýetirmek, bilim-terbiýe",
                    ),
                    "true": "1",
                },
                {
                    "question": "Bilim maksatnamasy haýsy ugurlara bölünýär?",
                    "variants": (
                        "Umumy bilim, hünär bilim",
                        "Umumy bilim, ýokary bilim",
                        "Umumy orta bilim, ýokary bilim",
                    ),
                    "true": "1",
                },
                {
                    "question": 'Ýokary hünär bilimi hakyndaky ähli maksatlary Türkmenistanyň "Bilim"\nhakynda kanunyň rejelenen görnüşiniň haýsy maddasynda berilendir?',
                    "variants": (
                        "24-nji madda",
                        "28-nji madda",
                        "55-nji madda",
                    ),
                    "true": "2",
                },
                {
                    "question": "Indiwid kim?",
                    "variants": (
                        "Özbaşdak pikirlenip bilýän sosiallaşan adamlar we akyl taýdan yza galanlar",
                        "Şahsyýet we 18 ýaşa çenli çagalar",
                        "Köpüň biri, 18 ýaşa çenli çagalar we akyl taýdan yza galanlar",
                    ),
                    "true": "3",
                },
                {
                    "question": "Adaptasiýa näme?",
                    "variants": (
                        "Duýgurlyk",
                        "Uýgunlaşmak",
                        "Öwrenişmek",
                    ),
                    "true": "2",
                },
                {
                    "question": "Şahsyýetiň kemala gelmegine täsir edýän faktorlar haýsylar?",
                    "variants": (
                        "Terbiýe, nesle geçirijilik, sosial sreda",
                        "Terbiýe, bilim, akyl-paýhas",
                        "Terbiýe, biologik we fiziologik aýratynlyklary",
                    ),
                    "true": "1",
                },
                {
                    "question": "Şahsyýetiň kemala gelmegine täsir edýän formal däl subýektler haýsylar?",
                    "variants": (
                        "Gurnaklar, tanyşlar, erkin gatnaşyklar, sungat we medeniýet edebiýat",
                        "Sosial gatlaklar, alymlar, bilim ulgamy",
                        "Garyndaşlar, ene-atalar, ýokary bilimli adamlar",
                    ),
                    "true": "1",
                },
                {
                    "question": "Prental ösüş näme?",
                    "variants": (
                        "Irki bäbeklik döwri",
                        "Enäniň göwsündäki ösüş döwri",
                        "Uly mekdep ýaşly çagalar",
                    ),
                    "true": "2",
                },
                {
                    "question": "Şahsyýetiň esasan üç sany faktoryň nesle geçirijiliginiň sosial sredanyň\ntälim terbiýäniň täsiri bilen kemala gelýändigini subut edýän alym kim?",
                    "variants": (
                        "Aristotel",
                        "Platon",
                        "L.P.Pawlow",
                    ),
                    "true": "3",
                },
                {
                    "question": "Aksellerasiýa näme?",
                    "variants": (
                        "Adamyň beden ösüşiniň tizlenmegi",
                        "Adamyň akyl taýdan ösüşiniň tizlenmegi",
                        "Adamyň daş-töweregi bagly ösüşiniň tizlenmegi",
                    ),
                    "true": "1",
                },
                {
                    "question": '"Terbiýe - bu çagalaryň ululara aňsyz öýkenmesidir?" diýip haýsy alym belläpdir?',
                    "variants": (
                        "Monro",
                        "A.Diskweg",
                        "L.Tolstoý",
                    ),
                    "true": "1",
                },
                {
                    "question": "Adamyň emosional lezzet alyş duýgysyny nähili terbiýe kämilleşdirýär?",
                    "variants": (
                        "Ahlak terbiýesi",
                        "Gözellik terbiýesi",
                        "Zähmet terbiýesi",
                    ),
                    "true": "2",
                },
                {
                    "question": '"Beýik didaktika" kimiň işi?',
                    "variants": (
                        "W.Ratke",
                        "Ýa.A.Komenskiý",
                        "A.S.Makarenko",
                    ),
                    "true": "2",
                },
                {
                    "question": "Çaganyň kiçi mekdep ýaşly döwri näçe ýaşdan näçe ýaşa çenli?",
                    "variants": (
                        "7 ýaşdan 12 ýaşa çenli",
                        "6 ýaşdan 11 ýaşa çenli",
                        "8 ýaşdan 11 ýaşa çenli",
                    ),
                    "true": "2",
                },
                {
                    "question": "Okatmagyň funksiýalary haýsylar?",
                    "variants": (
                        "Okatmak, jemgyýetde goşmak, sosiallaşdyrmak",
                        "Okatmak, terbiýe bermek ösdürmek",
                        "Okatmak, şahsyýet edip ýetişdirmek",
                    ),
                    "true": "2",
                },
                {
                    "question": "Okatmak işi näme?",
                    "variants": (
                        "Bilim, ylym bermek",
                        "Dersler bilen tanyşdyrmak",
                        "Mugallym bilen okuwçynyň aragatnaşygy",
                    ),
                    "true": "3",
                },
                {
                    "question": "Indiwid diýen düşünje nämäni aňladýar?",
                    "variants": (
                        "Häzirki zaman ösen adamzat jemgyýetini emele getiren umumylyklygyny aňladýar",
                        "Özüňe derňemäge, özüňi bahalamaga, özüňe gözegçilik etmäge ukybyň bolmagy",
                        "Kimdir biriniň gözegçiligine mätäç adamlar",
                    ),
                    "true": "3",
                },
                # continue
                {
                    "question": "Türkmenistanyň Magtymguly adyndaky Ýaşlar guramasy haçan döredildi?",
                    "variants": (
                        "1994-nji ýylyň 15-nji oktýabry",
                        "1994-nji ýylyň 15-nji noýabry",
                        "1991-nji ýylyň 16-njy noýabry",
                    ),
                    "true": "1",
                },
                {
                    "question": "Iholastika diýmek näme?",
                    "variants": (
                        "Alym-mekdep",
                        "Dini mekdep",
                        "Ýokary okuw",
                    ),
                    "true": "1",
                },
                {
                    "question": '"Bilim hakynda" Türkmenistanyň kanunynyň rejelenen görnüşi\nnäçe maddadan durýar?',
                    "variants": (
                        "60",
                        "12",
                        "62",
                    ),
                    "true": "1",
                },
                {
                    "question": "Diskusiýa görnüşi okatmagyň haýsy usulyna degişli?",
                    "variants": (
                        "Amaly usuly",
                        "Görkezme usuly",
                        "Söz üsti usuly",
                    ),
                    "true": "1",
                },
                {
                    "question": "Pedagogiki garaýyşlarwe pikirler ýazuwyň döremeginden öň nämelerde\nýüze çykypdyr?",
                    "variants": (
                        "Aýdymlarda, yrymlarda, ýadygärliklerde",
                        "Nakyllarda, yrymlarda, meklerde",
                        "Mukaddes kitaplarda, rowaýatlarda, däp=dessurlarda, yrymlarda",
                    ),
                    "true": "1",
                },
                {
                    "question": "Çaganyň ösüşinde ýaş aýratynlyklaryna bölmekde psihologik ösüş\nhaýsy ýagdaýlary öz içine alýar?",
                    "variants": (
                        "Ünsüň, pikirlenmäniň we sözleýşiň, temperamentiň we gylyk-häsiýetiň\n    aýratynlyklary degişlidir",
                        "Gan-aýlanyş, içki mäzleriň, nerw sistemasynyň we ş.m. degişlidir",
                        "Hyýala getirmeleriň, syýasy, ahlak garaýyşlarynyň nerw sistemasyny\n    we ş.m degişlidir",
                    ),
                    "true": "1",
                },
                {
                    "question": "Pedagog sözi ilkibaşda nähili düşünjede ulanylypdyr?",
                    "variants": (
                        "Gadymy Gresiýada öz eýesiniň çagasynyň mekdebe äkidip getirýän\n    gula ýüzlenipdirler",
                        "Afiny mekdeplerinde bilim berýän mugallymlara ýüzlenipdirler",
                        "Halypa",
                    ),
                    "true": "1",
                },
                {
                    "question": "Bilim bermekde dürli dersleri bilen baglanyşykda öwrenmekligi haýsy\nGündogar akyldary maslahat beripdir?",
                    "variants": (
                        "Al Horezmi",
                        "Al Faraby",
                        "Al Biruny",
                    ),
                    "true": "1",
                },
                {
                    "question": "Didaktika sözüni ilkinji gezek ylmy dolanyşyga girizen alym kim?",
                    "variants": (
                        "Frensis Bekon",
                        "Aristotel",
                        "Ýan Amos Komenskiý",
                    ),
                    "true": "1",
                },
                {
                    "question": "Bilimleri, başarnyklary, endikleri özleşdirmek hem-de emele getirmek\nmaksady bilen ýörite gurnalýan mugallymlaryň we okuwçylaryň aragatnaşygyna\nnäme diýilýär?",
                    "variants": (
                        "Okatmak",
                        "Sosiallaşmak",
                        "Terbiýelemek",
                    ),
                    "true": "1",
                },
                {
                    "question": "Belli bir endigi, bilimi, başarnygy ýa-da okuw öwretmek we özleşdirmek\nüçin ýörite gurnalýan sapaklaryň gidişine näme diýilýär?",
                    "variants": (
                        "Guramaçylyk",
                        "Okuw prosesi",
                        "Pedagogik iş",
                    ),
                    "true": "1",
                },
                {
                    "question": "Okatmagyň maksadyna we wezipelerine näme diýilýär?",
                    "variants": (
                        "Forma",
                        "Metod",
                        "Serişde",
                    ),
                    "true": "1",
                },
                {
                    "question": "Okatmak döwrüniň kanunalaýyklygy netijesinde okuwçylara häzirki döwrüň\ntalabyna laýyk bilim we terbiýe kanun maksady bilen ulanylýan esasy\nbaş düzgünlere näme diýilýär?",
                    "variants": (
                        "Bilim bermek",
                        "Okatmagyň esaslary",
                        "Okatmagyň düzgünleri",
                    ),
                    "true": "1",
                },{
                    "question": "Mugallymyň okuwçylara maglumatlary bermek, terbiýelemek, aňlaatmak we\ndurmuşda ulanmagyň maksadyny düşündirmek boýunça tertiplenen işe näme\ndiýilýär?",
                    "variants": (
                        "Okatmak",
                        "Okamak",
                        "Didaktika",
                    ),
                    "true": "1",
                },
            ]
        }

    def refresh_next_btn(self, inner_text: str, func_for_connection):
        self.next_btn = QtWidgets.QPushButton(self.quizzwidget)
        self.next_btn.setGeometry(QtCore.QRect(790, 20, 190, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet(
            "background-color: #48475d;\n"
            "border: 2px solid #4bca64;\n"
            "border-radius: 25px;\n"
            "color: white"
        )

        self.next_btn.setObjectName("next_btn")
        self.next_btn.setText(inner_text)
        self.next_btn.clicked.connect(func_for_connection)

    def toggle_results(self, on: bool) -> None:
        if on:
            self.false_legend.setVisible(True)
            self.false_legend_label.setVisible(True)
            self.true_legend.setVisible(True)
            self.true_legend_label.setVisible(True)
            self.results_layout.setVisible(True)
            self.false_answer_count.setVisible(True)
            self.true_answer_count.setVisible(True)
            self.percent.setVisible(True)
            self.verticalLayoutWidget.setVisible(True)

        else:
            self.false_legend.setVisible(False)
            self.false_legend_label.setVisible(False)
            self.true_legend.setVisible(False)
            self.true_legend_label.setVisible(False)
            self.results_layout.setVisible(False)
            self.false_answer_count.setVisible(False)
            self.true_answer_count.setVisible(False)
            self.percent.setVisible(False)
            self.verticalLayoutWidget.setVisible(False)

    def finish_quizz(self):
        self.toggle_quizz_display(False)
        self.toggle_results(True)
        self.false_legend_label.setText("-  Ýalňyş")
        self.true_legend_label.setText("-  Dogry")
    
        false_answers = len(self.quizz_data["questions"]) + - self.true_answers
        data = [false_answers, self.true_answers]
        plt.pie(data, startangle=90, colors=["#cb3f3f", "#1da241"])
        plt.savefig("chart.png", transparent=True)
        pixmap = QtGui.QPixmap("chart.png").scaled(421, 421, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.chart.setPixmap(pixmap)

        self.false_answer_count.setText(f"Dogry jogaplar: {self.true_answers}")
        self.true_answer_count.setText(f"Ýalňyş jogaplar: {false_answers}")
        self.percent.setText(f"Ýetişik: {(self.true_answers / len(self.quizz_data["questions"])) * 100}%")

    def next_question(self):
        self.id += 1
        self.quizz_id.setText(f"Sorag №{self.id + 1}")
        self.question.setText(self.quizz_data["questions"][self.id]["question"])
        self.answer_label1.setText(
            "a) " + self.quizz_data["questions"][self.id]["variants"][0]
        )
        self.answer_label2.setText(
            "b) " + self.quizz_data["questions"][self.id]["variants"][1]
        )
        self.answer_label3.setText(
            "ç) " + self.quizz_data["questions"][self.id]["variants"][2]
        )
        self.next_btn.setVisible(False)

        self.set_btns_border_color(status="refresh")

        if self.id == len(self.quizz_data["questions"]) - 1:
            self.refresh_next_btn("Netijeleri görmek", self.finish_quizz)

    def set_btns_border_color(self, status=None):
        if status == "refresh":
            self.answer1.setStyleSheet(self.default_style)
            self.answer2.setStyleSheet(self.default_style)
            self.answer3.setStyleSheet(self.default_style)
        else:
            (
                self.answer1.setStyleSheet(self.true_style)
                if self.quizz_data["questions"][self.id]["true"] == "1"
                else self.answer1.setStyleSheet(self.false_style)
            )
            (
                self.answer2.setStyleSheet(self.true_style)
                if self.quizz_data["questions"][self.id]["true"] == "2"
                else self.answer2.setStyleSheet(self.false_style)
            )
            (
                self.answer3.setStyleSheet(self.true_style)
                if self.quizz_data["questions"][self.id]["true"] == "3"
                else self.answer3.setStyleSheet(self.false_style)
            )

    def tap_a(self):
        self.next_btn.setVisible(True)
        self.set_btns_border_color()

        if self.quizz_data["questions"][self.id]["true"] == "1":
            self.true_answers += 1

    def tap_b(self):
        self.next_btn.setVisible(True)
        self.set_btns_border_color()

        if self.quizz_data["questions"][self.id]["true"] == "2":
            self.true_answers += 1

    def tap_c(self):
        self.next_btn.setVisible(True)
        self.set_btns_border_color()

        if self.quizz_data["questions"][self.id]["true"] == "3":
            self.true_answers += 1

    def restart_test(self):
        self.toggle_quizz_display(False)
        self.start_btn.setVisible(True)
        self.true_answers = 0
        self.set_btns_border_color(status="refresh")
        self.toggle_results(False)

    def start_test(self):
        self.toggle_quizz_display(True)
        self.start_btn.setVisible(False)
        self.id = 0
        self.quizz_id.setText(f"Sorag №{self.id + 1}")
        self.question.setText(self.quizz_data["questions"][self.id]["question"])
        self.answer_label1.setText(
            "a) " + self.quizz_data["questions"][self.id]["variants"][0]
        )
        self.answer_label2.setText(
            "b) " + self.quizz_data["questions"][self.id]["variants"][1]
        )
        self.answer_label3.setText(
            "ç) " + self.quizz_data["questions"][self.id]["variants"][2]
        )

    def toggle_quizz_display(self, on: bool) -> None:
        if on:
            self.answer_label1.setVisible(True)
            self.answer_label2.setVisible(True)
            self.answer_label3.setVisible(True)
            self.answer1.setVisible(True)
            self.answer2.setVisible(True)
            self.answer3.setVisible(True)
            self.restart_btn.setVisible(True)
            self.question.setVisible(True)
            self.quizz_id.setVisible(True)
        else:
            self.answer_label1.setVisible(False)
            self.answer_label2.setVisible(False)
            self.answer_label3.setVisible(False)
            self.answer1.setVisible(False)
            self.answer2.setVisible(False)
            self.answer3.setVisible(False)
            self.restart_btn.setVisible(False)
            self.question.setVisible(False)
            self.quizz_id.setVisible(False)
            self.next_btn.setVisible(False)

    def retranslateUi(self, QuizzWindow):
        _translate = QtCore.QCoreApplication.translate
        QuizzWindow.setWindowTitle(_translate("QuizzWindow", "MainWindow"))
        self.answer1.setText(_translate("QuizzWindow", "a"))
        self.answer2.setText(_translate("QuizzWindow", "b"))
        self.answer3.setText(_translate("QuizzWindow", "ç"))
        self.quizz_id.setText(_translate("QuizzWindow", "Sorag №"))
        self.answer_label1.setText(_translate("QuizzWindow", "a)"))
        self.answer_label2.setText(_translate("QuizzWindow", "b)"))
        self.answer_label3.setText(_translate("QuizzWindow", "ç)"))
        self.restart_btn.setText(_translate("QuizzWindow", "Täzeden başlat"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QuizzWindow = QtWidgets.QMainWindow()
    ui = Ui_QuizzWindow()
    ui.setupUi(QuizzWindow)
    QuizzWindow.show()
    sys.exit(app.exec_())
