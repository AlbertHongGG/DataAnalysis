from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.figure import Figure


@dataclass(frozen=True)
class PlotContext:
    data: pd.DataFrame
    output_dir: Path


class PlotJob(ABC):
    file_name: str
    title: str

    def render(self, context: PlotContext) -> Path:
        sns.set_theme(style="whitegrid", context="talk")
        figure, axis = plt.subplots(figsize=(12, 7))

        try:
            self.draw(axis, context.data)
            figure.tight_layout()
            output_path = context.output_dir / self.file_name
            figure.savefig(output_path, dpi=300, bbox_inches="tight")
            return output_path
        finally:
            plt.close(figure)

    @abstractmethod
    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        raise NotImplementedError

    def _apply_common_style(self, axis: Axes) -> None:
        axis.set_title(self.title, pad=16, weight="semibold")
        axis.grid(True, linestyle="--", alpha=0.35)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)


def configure_regression_style(color: str) -> dict[str, object]:
    return {
        "scatter_kws": {"s": 110, "alpha": 0.88, "color": color},
        "line_kws": {"linewidth": 2.4, "color": color},
        "ci": 95,
        "truncate": False,
    }