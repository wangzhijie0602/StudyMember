import sys,io,json
from PIL import Image
from PyQt5.QtGui import QPixmap, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_untitled,member,time

def run_main():
    verify = ui.userText.toPlainText()
    ui.button.setEnabled(False)
    token = member.get_token(verify)
    tokenDict = json.loads(token.text)
    token = tokenDict['data'][0]['token']
    page = member.get_member(token,"1","regiment")['data']['last_page']
    nodone = 0
    name1 = ""
    name2 = ""
    for i in range(1,page + 1):
        userData = member.get_member(token,i,"/regiment")
        for j in userData['data']['data']:
            if j['isStudy'] == "否":
                nodone += 1
                name1 = name1 + j['realname'] + '\n'
    page = member.get_member(token,"1","/regiment/youngList")['data']['last_page']
    for i in range(1,page + 1):
        userData = member.get_member(token,i,"/regiment/youngList")
        for j in userData['data']['data']:
            if j['isStudy'] == "否":
                nodone += 1
                name2 = name2 + j['realname'] + '\n'
    ui.userText.setText("一共" + str(nodone) + "人当前未完成\n" +
                        "其中团员为：\n" + name1 + "\n" +
                        "非团员为：\n" + name2 + "\n" +
                        time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        )


def set_img_on_label(lb,img_b64):
    img_io = io.BytesIO(img_b64)
    img=Image.open(img_io)
    pix = img.toqpixmap()
    lb.setScaledContents(True)  # 自适应QLabel大小
    lb.setPixmap(pix)

def initimage():
    imagedata = member.get_image()
    print(imagedata)
    set_img_on_label(ui.imageLabel,imagedata)
    


def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    global ui
    ui = Ui_untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    initimage()
    ui.button.clicked.connect(run_main)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()