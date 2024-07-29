# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CoordinateCaptureDockWidget
                                 A QGIS plugin
 Python port of the deprecated Coordinate Capture core plugin
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-04
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Stefanos Natsis
        email                : uclaros@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import QWidget, QDockWidget, QGridLayout, QPushButton, QLineEdit, QToolButton, QLabel
from qgis.PyQt.QtGui import QIcon, QPixmap


class CoordinateCaptureDockWidget(QDockWidget):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(CoordinateCaptureDockWidget, self).__init__(parent)

        self.setWindowTitle(self.tr("Coordinate Capture"))
        self.setGeometry(0, 0, 300, 228)
        self.dockWidgetContents = QWidget(self)
        self.setWidget(self.dockWidgetContents)
        self.gridLayout = QGridLayout()
        self.dockWidgetContents.setLayout(self.gridLayout)

        self.dockWidgetContents.layout().setColumnMinimumWidth(0, 36)

        self.userCrsToolButton = QToolButton(self.dockWidgetContents)
        self.userCrsToolButton.setIcon(QIcon(":/plugins/coordinate_capture/mIconProjectionEnabled.svg"))
        self.userCrsToolButton.setToolTip(self.tr("Click to select the CRS to use for coordinate display"))

        self.userCrsLabel = QLabel(self.dockWidgetContents)
        self.userCrsLabel.setPixmap(QPixmap(":/plugins/coordinate_capture/transformed.svg"))
        self.userCrsLabel.setGeometry(self.userCrsToolButton.geometry())

        self.userCrsEdit = QLineEdit(self.dockWidgetContents)
        self.userCrsEdit.setReadOnly(True)
        self.userCrsEdit.setToolTip(self.tr("Coordinate in your selected CRS (lat,lon or east,north)"))
        self.copyUserCrsCoordinatesAction = self.userCrsEdit.addAction(QIcon(":/plugins/coordinate_capture/mActionEditCopy.svg"),
                                                                       QLineEdit.TrailingPosition)
        self.copyUserCrsCoordinatesAction.triggered.connect(self.copyUserCrsCoordinates)

        self.canvasCrsEdit = QLineEdit(self.dockWidgetContents)
        self.canvasCrsEdit.setReadOnly(True)
        self.canvasCrsEdit.setToolTip(self.tr("Coordinate in map canvas coordinate reference system (lat,lon or east,north)"))
        self.copyCanvasCrsCoordinatesAction = self.canvasCrsEdit.addAction(QIcon(":/plugins/coordinate_capture/mActionEditCopy.svg"),
                                                                           QLineEdit.TrailingPosition)
        self.copyCanvasCrsCoordinatesAction.triggered.connect(self.copyCanvasCrsCoordinates)

        self.trackMouseButton = QToolButton(self.dockWidgetContents)
        self.trackMouseButton.setIcon(QIcon(":/plugins/coordinate_capture/tracking.svg"))
        self.trackMouseButton.setCheckable(True)
        self.trackMouseButton.setToolTip(self.tr("Click to enable mouse tracking. Click the canvas to stop"))
        self.trackMouseButton.setChecked(False)

        # Create the action for tool
        self.captureButton = QPushButton(self.dockWidgetContents)
        self.captureButton.setText(self.tr("Start Capture"))
        self.captureButton.setToolTip(self.tr("Click to enable coordinate capture"))
        self.captureButton.setIcon(QIcon(":/plugins/coordinate_capture/coordinate_capture.png"))
        self.captureButton.setWhatsThis(self.tr("Click on the map to view coordinates and capture to clipboard."))

        # // Set the icons
        # setCurrentTheme(QString());

        self.dockWidgetContents.layout().addWidget(self.userCrsToolButton, 0, 0)
        self.dockWidgetContents.layout().addWidget(self.userCrsEdit, 0, 1)
        self.dockWidgetContents.layout().addWidget(self.userCrsLabel, 1, 0)
        self.dockWidgetContents.layout().addWidget(self.canvasCrsEdit, 1, 1)
        self.dockWidgetContents.layout().addWidget(self.trackMouseButton, 2, 0)
        self.dockWidgetContents.layout().addWidget(self.captureButton, 2, 1)

    def copyUserCrsCoordinates(self):
        self.userCrsEdit.selectAll()
        self.userCrsEdit.copy()

    def copyCanvasCrsCoordinates(self):
        self.canvasCrsEdit.selectAll()
        self.canvasCrsEdit.copy()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
