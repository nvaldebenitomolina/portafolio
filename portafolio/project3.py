from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar
import pandas as pd


def plot1():
    df = pd.read_csv('/home/nvaldebenito/Documentos/curriculum/portafolio/static/assets/data/project/project3/data_filter.csv')
    print(df['category'].value_counts().values)
    #plot_div = plot([Bar(x=df['category'].value_counts().index, y=df['category'].value_counts().values, offset='div')])
    final_data = [Bar(x=df['category'].value_counts().index, y=df['category'].value_counts().values)]
    plot_div = plot([Bar(x=df['category'].value_counts().index, y=df['category'].value_counts().values)], output_type='div')
    return plot_div