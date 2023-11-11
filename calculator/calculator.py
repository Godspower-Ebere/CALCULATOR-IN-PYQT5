from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

    
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CALCULATOR GP VERSION")
        self.setWindowIcon(QIcon("calculator.png"))
        self.setMaximumHeight(50)
        layout=QVBoxLayout()
        layout2=QHBoxLayout()
        layout3=QHBoxLayout()
        layout4=QHBoxLayout()
        layout5=QHBoxLayout()
        layout6=QHBoxLayout()

        self.entry=QLineEdit()
        self.entry.setEnabled(False)
        self.entry.setFont(QFont("tahoma",50))
        
        one=QPushButton("1")
        one.setFont(QFont("Tahoma",25))
        one.clicked.connect(self.one)
        
        two=QPushButton("2")
        two.setFont(QFont("Tahoma",25))
        two.clicked.connect(self.two)
        
        three=QPushButton("3")
        three.setFont(QFont("Tahoma",25))
        three.clicked.connect(self.three)
        
        four=QPushButton("4")
        four.setFont(QFont("Tahoma",25))
        four.clicked.connect(self.four)

        
        five=QPushButton("5")
        five.setFont(QFont("Tahoma",25))
        five.clicked.connect(self.five)
        
        six=QPushButton("6")
        six.setFont(QFont("Tahoma",25))
        six.clicked.connect(self.six)
        
        seven=QPushButton("7")
        seven.setFont(QFont("Tahoma",25))
        seven.clicked.connect(self.seven)
        
        eight=QPushButton("8")
        eight.setFont(QFont("Tahoma",25))
        eight.clicked.connect(self.eight)
        
        nine=QPushButton("9")
        nine.setFont(QFont("Tahoma",25))
        nine.clicked.connect(self.nine)
        
        zero=QPushButton("0")
        zero.setFont(QFont("Tahoma",25))
        zero.clicked.connect(self.zero)
        
        divide=QPushButton("/")
        divide.setFont(QFont("Tahoma",25))
        divide.clicked.connect(self.divide)
        
        times=QPushButton("X")
        times.setFont(QFont("Tahoma",25))
        times.clicked.connect(self.times)
        
        min=QPushButton("-")
        min.setFont(QFont("Tahoma",25))
        min.clicked.connect(self.min)
        
        stop=QPushButton(".")
        stop.setFont(QFont("Tahoma",25))
        stop.clicked.connect(self.stop)
        
        plus=QPushButton("+")
        plus.setFont(QFont("Tahoma",25))
        plus.clicked.connect(self.plus)
        
        equal=QPushButton("=")
        equal.setFont(QFont("Tahoma",25))
        equal.clicked.connect(self.equal)

        clear=QPushButton("C")
        clear.setFont(QFont("Tahoma",25))
        clear.clicked.connect(self.clear)

        remove=QPushButton("c")
        remove.setFont(QFont("Tahoma",25))
        remove.clicked.connect(self.remove)
        
        layout2.addWidget(seven)
        layout2.addWidget(eight)
        layout2.addWidget(nine)
        layout2.addWidget(divide)
        
        layout3.addWidget(four)
        layout3.addWidget(five)
        layout3.addWidget(six)
        layout3.addWidget(times)
        
        layout4.addWidget(one)
        layout4.addWidget(two)
        layout4.addWidget(three)
        layout4.addWidget(min)

        layout5.addWidget(zero)
        layout5.addWidget(stop)
        layout5.addWidget(plus)
        layout5.addWidget(equal)

        layout6.addWidget(clear)
        layout6.addWidget(remove)

        
        layout.addWidget(self.entry)
        self.setLayout(layout)
        self.resize(400,400)
        min.setToolTip('This is a <br><b style="color:red;">Minus</b> Symbol')
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        layout.addLayout(layout5)
        layout.addLayout(layout6)
        self.show()
        
    def one(self):
        one=self.entry.text()
        one+="1"
        self.entry.setText(one)
    def two(self):
        two=self.entry.text()
        two+="2"
        self.entry.setText(two)
    def three(self):
        one=self.entry.text()
        one+="3"
        self.entry.setText(one)
    def four(self):
        four=self.entry.text()
        four+="4"
        self.entry.setText(four)
    def five(self):
        five=self.entry.text()
        five+="5"
        self.entry.setText(five)
    def six(self):
        six=self.entry.text()
        six+="6"
        self.entry.setText(six)
    def seven(self):
        seven=self.entry.text()
        seven+="7"
        self.entry.setText(seven)
    def eight(self):
        eight=self.entry.text()
        eight+="8"
        self.entry.setText(eight)
    def nine(self):
        nine=self.entry.text()
        nine+="9"
        self.entry.setText(nine)
    def zero(self):
        zero=self.entry.text()
        zero+="0"
        self.entry.setText(zero)
    def plus(self):
        plus=self.entry.text()
        plus+="+"
        self.entry.setText(plus)
    def divide(self):
        divide=self.entry.text()
        divide+="/"
        self.entry.setText(divide)
    def times(self):
        times=self.entry.text()
        times+="*"
        self.entry.setText(times)
    def stop(self):
        stop=self.entry.text()
        stop+="."
        self.entry.setText(stop)
    def min(self):
        min=self.entry.text()
        min+="-"
        self.entry.setText(min)
    def equal(self):
        e=self.entry.text()
        ans=eval(e)
        equal=str(ans)
        self.entry.setText(equal)
    def clear(self):
        equal=self.entry.text()
        equal=""
        self.entry.setText(equal)
    def remove(self):
        remove=self.entry.text()
        new=""
        if remove!="":
            get=remove[-1]
            new=remove.removesuffix(get)
        self.entry.setText(new)
app=QApplication([])
window=main()
app.exec_()


























