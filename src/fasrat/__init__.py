"""
FASRAT - Fast Area-weighted Spatial ReAggregation Tool

A Python package for computing area-weighted spatial reaggregation weights
between shapefile geometries and raster pixels.
"""

__version__ = "0.1.0"

from .geometry import *
from .constants import *
from .process import compute_raster_weights

__all__ = ["compute_raster_weights", "NON_CONTIGUOUS_STATES"]
