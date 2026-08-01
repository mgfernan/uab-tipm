from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

from .models import (
    Band,
    BitErrorRateThreshold,
    DataChannel,
    FreqBandType,
    Link,
    LinkDirection,
    ModulationScheme,
    OrbitType,
    PropagationLosses,
    Satellite,
    UserEquipment,
    WaveformParameters,
)


def compute_slant_range(altitude_km: float, elevation_angle_deg: float) -> float:
    r_e_km = 6371.0
    return (
        np.sqrt((r_e_km + altitude_km) ** 2 - r_e_km**2 * np.cos(np.radians(elevation_angle_deg)) ** 2)
        - r_e_km * np.sin(np.radians(elevation_angle_deg))
    )


def compute_free_space_path_loss(slant_range_km: float, center_frequency_GHz: float) -> float:
    speed_of_light_m_s = 299792458.0
    wavelength_m = speed_of_light_m_s / (center_frequency_GHz * 1e9)
    return 20 * np.log10(4 * np.pi * slant_range_km * 1e3 / wavelength_m)


def compute_eirp(user_equipment: UserEquipment) -> float:
    return user_equipment.power_tx_dBm + user_equipment.gain_tx_dBi - user_equipment.loss_cable_tx_dB - 30


def compute_modulation_order(modulation: ModulationScheme) -> int:
    return {
        ModulationScheme.BPSK: 1,
        ModulationScheme.QPSK: 2,
        ModulationScheme.QAM16: 4,
        ModulationScheme.QAM54: 1,
        ModulationScheme.QAM256: 1,
    }[modulation]


def compute_r_eff(data_channel: DataChannel, link_direction: LinkDirection) -> float:
    modulation_order = compute_modulation_order(data_channel.modulation)
    r_eff = (data_channel.n_bits + 24) / (data_channel.n_symbols * modulation_order * data_channel.n_repetitions)
    if link_direction == LinkDirection.UPLINK:
        return r_eff / data_channel.n_resource_units
    return r_eff / data_channel.n_subframes


def compute_cnr_ref(data_channel: DataChannel, ber_thresholds: Dict[ModulationScheme, BitErrorRateThreshold]) -> float:
    threshold = ber_thresholds[data_channel.modulation]
    modulation_order = compute_modulation_order(data_channel.modulation)
    return threshold.EbN0_threshold_dB + 10 * np.log10(modulation_order) + 10 * np.log10(data_channel.n_symbols / data_channel.n_bits)


def compute_cnr(eirp_dbw: float, g_over_t_rx_dB_per_K: float, bandwidth_mhz: float, fspl_dB: float, total_loss_dB: float) -> float:
    return eirp_dbw + g_over_t_rx_dB_per_K - 10 * np.log10(1.38e-23 * bandwidth_mhz * 1e6) - fspl_dB - total_loss_dB


def compute_two_way_latency_s(slant_range_km: float) -> float:
    c_km_per_s = 299792.458
    return (2 * slant_range_km) / c_km_per_s


def build_link_budget_state() -> Dict[str, object]:
    user_equipment = UserEquipment(
        power_tx_dBm=23,
        gain_tx_dBi=0,
        loss_cable_tx_dB=0,
        noise_figure_dB=7,
        gain_rx_dBi=0,
        temperature_antenna_K=290,
        temperature_ambient_K=290,
        altitude_m=0,
    )

    satellites = {
        "GEO": Satellite(orbit_type=OrbitType.GEO, altitude_km=36000, eirp_density_dBm_per_MHz=59, g_over_t_rx_dB_per_K=19),
        "LEO": Satellite(orbit_type=OrbitType.LEO, altitude_km=1200, eirp_density_dBm_per_MHz=40, g_over_t_rx_dB_per_K=1.1),
        "STARLINK": Satellite(orbit_type=OrbitType.LEO, altitude_km=550, eirp_density_dBm_per_MHz=34, g_over_t_rx_dB_per_K=1.1),
    }

    bands = {
        "S": Band(type=FreqBandType.S, bw_user_MHz=0.18, center_freq_GHz=2.0),
        "Ka": Band(type=FreqBandType.Ka, bw_user_MHz=400, center_freq_GHz=30.0),
    }

    links = {
        "downlink": Link(satellite=satellites["GEO"], band=bands["S"], elevation_angles_deg=[0, 5, 10]),
        "uplink": Link(satellite=satellites["GEO"], band=bands["S"], elevation_angles_deg=[0, 5, 10]),
    }

    propagation_losses = PropagationLosses(
        shadowing_margin_dB=3,
        additional_losses_dB=0,
        polarization_loss_dB=3,
        scintillation_loss_dB=2.2,
        atmospheric_loss_dB=0.2,
    )

    data_channel = DataChannel(
        modulation=ModulationScheme.QPSK,
        n_bits=208,
        n_symbols=160,
        n_repetitions=1,
        n_subframes=8,
        n_resource_units=1,
    )

    waveform_parameters = WaveformParameters(
        n_used_subcarriers=72,
        n_fft_bins=128,
        data_symbol_duration_us=1.0 / 1.92e6 * 128,
        cyclic_prefix_duration_us=1.0 / 1.92e6 * 9,
        oversampling_factor=1.0,
    )

    ber_thresholds = {
        ModulationScheme.BPSK: BitErrorRateThreshold(modulation=ModulationScheme.BPSK, target_ber=1e-6, EbN0_threshold_dB=10.5),
        ModulationScheme.QPSK: BitErrorRateThreshold(modulation=ModulationScheme.QPSK, target_ber=1e-6, EbN0_threshold_dB=10.5),
        ModulationScheme.QAM16: BitErrorRateThreshold(modulation=ModulationScheme.QAM16, target_ber=1e-6, EbN0_threshold_dB=14.4),
    }

    return {
        "user_equipment": user_equipment,
        "satellites": satellites,
        "bands": bands,
        "links": links,
        "propagation_losses": propagation_losses,
        "data_channel": data_channel,
        "waveform_parameters": waveform_parameters,
        "ber_thresholds": ber_thresholds,
    }
