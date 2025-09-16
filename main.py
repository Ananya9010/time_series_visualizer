# This entrypoint file is used in development. Start by reading README.md
import time_series_visualizer
from unittest import main

# Test your functions by calling them here
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Run unit tests automatically
if __name__ == "__main__":
    main(module="test_module", exit=False)
