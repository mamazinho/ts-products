import enum

from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from models.product_category_model import ProductCategoryModel
from sqlalchemy.orm import relationship
from config.settings import Settings
from datetime import datetime

class ProductMeasuresModel(Settings.Base):

    __tablename__ = 'product_measures'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    width_value = Column(Float)
    height_value = Column(Float)
    length_value = Column(Float)
    weight_value = Column(Float)

    def __str__(self):
        return f"{self.id} - {self.product_id} - {self.width_value} - {self.height_value} - {self.length_value} - {self.weight_value}"