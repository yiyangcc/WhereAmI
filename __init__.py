# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WhereAmI
                                 A QGIS plugin
 Show location of a point click on the map
                             -------------------
        begin                : 2017-01-14
        copyright            : (C) 2017 by yiyang
        email                : chiangyiyang@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WhereAmI class from file WhereAmI.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .WhereAmI import WhereAmI
    return WhereAmI(iface)
