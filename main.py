from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)

app = QApplication([]) #menyimpan Qapp

window = QWidget() #menympan Qwidget
window.setWindowTitle('Memory card') #judul

#buton jwb
btn_ok = QPushButton('Answer') #tombl jwb

#label question
lb_question = QLabel('----------------------')
Radiogroubbox = QGroupBox("Answer option") #masukan jwbn
radiobtn = QRadioButton('----------------------')

#bikin3buah button
layout_ans1 = QHBoxLayout
layout_ans2 = QHBoxLayout # the vertical will be inside horizontal
layout_ans3 = QHBoxLayout

#tw0answer in first collumn
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

#twoanswer inthe secc collumn
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

#susun pertanyaan
layout_lines1 = QHBoxLayout() #pertyanyaan
layout_lines2 = QHBoxLayout() #pilihan jwb
layout_lines3 = QHBoxLayout() #tombol jwb

layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(Radiogroubbox)
layout_line3.addstrecth(1)
layout_line3.addwidget(btn_OK, Strecth = 2)
layout_line3.addstrecth(1)

layout_card = QVBoxLayout()

layout_card.addlayout(layout_line1, strecth = 2)
layout_card.addlayout(layout_line2, strecth = 8)
layout_card.addstrecth(1)
layout_card.addlayout(layout_line3, strecth = 1)
layout_card.addstrecth(1)
layout_card.setspacing(5) #spasi

window.setLayout(layout_card)




