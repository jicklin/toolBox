import json
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QProgressBar
from MainWindow import Ui_MainWindow
from PdfMenu import Ui_PdfMenu
from diffAssign import Ui_diffAssignForm
from PdfMergeTool import PdfMergeTool
from Office2Pdf import Ui_officeToPdfForm
from excel2pdf import PDFConverter
from DiffAssignTool import DiffAssignTool
from PyQt5.QtCore import *
from LaodingMessage import LoadingPop


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.pdfItem = PdfMenu()
        self.officeItem = Office2PDF()
        self.diffAssign = DiffAssign()

        self.fileOpenAction.triggered.connect(self.openMsg)
        self.appCloseAction.triggered.connect(self.close)
        self.pdfProcessAction.triggered.connect(self.openPdfMenu)
        self.office2PdfAction.triggered.connect(self.openOfficeMenu)
        self.diffAssignaction.triggered.connect(self.openDiffAssignMenu)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files(*.txt)")
        self.statusbar.showMessage(file)

    def openPdfMenu(self):
        self.closeOther()
        self.Maingridlayout.addWidget(self.pdfItem)
        self.pdfItem.show()

    def openOfficeMenu(self):
        self.closeOther()
        self.Maingridlayout.addWidget(self.officeItem)
        self.officeItem.show()

    def openDiffAssignMenu(self):
        self.closeOther()
        self.Maingridlayout.addWidget(self.diffAssign)
        self.diffAssign.show()

    def closeOther(self):
        """
        删除其他的渲染的敞口
        :return:
        """
        show_num = self.Maingridlayout.count()
        print(show_num)
        if show_num != 0:
            for i in range(show_num):
                self.Maingridlayout.itemAt(i).widget().close()


class PdfMenu(QWidget, Ui_PdfMenu):
    def __init__(self):
        super(PdfMenu, self).__init__()
        self.setupUi(self)
        self.mergePdfBtn.clicked.connect(self.merge_pdf)
        self.mergedistUnitNoBtn.clicked.connect(self.merge_unit_pdf)

    def merge_pdf(self):
        targetPath = QFileDialog.getExistingDirectory(self, "选择合并的文件夹", "./")
        if len(targetPath) == 0:
            QMessageBox.warning(self, "提示", "必须选择需要合并的文件夹。", QMessageBox.Yes | QMessageBox.No)
            return

        outPath = QFileDialog.getExistingDirectory(self, "请选择合并后的文件位置", "./")
        if len(outPath) == 0:
            QMessageBox.warning(self, "提示", "请选择合并后的文件位置。", QMessageBox.Yes | QMessageBox.No)
            return

        pdf_merge_tool = PdfMergeTool(targetPath, outPath)
        try:
            filepath = pdf_merge_tool.merge_pdf()
            QMessageBox.information(self, "提示",
                                    '恭喜马佳佳同学合并成功,输出的文件位于:' + filepath,
                                    QMessageBox.Yes | QMessageBox.No)
        except BaseException as e:
            QMessageBox.warning(self, "失败", "处理失败。" + e, QMessageBox.Yes | QMessageBox.No)
            return

    def merge_unit_pdf(self):
        targetPath = QFileDialog.getExistingDirectory(self, "选择合并的文件夹", "./")
        if len(targetPath) == 0:
            QMessageBox.warning(self, "提示", "必须选择需要合并的文件夹。", QMessageBox.Yes | QMessageBox.No)
            return

        outPath = QFileDialog.getExistingDirectory(self, "请选择合并后的文件位置", "./")
        if len(outPath) == 0:
            QMessageBox.warning(self, "提示", "请选择合并后的文件位置。", QMessageBox.Yes | QMessageBox.No)
            return

        pdf_merge_tool = PdfMergeTool(targetPath, outPath)
        try:
            count, error_list = pdf_merge_tool.merge_unit_pdf()
            QMessageBox.information(self, "提示",
                                    '恭喜马佳佳同学合并成功，共成功合并{}个单元,失败的单元如下：{}'.format(count, json.dumps(error_list)),
                                    QMessageBox.Yes | QMessageBox.No)


        except BaseException as e:
            QMessageBox.warning(self, "失败", "处理失败。" + str(e), QMessageBox.Yes | QMessageBox.No)
            return


class Office2PDF(QWidget, Ui_officeToPdfForm):
    def __init__(self):
        super(Office2PDF, self).__init__()
        self.setupUi(self)
        self.excel2PdfBtn.clicked.connect(self.excel_to_pdf)
        self.word2PdfBtn.clicked.connect(self.word_to_pdf)
        self.ppt2PdfBtn.clicked.connect(self.ppt_to_pdf)

    def open_bar(self, num):
        self.bar = QProgressBar(self)
        self.bar.maximum(num)

    def excel_to_pdf(self):
        targetPath = QFileDialog.getExistingDirectory(self, "选择合并的文件夹", "./")
        if len(targetPath) == 0:
            QMessageBox.warning(self, "提示", "必须选择需要合并的文件夹。", QMessageBox.Yes | QMessageBox.No)
            return

        outPath = QFileDialog.getExistingDirectory(self, "请选择合并后的文件位置", "./")
        converter = PDFConverter(pathname=targetPath, postfix=['xls', 'xlsx'], outpath=outPath)
        try:
            file_list = converter.filename_list
            converter.run_excel_conver()
            QMessageBox.information(self, "提示",
                                    '恭喜马佳佳同学处理成功 ^_^',
                                    QMessageBox.Yes | QMessageBox.No)
        except BaseException as e:
            QMessageBox.warning(self, "失败", "处理失败。" + str(e), QMessageBox.Yes | QMessageBox.No)

    def word_to_pdf(self):
        targetPath = QFileDialog.getExistingDirectory(self, "选择合并的文件夹", "./")
        if len(targetPath) == 0:
            QMessageBox.warning(self, "提示", "必须选择需要合并的文件夹。", QMessageBox.Yes | QMessageBox.No)
            return

        outPath = QFileDialog.getExistingDirectory(self, "请选择合并后的文件位置,不选择的话默认程序执行下的pdfconver文件中", "./")
        converter = PDFConverter(pathname=targetPath, postfix=['doc', 'docx'], outpath=outPath)
        try:
            converter.run_word_conver()
            QMessageBox.information(self, "提示",
                                    '恭喜马佳佳同学处理成功 ^_^',
                                    QMessageBox.Yes | QMessageBox.No)
        except BaseException as e:
            QMessageBox.warning(self, "失败", "处理失败。" + str(e), QMessageBox.Yes | QMessageBox.No)

    def ppt_to_pdf(self):
        targetPath = QFileDialog.getExistingDirectory(self, "选择合并的文件夹", "./")
        if len(targetPath) == 0:
            QMessageBox.warning(self, "提示", "必须选择需要合并的文件夹。", QMessageBox.Yes | QMessageBox.No)
            return

        outPath = QFileDialog.getExistingDirectory(self, "请选择合并后的文件位置,不选择的话默认程序执行下的pdfconver文件中", "./")
        converter = PDFConverter(pathname=targetPath, postfix=['ppt', 'pptx'], outpath=outPath)
        try:
            converter.run_ppt_conver()
            QMessageBox.information(self, "提示",
                                    '恭喜马佳佳同学处理成功 ^_^',
                                    QMessageBox.Yes | QMessageBox.No)
        except BaseException as e:
            QMessageBox.warning(self, "失败", "处理失败。" + str(e), QMessageBox.Yes | QMessageBox.No)


class DiffAssign(QWidget, Ui_diffAssignForm):
    def __init__(self):
        super(DiffAssign, self).__init__()
        self.loading = LoadingPop()
        self.setupUi(self)
        self.fileSelectorBtn.clicked.connect(self.selectProcessFile)
        self.fileOutPathBtn.clicked.connect(self.selectOutPath)
        self.pushButton.clicked.connect(self.process)

    def selectProcessFile(self):
        file, ok = QFileDialog.getOpenFileName(self, "选择需要处理的excel文件", "./", 'EXCEL文件(*.xls);EXCEL文件(*.xlsx)')
        self.fileShowInput.append(file)

    def selectOutPath(self):
        outPath = QFileDialog.getExistingDirectory(self, "不选择的话默认程序执行下的diff文件中", "./")
        self.outPathInput.setText(outPath)

    def showSuccess(self,message):
        self.loading.close()
        QMessageBox.information(self, "提示",
                                '恭喜马佳佳同学处理成功 ^_^',
                                QMessageBox.Yes | QMessageBox.No)

    def showError(self,message):
        self.loading.close()
        QMessageBox.warning(self, "失败", "处理失败啦。" + message, QMessageBox.Yes | QMessageBox.No)

    def process(self):

        inputFilePath = self.fileShowInput.toPlainText()
        outpath = self.outPathInput.toPlainText()
        num = self.groupNumInput.toPlainText()
        # tool = DiffAssignTool(inputFilePath, outpath, num)
        # tool.create_file()
        self.loading = LoadingPop()
        self.loading.show()
        self.thread_1 = Work(inputFilePath, outpath, num)
        self.thread_1.messageTxtValue.connect(self.loading.set_message)
        self.thread_1.showSuccess.connect(self.showSuccess)
        self.thread_1.showError.connect(self.showError)
        self.thread_1.start()





class Work(QThread):
    messageTxtValue = pyqtSignal(str)
    showSuccess = pyqtSignal(str)
    showError = pyqtSignal(str)

    def __init__(self, inputFilePath, outpath, num):
        super(Work, self).__init__()
        self.inputFilePath = inputFilePath
        self.outpath = outpath
        self.num = num

    def run(self):
        self.messageTxtValue.emit('开始读取excel文件')
        try:
            tool = DiffAssignTool(self.inputFilePath, self.outpath, self.num, self.messageTxtValue)
            tool.create_file()
            self.showSuccess.emit('成功啦')

        except BaseException as e:
            self.showError.emit(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
