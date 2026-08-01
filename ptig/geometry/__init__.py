"""Geometry helpers for satellite footprint and slant-range calculations."""

from .footprint import compute_boundary_lat_lon, compute_perpendicular_unit_vector, plot_fov_boundaries

__all__ = [
    "compute_boundary_lat_lon",
    "compute_perpendicular_unit_vector",
    "plot_fov_boundaries",
]
