import pandas as pd
import numpy as np
import plotly
import bokeh
import holoviews
# import hvplot.pandas
import sklearn.datasets


holoviews.extension('bokeh')
pd.set_option("display.max_columns", 30)


wine_data = sklearn.datasets.load_wine()
wine_df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
wine_df["Target"] = wine_data.target

scatter_plot = holoviews.Scatter(
    wine_df,
    kdims='alcohol',
    vdims='malic_acid',
    label='alcohol vs malic acid',
)

from bokeh.plotting import show
from IPython.display import display_html
show(holoviews.render(scatter_plot))
