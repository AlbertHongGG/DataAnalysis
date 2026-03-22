from __future__ import annotations

import seaborn as sns
from matplotlib.axes import Axes
import pandas as pd

from analysis_app.plot_base import PlotJob, configure_regression_style


class CogVsCycloSPlot(PlotJob):
    file_name = "03_cog_fn_s_vs_cyclo_fn_s.png"
    title = "Cyclomatic vs. Cognitive Complexity per Function (S)"

    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        sns.regplot(
            data=data,
            x="cyclo_fn_s",
            y="cog_fn_s",
            ax=axis,
            **configure_regression_style("#d62728"),
        )
        axis.set_xlabel("Cyclomatic Complexity / Fn")
        axis.set_ylabel("Cognitive Complexity / Fn")
        self._apply_common_style(axis)