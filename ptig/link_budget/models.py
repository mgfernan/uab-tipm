from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class LinkDirection(Enum):
    UPLINK = "uplink"
    DOWNLINK = "downlink"


class ModulationScheme(Enum):
    BPSK = "BPSK"
    QPSK = "QPSK"
    QAM16 = "16-QAM"
    QAM54 = "64-QAM"
    QAM256 = "256-QAM"


class FreqBandType(Enum):
    S = "S"
    Ka = "Ka"


class OrbitType(Enum):
    GEO = "GEO"
    LEO = "LEO"


@dataclass
class UserEquipment:
    power_tx_dBm: float
    gain_tx_dBi: float
    loss_cable_tx_dB: float
    noise_figure_dB: float
    gain_rx_dBi: float
    temperature_antenna_K: float
    temperature_ambient_K: float
    altitude_m: float


@dataclass
class Satellite:
    orbit_type: OrbitType
    altitude_km: float
    eirp_density_dBm_per_MHz: float
    g_over_t_rx_dB_per_K: float


@dataclass
class Band:
    type: FreqBandType
    center_freq_GHz: float
    bw_user_MHz: float


@dataclass
class Link:
    satellite: Satellite
    band: Band
    elevation_angles_deg: list[float]


@dataclass
class PropagationLosses:
    shadowing_margin_dB: float
    additional_losses_dB: float
    polarization_loss_dB: float
    scintillation_loss_dB: float
    atmospheric_loss_dB: float

    def compute_total_loss_dB(self) -> float:
        return (
            self.shadowing_margin_dB
            + self.additional_losses_dB
            + self.polarization_loss_dB
            + self.scintillation_loss_dB
            + self.atmospheric_loss_dB
        )


@dataclass
class DataChannel:
    modulation: ModulationScheme
    n_bits: int
    n_symbols: int
    n_repetitions: int
    n_subframes: int
    n_resource_units: int


@dataclass
class WaveformParameters:
    n_used_subcarriers: int
    n_fft_bins: int
    data_symbol_duration_us: float
    cyclic_prefix_duration_us: float
    oversampling_factor: float


@dataclass
class BitErrorRateThreshold:
    modulation: ModulationScheme
    target_ber: float
    EbN0_threshold_dB: float
