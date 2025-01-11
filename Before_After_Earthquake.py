# Replace 'your_layer_name' with the actual name of your vector layer
from PyQt5.QtGui import QColor
from qgis.core import QgsProject, QgsSymbol, QgsCategorizedSymbolRenderer, QgsRendererCategory
from PyQt5.QtCore import QDateTime

layer_name = 'Morocco-Earthquake-Sept'
date_column = 'datetime'
cutoff_date = '2023-09-10 11:25:14'

layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# Create a categorization style
categories = []

# Convert the cutoff date to a QDateTime object
cutoff_datetime = QDateTime.fromString(cutoff_date, "yyyy-MM-dd HH:mm:ss")

# Iterate over features and categorize based on the date
for feature in layer.getFeatures():
    # Convert the QDateTime to a string
    date_str = feature[date_column].toString("yyyy-MM-dd HH:mm:ss")

    # Convert the date string to a QDateTime object
    feature_datetime = QDateTime.fromString(date_str, "yyyy-MM-dd HH:mm:ss")

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
