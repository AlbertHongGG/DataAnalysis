from __future__ import annotations

import seaborn as sns
from matplotlib.axes import Axes
import pandas as pd

from analysis_app.plot_base import PlotJob, configure_regression_style


class CogFnDiffPlot(PlotJob):
    file_name = "02_cog_fn_diff_vs_project_id.png"
    title = "Cognitive Complexity Difference"

    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        sns.regplot(
            data=data,
            x="row_id",
            y="cog_fn_diff",
            ax=axis,
            **configure_regression_style("#2ca02c"),
        )
        axis.set_xlabel("Project ID")
        axis.set_ylabel("[Cog/Fn] Diff")
        axis.set_xticks(data["row_id"])
        self._apply_common_style(axis)