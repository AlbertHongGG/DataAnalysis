from __future__ import annotations

import seaborn as sns
from matplotlib.axes import Axes
import pandas as pd

from analysis_app.plot_base import PlotJob, configure_regression_style


class FuncDiffPlot(PlotJob):
    file_name = "05_func_diff_vs_project_id.png"
    title = "Function Difference"

    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        sns.regplot(
            data=data,
            x="row_id",
            y="func_diff",
            ax=axis,
            **configure_regression_style("#2ca02c"),
        )
        axis.set_xlabel("Project ID")
        axis.set_ylabel("[Func] Diff")
        axis.set_xticks(data["row_id"])
        self._apply_common_style(axis)