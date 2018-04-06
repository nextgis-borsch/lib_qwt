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

set(HHEADERS
    qwt.h
    qwt_abstract_scale_draw.h
    qwt_clipper.h
    qwt_color_map.h
    qwt_compat.h
    qwt_column_symbol.h
    qwt_date.h
    qwt_date_scale_draw.h
    qwt_date_scale_engine.h
    qwt_dyngrid_layout.h
    qwt_global.h
    qwt_graphic.h
    qwt_interval.h
    qwt_interval_symbol.h
    qwt_math.h
    qwt_magnifier.h
    qwt_null_paintdevice.h
    qwt_painter.h
    qwt_painter_command.h
    qwt_panner.h
    qwt_picker.h
    qwt_picker_machine.h
    qwt_pixel_matrix.h
    qwt_point_3d.h
    qwt_point_polar.h
    qwt_round_scale_draw.h
    qwt_scale_div.h
    qwt_scale_draw.h
    qwt_scale_engine.h
    qwt_scale_map.h
    qwt_spline.h
    qwt_symbol.h
    qwt_system_clock.h
    qwt_text_engine.h
    qwt_text_label.h
    qwt_text.h
    qwt_transform.h
    qwt_widget_overlay.h
)

set(CSOURCES
    qwt_abstract_scale_draw.cpp
    qwt_clipper.cpp
    qwt_color_map.cpp
    qwt_column_symbol.cpp
    qwt_date.cpp
    qwt_date_scale_draw.cpp
    qwt_date_scale_engine.cpp
    qwt_dyngrid_layout.cpp
    qwt_event_pattern.cpp
    qwt_graphic.cpp
    qwt_interval.cpp
    qwt_interval_symbol.cpp
    qwt_math.cpp
    qwt_magnifier.cpp
    qwt_null_paintdevice.cpp
    qwt_painter.cpp
    qwt_painter_command.cpp
    qwt_panner.cpp
    qwt_picker.cpp
    qwt_picker_machine.cpp
    qwt_pixel_matrix.cpp
    qwt_point_3d.cpp
    qwt_point_polar.cpp
    qwt_round_scale_draw.cpp
    qwt_scale_div.cpp
    qwt_scale_draw.cpp
    qwt_scale_map.cpp
    qwt_spline.cpp
    qwt_scale_engine.cpp
    qwt_symbol.cpp
    qwt_system_clock.cpp
    qwt_text_engine.cpp
    qwt_text_label.cpp
    qwt_text.cpp
    qwt_transform.cpp
    qwt_widget_overlay.cpp
)

if(WITH_QWTPLOT)
    set(HHEADERS ${HHEADERS}
        qwt_curve_fitter.h
        qwt_event_pattern.h
        qwt_abstract_legend.h
        qwt_legend.h
        qwt_legend_data.h
        qwt_legend_label.h
        qwt_plot.h
        qwt_plot_renderer.h
        qwt_plot_curve.h
        qwt_plot_dict.h
        qwt_plot_directpainter.h
        qwt_plot_grid.h
        qwt_plot_histogram.h
        qwt_plot_item.h
        qwt_plot_abstract_barchart.h
        qwt_plot_barchart.h
        qwt_plot_multi_barchart.h
        qwt_plot_intervalcurve.h
        qwt_plot_tradingcurve.h
        qwt_plot_layout.h
        qwt_plot_marker.h
        qwt_plot_zoneitem.h
        qwt_plot_textlabel.h
        qwt_plot_rasteritem.h
        qwt_plot_spectrogram.h
        qwt_plot_spectrocurve.h
        qwt_plot_scaleitem.h
        qwt_plot_legenditem.h
        qwt_plot_seriesitem.h
        qwt_plot_shapeitem.h
        qwt_plot_canvas.h
        qwt_plot_panner.h
        qwt_plot_picker.h
        qwt_plot_zoomer.h
        qwt_plot_magnifier.h
        qwt_plot_rescaler.h
        qwt_point_mapper.h
        qwt_raster_data.h
        qwt_matrix_raster_data.h
        qwt_sampling_thread.h
        qwt_samples.h
        qwt_series_data.h
        qwt_series_store.h
        qwt_point_data.h
        qwt_scale_widget.h
    )

    set(CSOURCES ${CSOURCES}
        qwt_curve_fitter.cpp
        qwt_abstract_legend.cpp
        qwt_legend.cpp
        qwt_legend_data.cpp
        qwt_legend_label.cpp
        qwt_plot.cpp
        qwt_plot_renderer.cpp
        qwt_plot_xml.cpp
        qwt_plot_axis.cpp
        qwt_plot_curve.cpp
        qwt_plot_dict.cpp
        qwt_plot_directpainter.cpp
        qwt_plot_grid.cpp
        qwt_plot_histogram.cpp
        qwt_plot_item.cpp
        qwt_plot_abstract_barchart.cpp
        qwt_plot_barchart.cpp
        qwt_plot_multi_barchart.cpp
        qwt_plot_intervalcurve.cpp
        qwt_plot_zoneitem.cpp
        qwt_plot_tradingcurve.cpp
        qwt_plot_spectrogram.cpp
        qwt_plot_spectrocurve.cpp
        qwt_plot_scaleitem.cpp
        qwt_plot_legenditem.cpp
        qwt_plot_seriesitem.cpp
        qwt_plot_shapeitem.cpp
        qwt_plot_marker.cpp
        qwt_plot_textlabel.cpp
        qwt_plot_layout.cpp
        qwt_plot_canvas.cpp
        qwt_plot_panner.cpp
        qwt_plot_rasteritem.cpp
        qwt_plot_picker.cpp
        qwt_plot_zoomer.cpp
        qwt_plot_magnifier.cpp
        qwt_plot_rescaler.cpp
        qwt_point_mapper.cpp
        qwt_raster_data.cpp
        qwt_matrix_raster_data.cpp
        qwt_sampling_thread.cpp
        qwt_series_data.cpp
        qwt_point_data.cpp
        qwt_scale_widget.cpp
    )
endif()

if(WITH_SVG)
    set(HHEADERS ${HHEADERS} qwt_plot_svgitem.h)
    set(CSOURCES ${CSOURCES} qwt_plot_svgitem.cpp)
endif()

if(WITH_QWTOPENGL)
    set(HHEADERS ${HHEADERS} qwt_plot_glcanvas.h)
    set(CSOURCES ${CSOURCES} qwt_plot_glcanvas.cpp)
endif()

if(WITH_QWTWIDGETS)
    set(HHEADERS ${HHEADERS}
        qwt_abstract_slider.h
        qwt_abstract_scale.h
        qwt_arrow_button.h
        qwt_analog_clock.h
        qwt_compass.h
        qwt_compass_rose.h
        qwt_counter.h
        qwt_dial.h
        qwt_dial_needle.h
        qwt_knob.h
        qwt_slider.h
        qwt_thermo.h
        qwt_wheel.h
    )

    set(CSOURCES ${CSOURCES}
        qwt_abstract_slider.cpp
        qwt_abstract_scale.cpp
        qwt_arrow_button.cpp
        qwt_analog_clock.cpp
        qwt_compass.cpp
        qwt_compass_rose.cpp
        qwt_counter.cpp
        qwt_dial.cpp
        qwt_dial_needle.cpp
        qwt_knob.cpp
        qwt_slider.cpp
        qwt_thermo.cpp
        qwt_wheel.cpp
    )
endif()

QT4_WRAP_CPP(QWT_MOC_SOURCES ${HHEADERS})

if(BUILD_SHARED_LIBS)
    add_library(${LIB_NAME} SHARED ${CSOURCES} ${QWT_MOC_SOURCES} ${HHEADERS})
    set_target_properties (${LIB_NAME} PROPERTIES
        VERSION ${VERSION}
        SOVERSION ${QWT_MAJOR_VERSION}
        DEFINE_SYMBOL QWT_MAKEDLL)
elseif(OSX_FRAMEWORK)
    add_library(${LIB_NAME} SHARED ${CSOURCES} ${QWT_MOC_SOURCES} ${HHEADERS})
    set_target_properties(${LIB_NAME} PROPERTIES
      FRAMEWORK TRUE
      FRAMEWORK_VERSION ${FRAMEWORK_VERSION}
      MACOSX_FRAMEWORK_SHORT_VERSION_STRING ${VERSION}
      MACOSX_FRAMEWORK_BUNDLE_VERSION ${VERSION}
      MACOSX_FRAMEWORK_IDENTIFIER org.qwt.qwt
      XCODE_ATTRIBUTE_INSTALL_PATH "@rpath"
      PUBLIC_HEADER "${HHEADERS}"
      VERSION ${VERSION}
      SOVERSION ${QWT_MAJOR_VERSION}
      )
else()
    add_library(${LIB_NAME} STATIC ${CSOURCES} ${QWT_MOC_SOURCES} ${HHEADERS})
endif()

target_link_extlibraries(${LIB_NAME})
set(TARGET_LINK_LIB ${TARGET_LINK_LIB} ${LIB_NAME} PARENT_SCOPE)

# Add path to includes to build-tree export
target_include_directories(${LIB_NAME} INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
)

if(WIN32)
    target_compile_definitions(${LIB_NAME} INTERFACE QWT_DLL)
endif()

# Add all targets to the build-tree export set
export(TARGETS ${LIB_NAME}
    FILE ${PROJECT_BINARY_DIR}/${PACKAGE_UPPER_NAME}Targets.cmake)

###############################################################################
# Targets installation

if(NOT SKIP_INSTALL_LIBRARIES AND NOT SKIP_INSTALL_ALL)
    install(TARGETS ${LIB_NAME}
        EXPORT ${PACKAGE_UPPER_NAME}Targets
        RUNTIME DESTINATION ${INSTALL_BIN_DIR}
        LIBRARY DESTINATION ${INSTALL_LIB_DIR}
        ARCHIVE DESTINATION ${INSTALL_LIB_DIR}
        INCLUDES DESTINATION ${INSTALL_INC_DIR}
        FRAMEWORK DESTINATION ${INSTALL_LIB_DIR}
    )
endif()

if(NOT SKIP_INSTALL_HEADERS AND NOT SKIP_INSTALL_ALL)
    install(FILES ${HHEADERS} DESTINATION "${INSTALL_INC_DIR}/${PROJECT_NAME}")
endif()

if(NOT SKIP_INSTALL_LIBRARIES AND NOT SKIP_INSTALL_ALL)
    # Install the <Package>Config.cmake
    install(FILES
      ${PROJECT_BINARY_DIR}/${PACKAGE_UPPER_NAME}Config.cmake
      DESTINATION ${INSTALL_CMAKECONF_DIR} COMPONENT dev)

    # Install the export set for use with the install-tree
    install(EXPORT ${PACKAGE_UPPER_NAME}Targets DESTINATION ${INSTALL_CMAKECONF_DIR} COMPONENT dev)
endif()
