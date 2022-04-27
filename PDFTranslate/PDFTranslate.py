"""
PDFTranslate

Copyright (c) 2020 3x-boy

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php
"""

import os
import pyPDF2
from googletrans import Translator


class Translator:
    """
    Translate the PDF content into the specified language 
    and output it to a file.
    
    Parameters
    ----------
        txt_name : str
            Enter str type
        file_path : str
            Enter str type
        input_lang : str
            Enter str type
        output_lang : str
            Enter str type
        start_del : str
            Enter str type
        end_del : str
            Enter str type
    """

    def __init__(self, file_path, input_lang="en", output_lang="ja"):
        """
        Write docstring in Numpy style

        Parameters
        ----------
        file_path : str
            Enter str type
        input_lang : str
            Enter str type, default "en"
        output_lang : str
            Enter str type, default "ja"
        """

        now = datetime.now()
        self.txt_name = "{}/{}_{0:%Y%m%d}.txt".format(os.path.dirname(file_path), input_file_name, now)
        self.file_path = file_path
        self.input_lang = input_lang
        self.output_lang = output_lang
        self.start_del = "Translated(src=en, dest=ja, text="
        self.end_del = ", pronunciation=None, extra_data=\"{'translat...\")"

    def pdf_trans(self,):
        """
        Write docstring in Numpy style

        Parameters
        ----------
        test_2 : str
            Enter str type

        Returns
        -------
        self.test_1 : str
            Enter str type
        """
        if not '.pdf' == self.file_path[-4:]:
            print("FirePathError : PDFファイルのパスを入力してください")
            return

        if not os.path.isfile(self.file_path):
            print("FirePathError : 正しいファイルパスを入力してください")
            return

        with open(self.file_path, mode='rb') as f:
            reader = PyPDF2.PdfFileReader(f)

            # PDFファイルのパスワードチェック
            print("\nファイルのチェック・・\n")

            # 翻訳不可能な場合
            if reader.isEncrypted:
                print("FileError：パスワード付きPDFファイルの為、翻訳不可")
                return
            
            # 翻訳可能な場合
            print("***翻訳可能なPDFファイルです***")

            # 翻訳の実行
            print("\n翻訳実行・・・\n")
            translator = Translator()
            for idx, i in enumerate(range(reader.numPages)):
                try:
                    if idx = 1:
                        print("\n\n{}\n".format(reader.getPage(i)))
                    page = reader.getPage(i)
                    en_text = page.extractText()
                    ja_text_page = translator.translate(en_text, src=self.input_lang, dest=self.output_lang)
                    translation_text += str(ja_text_page).replace(self.start_del, "").replace(self.end_del, "")
                except Exception as e:
                    print(e)

        # 翻訳後テキストへ書き込み
        with open(self.txt_name, mode='w', encoding='utf-8') as f:
            f.write(translation_text)
        
        print("\n******翻訳完了******\n")
        return