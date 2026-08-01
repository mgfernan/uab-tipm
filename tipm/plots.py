from __future__ import annotations

from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


FR1_BANDS_L = {
    "n255": {"Uplink": (1626.5, 1660.5), "Downlink": (1525, 1559)},
    "n253": {"Uplink": (1668, 1675), "Downlink": (1518, 1525)},
}

FR1_BANDS_S = {
    "n256": {"Uplink": (1980, 2010), "Downlink": (2170, 2200)},
    "n254": {"Uplink": (1610, 1626.5), "Downlink": (2483.5, 2500)},
    "n252": {"Uplink": (2000, 2020), "Downlink": (2180, 2200)},
}

FR1_BANDS_KU = {
    "n248": {"Uplink": (14000, 14500), "Downlink": (10700, 12750)},
    "n247": {"Uplink": (13750, 14000), "Downlink": (10700, 12750)},
}

FR2_BANDS_KA = {
    "n510": {"Uplink": (27500, 28350), "Downlink": (17700, 20200)},
    "n511": {"Uplink": (28350, 30000), "Downlink": (17700, 20200)},
    "n512": {"Uplink": (27500, 30000), "Downlink": (17700, 20200)},
}

ALL_BANDS = {
    "FR1-L": FR1_BANDS_L,
    "FR1-S": FR1_BANDS_S,
    "FR1-Ku": FR1_BANDS_KU,
    "FR2-Ka": FR2_BANDS_KA,
}

COLORS = {"Uplink": "skyblue", "Downlink": "lightcoral"}


def plot_frequency_bands() -> None:
    """Render the FR1/FR2 frequency band charts used in the slide deck."""
    sns.set_theme(style="whitegrid")
    plt.rc("axes", unicode_minus=False)

    def plot_bands_on_axis(
        ax,
        band_type_names_for_this_subplot: List[str],
        xlim_range: Tuple[float, float],
        title_text: str,
        num_xticks: int = 5,
    ) -> None:
        current_y_pos = 0
        y_tick_positions: List[float] = []
        y_tick_labels: List[str] = []

        for band_type_name in band_type_names_for_this_subplot:
            bands_dict = ALL_BANDS[band_type_name]
            for band_name, freqs in bands_dict.items():
                y_tick_positions.append(current_y_pos)
                if "Downlink" in freqs:
                    start_freq_dl, end_freq_dl = freqs["Downlink"]
                    bandwidth_dl = end_freq_dl - start_freq_dl
                    y_tick_labels.append(f"{band_name} ({bandwidth_dl:.1f} MHz)")
                else:
                    y_tick_labels.append(band_name)
                current_y_pos += 1
            current_y_pos += 1

        current_y_pos_for_plotting = 0
        for band_type_name in band_type_names_for_this_subplot:
            bands_dict = ALL_BANDS[band_type_name]
            for band_name, freqs in bands_dict.items():
                for link_type, (start_freq, end_freq) in freqs.items():
                    width = end_freq - start_freq
                    legend_label = (
                        link_type
                        if (band_name == list(bands_dict.keys())[0] and band_type_name == band_type_names_for_this_subplot[0])
                        else ""
                    )
                    ax.barh(
                        current_y_pos_for_plotting,
                        width,
                        left=start_freq,
                        height=0.8,
                        color=COLORS[link_type],
                        edgecolor="white",
                        linewidth=0.8,
                        label=legend_label,
                    )
                    ax.text(
                        start_freq + width / 2,
                        current_y_pos_for_plotting - 0.4,
                        f"{start_freq}-{end_freq}",
                        va="top",
                        ha="center",
                        fontsize=7,
                        color="dimgray",
                    )
                current_y_pos_for_plotting += 1
            current_y_pos_for_plotting += 1

        ax.set_xlabel("Frequency (MHz)", fontsize=12)
        ax.set_title(title_text, fontsize=14)
        ax.grid(axis="x", linestyle="--", alpha=0.7, color=sns.color_palette("muted")[7])
        ax.grid(axis="y", linestyle="--", alpha=0.7, color=sns.color_palette("muted")[7])
        ax.set_yticks(y_tick_positions)
        ax.set_yticklabels(y_tick_labels, fontsize=9)
        ax.tick_params(axis="y", left=False)
        ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=num_xticks))

        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        if by_label:
            ax.legend(by_label.values(), by_label.keys(), title="Link Type", loc="upper right", frameon=True, borderpad=1)
        ax.set_xlim(xlim_range[0], xlim_range[1])
        ax.set_ylim(-1, current_y_pos - 1)
        sns.despine(ax=ax, top=True, right=True)

    fig_fr1, (ax1_fr1, ax2_fr1) = plt.subplots(
        2,
        1,
        figsize=(15, 10),
        sharex=False,
        gridspec_kw={"height_ratios": [1.8, 0.6]},
    )
    plot_bands_on_axis(ax1_fr1, ["FR1-L", "FR1-S"], (1400, 2600), "5G NR Band Allocation (FR1-L/S Bands)", num_xticks=5)
    plot_bands_on_axis(ax2_fr1, ["FR1-Ku"], (10000, 15000), "5G NR Band Allocation (FR1-Ku Band)", num_xticks=6)

    plt.tight_layout()
    plt.show()

    fig_fr2, ax_fr2 = plt.subplots(1, 1, figsize=(15, 5), sharex=False)
    plot_bands_on_axis(ax_fr2, ["FR2-Ka"], (15000, 32000), "5G NR Band Allocation (FR2-Ka Band)", num_xticks=7)

    plt.tight_layout()
    plt.show()
