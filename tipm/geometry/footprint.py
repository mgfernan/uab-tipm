from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
from pygnss.geodetic import lla_to_xyz, xyz_to_lla

R_E_KM = 6378.137


def compute_perpendicular_unit_vector(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    if a.shape != (3,):
        raise ValueError("a must be a shape (3,) vector")

    axes = np.eye(3)
    e = axes[np.argmin(np.abs(a))]
    b = np.cross(a, e)
    r_b = np.linalg.norm(b)
    if r_b == 0:
        raise ValueError("Cannot compute a perpendicular vector (a is zero vector).")
    return b / r_b


def compute_boundary_lat_lon(lat_sat_deg: float, lon_sat_deg: float, height_sat_km: float, nadir_angle_deg: float, n_points: int = 361):
    r_s_km = R_E_KM + height_sat_km
    nadir_angle_rad = np.radians(nadir_angle_deg)
    gamma_rad = np.arcsin(r_s_km / R_E_KM * np.sin(nadir_angle_rad)) - nadir_angle_rad

    s = np.array(tuple(lla_to_xyz(lon_sat_deg, lat_sat_deg, height_sat_km)))
    r_s = np.linalg.norm(s)
    u = s / r_s
    k = compute_perpendicular_unit_vector(u)
    e = np.cross(k, u)
    e = e / np.linalg.norm(e)
    n = np.cross(u, e)

    u = u.reshape(3, 1)
    e = e.reshape(3, 1)
    n = n.reshape(3, 1)

    az = np.linspace(0, 2.0 * np.pi, n_points).reshape(1, -1)
    cos_az = np.cos(az)
    sin_az = np.sin(az)
    cos_gamma = np.cos(gamma_rad)
    sin_gamma = np.sin(gamma_rad)

    p = R_E_KM * 1000.0 * (u * cos_gamma + e * sin_gamma * cos_az + n * sin_gamma * sin_az)

    xs_m = p[0, :]
    ys_m = p[1, :]
    zs_m = p[2, :]

    lon_deg, lat_deg, _ = xyz_to_lla(xs_m, ys_m, zs_m)
    return lat_deg, lon_deg


def plot_fov_boundaries(lat0_deg: float, lon0_deg: float, h: float, elevations_deg, R_E):
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    nadir_max = np.degrees(np.arcsin(R_E / (R_E + h) * np.cos(np.radians(elevations_deg))))

    fig = go.Figure()
    for i, nadir_deg in enumerate(nadir_max):
        lat_curve, lon_curve = compute_boundary_lat_lon(lat0_deg, lon0_deg, h, nadir_deg, n_points=361)
        elev = elevations_deg[i]
        fig.add_trace(
            go.Scattergeo(
                lon=lon_curve,
                lat=lat_curve,
                mode="lines",
                line=dict(width=2, color=colors[i % len(colors)]),
                name=f"ε_min = {elev}º",
            )
        )

    fig.add_trace(
        go.Scattergeo(
            lon=[lon0_deg],
            lat=[lat0_deg],
            mode="markers",
            marker=dict(size=7, color="black"),
            name="Sub-satellite point",
        )
    )

    fig.update_layout(
        title=f"Satellite FoV Footprint: Lat {lat0_deg}°, Lon {lon0_deg}°, Alt {h} km",
        showlegend=True,
        margin=dict(l=10, r=10, t=50, b=10),
        geo=dict(
            projection_type="equirectangular",
            showland=True,
            landcolor="rgb(240,240,240)",
            showcountries=True,
            showocean=True,
            oceancolor="rgb(210,230,255)",
            showframe=False,
            bgcolor="white",
            lataxis=dict(range=[-90, 90]),
            lonaxis=dict(range=[-180, 180]),
        ),
    )
    return fig
