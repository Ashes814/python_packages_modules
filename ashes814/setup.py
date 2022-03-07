# from distutils.core import setup
from setuptools import setup


def readme_file():
    with open('README.rst', encoding='utf-8') as rf:
        return rf.read()


setup(name='ashes814', version='1.0.0',
      description='It is a really niubi package!',
      packages=['ashes814'], py_modules=['tool'], author='Ashes', url='https://github.com/Ashes814',
      author_email='1534661514@qq.com', long_description=readme_file(),
      license='MIT')
# long_description = '''this is a verbose lib bala,balabalabalabalabala'
#                    balabalabalabalabalabalabalabalabalabalabala
#                    balabalabalabalabalabalabalabalabalabalabalabalabala
#                    balabalabalabalabalabalabalabalabalabalabalabalabala
#                    Lorem  Lorem Lorem Lorem Lorem Lorem Lorem Lorem
#                     Lorem Lorem Lorem Lorem Lorem Lorem Lorem
#                      Lorem Lorem Lorem Lorem Lorem Lorem Lorem
#                       Lorem Lorem Lorem Lorem Lorem Lorem
#                        Lorem Lorem Lorem Lorem Lorem Lorem
#                         Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem
#                         QAQ  QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ
#                          QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ
#                           QAQ QAQ QAQ QAQ
#                            QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ QAQ
#                             QAQ QAQ QAQ QAQ QAQ
#                    ''')
