import logging
import os
import re
import codecs
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import json

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='merger_pdf.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


class PdfMergeTool:

    def __init__(self, targetPath, outPath, selectFiles=None):
        self.targetPath = targetPath
        self.outPath = outPath
        self.selectFiles = selectFiles

    def format_unit_pdf_list(self):
        """
        逻辑出所有含有不动产单元号的的pdf文件，并根据前19位不动产单元号分组
        :param root_dir_path:
        :return:
        """
        self.pdf_obj = {}
        for root, dirs, files in os.walk(self.targetPath):
            for file in files:
                file_full_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1]
                # 只要pdf格式的
                if file_ext == '.pdf' or file_ext == '.PDF':
                    """
                    把不动产单元号揪出来 并且只要前边的19位
                    """
                    macth_obj = re.search(r'[A-Z0-9]+', file)
                    unit_code = macth_obj.group()
                    code = unit_code[0:19]
                    if code not in self.pdf_obj:
                        file_list = [file_full_path]
                        self.pdf_obj[code] = file_list
                    else:
                        self.pdf_obj[code].append(file_full_path)

    def traverse_pdf(self):
        """
        找到文件夹下的pdf文件
        :return:
        """
        self.pdf_obj = []
        for root, dirs, files in os.walk(self.targetPath):
            for file in files:
                file_full_path = os.path.join(root, file)
                file_ext = file.split('.')[-1].lower()

                # 只要pdf格式的
                if file_ext == 'pdf' or file_ext == '.PDF':
                    self.pdf_obj.append(file_full_path)

    def merge_unit_pdf(self):
        """
        拼接pdf
        :param pdf_list:
        :param root_dir_path:
        :return:
        """

        count = 0
        error_list = []
        self.format_unit_pdf_list()
        pdf_list = self.pdf_obj
        for key in pdf_list.keys():
            try:
                merger = PdfFileMerger()
                logging.info('总共需要处理%s个单元数据，当前是第%s个', len(pdf_list), count + 1)

                logging.info('开始遍历单元数据%s->%s', key, json.dumps(pdf_list[key], ensure_ascii=False))

                for file_path in pdf_list[key]:

                    f = codecs.open(file_path, 'rb')
                    file_rd = PdfFileReader(f)
                    if file_rd.isEncrypted:
                        logging.warn('不支持加密后的文件: %s', file_path)
                        continue
                    merger.append(file_rd)
                    logging.info('开始合并文件：%s', file_path)
                    f.close()

                out_file_path = os.path.join(os.path.abspath(self.outPath), key + ".pdf")
                merger.write(out_file_path)
                logging.info('单元：%s 合并后输出文件：%s', key, out_file_path)

                merger.close()
                count = count + 1
            except BaseException as e:
                error_list.append(key)
                logging.error('尝试合并文件错误,单元为：%s', key, exc_info=True)
                pass
        logging.info('恭喜马佳佳同学合并成功，共成功合并%s个单元,失败的单元如下：%s', count, json.dumps(error_list))


        return count, error_list

    def merge_pdf(self):
        merger = PdfFileMerger()
        self.traverse_pdf()
        pdf_list = self.pdf_obj

        logging.info('开始遍历PDF数据%s', json.dumps(pdf_list, ensure_ascii=False))

        for file_path in pdf_list:

            f = codecs.open(file_path, 'rb')
            file_rd = PdfFileReader(f)
            if file_rd.isEncrypted:
                logging.warning('不支持加密后的文件: %s', file_path)
                continue
            merger.append(file_rd)
            logging.info('开始合并文件：%s', file_path)
            f.close()

        out_file_path = os.path.join(os.path.abspath(self.outPath), "合并后的文件.pdf")
        merger.write(out_file_path)
        logging.info('合并后输出文件：%s', out_file_path)
        merger.close()
        return out_file_path