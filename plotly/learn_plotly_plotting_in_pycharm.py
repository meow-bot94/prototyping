import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import sklearn.datasets


print(f'default renderer: {plotly.io.renderers.default}')
# plotly.io.renderers.default = 'browser'
wine_data = sklearn.datasets.load_wine()
wine_df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
wine_df["Target"] = wine_data.target

scatter_plot = px.scatter(
    wine_df,
    x='alcohol',
    y='malic_acid',
    title='alcohol vs malic acid',
)
scatter_plot.show()

scatter_plot.show()
