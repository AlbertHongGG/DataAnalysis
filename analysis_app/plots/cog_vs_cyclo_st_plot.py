from __future__ import annotations

import seaborn as sns
from matplotlib.axes import Axes
import pandas as pd

from analysis_app.plot_base import PlotJob, configure_regression_style


class CogVsCycloSTPlot(PlotJob):
    file_name = "04_cog_fn_st_vs_cyclo_fn_st.png"
    title = "Cyclomatic vs. Cognitive Complexity per Function (ST)"

    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        sns.regplot(
            data=data,
            x="cyclo_fn_st",
            y="cog_fn_st",
            ax=axis,
            **configure_regression_style("#228b22"),
        )
        axis.set_xlabel("Cyclomatic Complexity / Fn")
        axis.set_ylabel("Cognitive Complexity / Fn")
        self._apply_common_style(axis)