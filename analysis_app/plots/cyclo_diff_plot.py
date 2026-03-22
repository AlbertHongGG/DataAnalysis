from __future__ import annotations

import seaborn as sns
from matplotlib.axes import Axes
import pandas as pd

from analysis_app.plot_base import PlotJob, configure_regression_style


class CycloFnDiffPlot(PlotJob):
    file_name = "01_cyclo_fn_diff_vs_project_id.png"
    title = "Cyclomatic Complexity Difference"

    def draw(self, axis: Axes, data: pd.DataFrame) -> None:
        sns.regplot(
            data=data,
            x="row_id",
            y="cyclo_fn_diff",
            ax=axis,
            **configure_regression_style("#1f77b4"),
        )
        axis.set_xlabel("Project ID")
        axis.set_ylabel("[Cyclo/Fn] Diff")
        axis.set_xticks(data["row_id"])
        self._apply_common_style(axis)