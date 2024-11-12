from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Siapa nama president pertama Indonesia?", "Mr. Soekarno", "Mr. Soeharto", "Mr. Habibie", "Gus Dur"))
question_list.append(Question("Bahasa yang digunakan di negara Philipine?", "Tagalog","Melayu","Hindi","Bangla"))
question_list.append(Question("Siapa Villain di drakor blind?", "inseong","sun hong","charless", "sung joon"))
question_list.append(Question("Tanggal berapa kah Indonesia merdeka?", "17 Agustus", "20 Desember", "19 January", "1 Mei"))
question_list.append(Question("12x5+129", "189","190","200","182"))
question_list.append(Question("Siapa presiden ke 5 Indonesia?", "Mrs. Megawati", "Mr. Jokowi", "Gus Dur", "Mr. Soekarno"))
question_list.append(Question("20x20-399", "1", "400", "799", "649"))
question_list.append(Question("Siapa wakil presiden Pertama Indonesia?", "Hatta", "Anies", "Gibran", "Megawati"))

app = QApplication([])

btn_OK = QPushButton('Answer')
lb_Question = QLabel('The most difficult question in the world!')

RadioGroupBox = QGroupBox("Answer options")
# Ada 4 Option
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
# Ada 4 Button
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# buat HboxLayout
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
# two answers in the first column
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
# two answers in the second column
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

# layout_ans1 panggil kedua kolom
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# setLayout menggunakan layout_ans1
RadioGroupBox.setLayout(layout_ans1)


# Bikin Test result
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel("Are you correct or not?")
lb_Correct = QLabel('The answer will be here!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop)) # posisi lb_Result di kiri atas
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2) # posisi lb_Correct di tengah
AnsGroupBox.setLayout(layout_res) # panggil layout_res karena dia menyimpan lb result dan correct

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

# tampilan layout_line 3
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2) # ukuran buttonnya akan lebih besar
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

# memberi spasi antar layout biar rapih
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spacing the content

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')


def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) # remove limits in order to reset radio button selection
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # bring back the limits so only one radio button can be selected 

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer) #ini adalah jawaban benar
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct("Correct!")
        window.score += 1
        print("Statitics\n-total Question:", window.total, "\n-right answer:", window.score)
        print("rating:", (window.score/window.total*100), "%")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct("Incorrect!")
            print("Rating:", (window.score/window.total*100), "%")

def next_question():
    window.total +=1
    print("Statics total question:", window.total, "\n-right answer:", window.score)
    ##inidigunakan untuk membuat pertanyaan yang ditampilkan akan hilang saat sudah di random
    cur_question = randint(0, len(question_list)-1) 
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == "Answer":
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')


btn_OK.clicked.connect(click_OK) # check that the answer panel appears when the button is pressed

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()








