# Replace 'your_layer_name' with the actual name of your vector layer

from PyQt5.QtGui import QColor
from qgis.core import QgsProject, QgsSymbol, QgsCategorizedSymbolRenderer, QgsRendererCategory
from datetime import datetime

layer_name = 'Morocco-Earthquake-Sept-2023'
date_column = 'datetime'

layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# Create a categorization style
categories = []

# Define the date format
date_format = "%Y-%m-%d"

# Convert the cutoff date to a datetime object
cutoff_datetime = datetime.strptime('2023-09-10', date_format)

# Iterate over features and categorize based on the date
for feature in layer.getFeatures():
    date_str = feature[date_column].toString(date_format)  # Convert QDateTime to string
    
    # Convert the date string to a datetime object
    feature_datetime = datetime.strptime(date_str, date_format)

    # Categorize based on the date
    if feature_datetime >= cutoff_datetime:
        category = 'After'
        color = QColor('red')
    else:
        category = 'Before'
        color = QColor('blue')

    # Create a symbol for the category
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(color)

    # Append the category and symbol to the list
    categories.append(QgsRendererCategory(feature[feature.fieldNameIndex(date_column)], symbol, category))

# Apply the categorized style to the layer
renderer = QgsCategorizedSymbolRenderer(date_column, categories)
layer.setRenderer(renderer)

# Refresh the layer to apply the changes
layer.triggerRepaint()
