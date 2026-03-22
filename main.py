from __future__ import annotations

import argparse
from pathlib import Path

from analysis_app.data_loader import load_analysis_dataframe
from analysis_app.plot_base import PlotContext
from analysis_app.plots import (
    CogFnDiffPlot,
    CogVsCycloSPlot,
    CogVsCycloSTPlot,
    CycloFnDiffPlot,
    FuncDiffPlot,
)


class AnalysisRunner:
    def __init__(self, input_path: Path, output_dir: Path) -> None:
        self.input_path = input_path
        self.output_dir = output_dir
        self.plot_jobs = [
            CycloFnDiffPlot(),
            CogFnDiffPlot(),
            CogVsCycloSPlot(),
            CogVsCycloSTPlot(),
            FuncDiffPlot(),
        ]

    def run(self) -> list[Path]:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        data = load_analysis_dataframe(self.input_path)
        context = PlotContext(data=data, output_dir=self.output_dir)
        return [job.render(context) for job in self.plot_jobs]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate seaborn analysis charts from the Notion export JSON."
    )
    parser.add_argument(
        "--input",
        default="all.json",
        help="Path to the source JSON file.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where chart images will be saved.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    runner = AnalysisRunner(
        input_path=Path(args.input),
        output_dir=Path(args.output_dir),
    )
    output_paths = runner.run()

    print("Generated charts:")
    for path in output_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()