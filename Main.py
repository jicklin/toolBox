import json
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox,QProgressBar
from MainWindow import Ui_MainWindow
from PdfMenu import Ui_PdfMenu
from PdfMergeTool import PdfMergeTool
from Office2Pdf import Ui_officeToPdfForm
from excel2pdf import PDFConverter


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.pdfItem = PdfMenu()
        self.officeItem = Office2PDF()

        self.fileOpenAction.triggered.connect(self.openMsg)
        self.appCloseAction.triggered.connect(self.close)
        self.pdfProcessAction.triggered.connect(self.openPdfMenu)
        self.office2PdfAction.triggered.connect(self.openOfficeMenu)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files(*.txt)")
        self.statusbar.showMessage(file)

    def openPdfMenu(self):
        self.Maingridlayout.addWidget(self.pdfItem)
        self.pdfItem.show()

    def openOfficeMenu(self):
        self.Maingridlayout.removeWidget()
        self.Maingridlayout.addWidget(self.officeItem)
        self.officeItem.show()


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

    def open_bar(self,num):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
