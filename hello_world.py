from qgis.core import *

if __name__ == '__main__':
    # 第二个参数为是否启用 GUI
    qgs = QgsApplication([], False)
    # 初始化 QGIS
    qgs.initQgis()
    print(QgsApplication.prefixPath())
    print('Hello Qgis!')