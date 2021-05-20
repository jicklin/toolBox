import os, sys
from multiprocessing.pool import ThreadPool

from win32com.client import Dispatch, constants, gencache, DispatchEx
import logging

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='office_2_pdf.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


class PDFConverter:
    def __init__(self, pathname, postfix, outpath=None, export='.'):
        self._handle_postfix = postfix  # ['xls', 'xlsx']
        self._filename_list = list()
        if outpath is None or len(outpath) == 0:
            self._export_folder = os.path.join(os.path.abspath('.'), 'pdfconver')
        else:
            self._export_folder = outpath

        if not os.path.exists(self._export_folder):
            os.mkdir(self._export_folder)
        self._enumerate_filename(pathname)

    @property
    def filename_list(self):
        return self._filename_list

    def _enumerate_filename(self, pathname):
        '''
        读取所有文件名
        '''
        full_pathname = os.path.abspath(pathname)
        if os.path.isfile(full_pathname):
            if self._is_legal_postfix(full_pathname):
                self._filename_list.append(full_pathname)
            # else:
            #     raise TypeError('文件 {} 后缀名不合法！仅支持如下文件类型：{}。'.format(pathname, '、'.join(self._handle_postfix)))
        elif os.path.isdir(full_pathname):
            for relpath, _, files in os.walk(full_pathname):
                for name in files:
                    filename = os.path.join(full_pathname, relpath, name)
                    if self._is_legal_postfix(filename):
                        self._filename_list.append(os.path.join(filename))
        # else:
        # raise TypeError('文件/文件夹 {} 不存在或不合法！'.format(pathname))

    def _is_legal_postfix(self, filename):
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith(
            '~')

    def run_excel_conver(self):
        '''
        进行批量处理，根据后缀名调用函数执行转换
        '''
        if len(self._filename_list) == 0:
            raise BaseException('没有符合条件的文件')
        logging.info('需要转换的文件数：%s', len(self._filename_list))
        pool = ThreadPool(4)
        pool.map(self.xls, self._filename_list)
        pool.close()
        pool.join()
        logging.info('转换完成！')

    def run_word_conver(self):
        '''
        进行批量处理，根据后缀名调用函数执行转换
        '''
        if len(self._filename_list) == 0:
            raise BaseException('没有符合条件的文件')
        logging.info('需要转换的文件数：%s', len(self._filename_list))
        pool = ThreadPool(4)
        pool.map(self.doc, self._filename_list)
        pool.close()
        pool.join()
        logging.info('转换完成！')

    def run_ppt_conver(self):
        '''
        进行批量处理，根据后缀名调用函数执行转换
        '''
        if len(self._filename_list) == 0:
            raise BaseException('没有符合条件的文件')
        logging.info('需要转换的文件数：%s', len(self._filename_list))
        pool = ThreadPool(4)
        pool.map(self.ppt, self._filename_list)
        pool.close()
        pool.join()
        logging.info('转换完成！')

    def doc(self, filename):
        '''
        doc 和 docx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        logging.info('保存 PDF 文件：%s', exportfile)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        w = Dispatch("Word.Application")
        doc = w.Documents.Open(filename)
        doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)

        w.Quit(constants.wdDoNotSaveChanges)

    def docx(self, filename):
        self.doc(filename)

    def xls(self, filename):
        '''
        xls 和 xlsx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = DispatchEx("Excel.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        logging.info('保存 PDF 文件：%s', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename)

    def ppt(self, filename):
        '''
        ppt 和 pptx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        p = Dispatch("PowerPoint.Application")
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixedFormat(exportfile, 2, PrintRange=None)
        logging.info('保存 PDF 文件：%s', exportfile)
        p.Quit()

    def pptx(self, filename):
        self.ppt(filename)
