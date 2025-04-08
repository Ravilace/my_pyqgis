from qgis.core import QgsMapLayer, QgsRasterLayer, QgsVectorLayer
import os

def read_raster_file(raster_file_path):
    tif_base_name = os.path.basename(raster_file_path)
    raster_layer = QgsRasterLayer(raster_file_path, tif_base_name)
    return raster_layer

def get_raster_layer_attrs(raster_layer):
    print(f"{raster_layer.name()=}\n"
          f"{raster_layer.type()=}\n"
          f"{raster_layer.height()=}\n"
          f"{raster_layer.width()=}\n"
          f"{raster_layer.bandCount()=}\n"
          f"{raster_layer.extent()=}\n"
          f"{raster_layer.source()=}\n"
          f"{raster_layer.crs()=}\n")

if __name__ == '__main__':
    tif_path = r"F:\Work\面状图斑\15_新\小数据\tif\0_0.tif"
    tif_layer = read_raster_file(tif_path)
    get_raster_layer_attrs(tif_layer)
