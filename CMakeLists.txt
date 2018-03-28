################################################################################
# Project:  Lib QWT
# Purpose:  CMake build scripts
# Author:   Dmitry Baryshnikov, dmitry.baryshnikov@nexgis.com
################################################################################
# Copyright (C) 2017, NextGIS <info@nextgis.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
################################################################################

cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

project(qwt)

# Some init settings
set(CMAKE_COLOR_MAKEFILE ON)
# Set path to additional CMake modules
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

if(OSX_FRAMEWORK AND (BUILD_SHARED_LIBS OR BUILD_STATIC_LIBS))
  message(FATAL_ERROR "Only OSX_FRAMEWORK key or any or both BUILD_SHARED_LIBS
                       and BUILD_STATIC_LIBS keys are permitted")
endif()

if(OSX_FRAMEWORK)
  set(INSTALL_BIN_DIR "bin" CACHE INTERNAL "Installation directory for executables" FORCE)
  set(INSTALL_LIB_DIR "Library/Frameworks" CACHE INTERNAL "Installation directory for libraries" FORCE)
  set(INSTALL_INC_DIR ${INSTALL_LIB_DIR}/${PROJECT_NAME}.framework/Headers CACHE INTERNAL "Installation directory for headers" FORCE)
  set(INSTALL_CMAKECONF_DIR ${INSTALL_LIB_DIR}/${PROJECT_NAME}.framework/Resources/CMake CACHE INTERNAL "Installation directory for cmake config files" FORCE)
  set(SKIP_INSTALL_HEADERS ON)
  set(SKIP_INSTALL_EXECUTABLES ON)
  set(SKIP_INSTALL_FILES ON)
  set(SKIP_INSTALL_EXPORT ON)
  set(CMAKE_MACOSX_RPATH ON)
else()
    include(GNUInstallDirs)

    set(INSTALL_BIN_DIR ${CMAKE_INSTALL_BINDIR} CACHE INTERNAL "Installation directory for executables" FORCE)
    set(INSTALL_LIB_DIR ${CMAKE_INSTALL_LIBDIR} CACHE INTERNAL "Installation directory for libraries" FORCE)
    set(INSTALL_INC_DIR ${CMAKE_INSTALL_INCLUDEDIR} CACHE INTERNAL "Installation directory for headers" FORCE)
    set(INSTALL_DOC_DIR ${CMAKE_INSTALL_DOCDIR} CACHE INTERNAL "Share directory for data" FORCE)
    set(INSTALL_CMAKECONF_DIR ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME}/CMake CACHE INTERNAL "Installation directory for cmake config files" FORCE)
endif()

include(util)
check_version(QWT_MAJOR_VERSION QWT_MINOR_VERSION QWT_REV_VERSION)
set(VERSION ${QWT_MAJOR_VERSION}.${QWT_MINOR_VERSION}.${QWT_REV_VERSION})

if(OSX_FRAMEWORK)
    set(FRAMEWORK_VERSION "${QWT_MAJOR_VERSION}")
endif()
report_version(${PROJECT_NAME} ${VERSION})

configure_file(${CMAKE_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake IMMEDIATE @ONLY)

if(OSX_FRAMEWORK OR BUILD_SHARED_LIBS)
    add_definitions(-DQWT_DLL)
endif()

option(QT4_BUILD "Build with qt4" ON)

include(FindAnyProject)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
if(QT4_BUILD)
    find_anyproject(Qt4 REQUIRED COMPONENTS QtCore QtGui)
else()
    find_anyproject(Qt5 REQUIRED COMPONENTS Qt5Widgets Qt5Concurrent Qt5PrintSupport)
endif()

option(WITH_SVG "If you want to display svg images on the plot canvas, or export a plot to a SVG document" ON)
if(WITH_SVG)
    if(QT4_BUILD)
        find_anyproject(Qt4 REQUIRED COMPONENTS QtSvg)
    else()
        find_anyproject(Qt5 REQUIRED COMPONENTS Qt5Svg)
    endif()
else()
    add_definitions(-DQWT_NO_SVG)
endif()

option(WITH_QWTPLOT "QwtPlot enables all classes, that are needed to use the QwtPlot widget" ON)
option(WITH_QWTWIDGETS "QwtWidgets enables all classes, that are needed to use the all other widgets (sliders, dials, ...), beside QwtPlot" ON)
option(WITH_QWTOPENGL "If you want to use a OpenGL plot canvas" ON)
if(WITH_QWTOPENGL)
    if(QT4_BUILD)
        find_anyproject(Qt4 REQUIRED COMPONENTS QtOpenGL)
    else()
        find_anyproject(Qt5 REQUIRED COMPONENTS Qt5OpenGL)
    endif()
else()
    add_definitions(-DQWT_NO_OPENGL)
endif()
option(WITH_QWTMATHML "You can use the MathML renderer of the Qt solutions package to enable MathML support in Qwt" OFF)
option(WITH_QWTDESIGNER "If you want to build the Qwt designer plugin" OFF)
option(WITH_QWTPLAYGROUND "The playground is primarily intended for the Qwt development to explore and test new features" OFF)
option(WITH_QWTEXAMPLES "If you want to auto build the examples" OFF)

# TODO: remove implemented features from if
if(WITH_QWTPLAYGROUND OR WITH_QWTEXAMPLES OR WITH_QWTDESIGNER)
    message(FATAL_ERROR "Not cmaked yet!")
endif()

set(LIB_NAME ${PROJECT_NAME})
set(PACKAGE_NAME ${PROJECT_NAME})
string(TOUPPER ${PACKAGE_NAME} PACKAGE_UPPER_NAME)

add_subdirectory(src)

if(WITH_QWTDESIGNER)
    add_subdirectory(designer)
endif()
if(WITH_QWTPLAYGROUND)
    add_subdirectory(playground)
endif()
if(WITH_QWTEXAMPLES)
    add_subdirectory(examples)
endif()


# uninstall
add_custom_target(uninstall COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake)

# Export package ===============================================================

if(REGISTER_PACKAGE)
    # Export the package for use from the build-tree
    # (this registers the build-tree with a global CMake-registry)
    export(PACKAGE ${PACKAGE_UPPER_NAME})
endif()

# Create the <Package>Config.cmake file
configure_file(cmake/PackageConfig.cmake.in
    ${PROJECT_BINARY_DIR}/${PACKAGE_UPPER_NAME}Config.cmake @ONLY)

# Archiving ====================================================================

set(CPACK_PACKAGE_NAME "${PACKAGE_NAME}")
set(CPACK_PACKAGE_VENDOR "${PACKAGE_VENDOR}")
set(CPACK_PACKAGE_VERSION "${VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "${PACKAGE_NAME} Installation")
set(CPACK_PACKAGE_RELOCATABLE TRUE)
set(CPACK_ARCHIVE_COMPONENT_INSTALL ON)
set(CPACK_GENERATOR "ZIP")
set(CPACK_MONOLITHIC_INSTALL ON)
set(CPACK_STRIP_FILES TRUE)

# Get cpack zip archive name
get_cpack_filename(${VERSION} PROJECT_CPACK_FILENAME)
set(CPACK_PACKAGE_FILE_NAME ${PROJECT_CPACK_FILENAME})

include(CPack)
