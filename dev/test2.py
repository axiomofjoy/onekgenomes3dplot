import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import numpy as np

x0 = np.random.normal(2, 0.4, 400)
y0 = np.random.normal(2, 0.4, 400)
x1 = np.random.normal(3, 0.6, 600)
y1 = np.random.normal(6, 0.4, 400)
x2 = np.random.normal(4, 0.2, 200)
y2 = np.random.normal(4, 0.4, 200)

trace0 = go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
    marker=dict(color='#835AF1')
)
trace1 = go.Scatter(
    x=x1,
    y=y1,
    mode='markers',
    marker=dict(color='#7FA6EE')
)
trace2 = go.Scatter(
    x=x2,
    y=y2,
    mode='markers',
    marker=dict(color='#B8F7D4')
)
data = [trace0, trace1, trace2]

cluster0 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x0), y0=min(y0),
                 x1=max(x0), y1=max(y0),
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
cluster1 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x1), y0=min(y1),
                 x1=max(x1), y1=max(y1),
                 opacity=.25,
                 line=dict(color='#7FA6EE'),
                 fillcolor='#7FA6EE')]
cluster2 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x2), y0=min(y2),
                 x1=max(x2), y1=max(y2),
                 opacity=.25,
                 line=dict(color='#B8F7D4'),
                 fillcolor='#B8F7D4')]

updatemenus = list([
    dict(buttons=list([
            dict(label = 'None',
                 method = 'relayout',
                 args = ['shapes', []]),
            dict(label = 'Cluster 0',
                 method = 'relayout',
                 args = ['shapes', cluster0]),
            dict(label = 'Cluster 1',
                 method = 'relayout',
                 args = ['shapes', cluster1]),
            dict(label = 'Cluster 2',
                 method = 'relayout',
                 args = ['shapes', cluster2]),
            dict(label = 'All',
                 method = 'relayout',
                 args = ['shapes', cluster0+cluster1+cluster2])
        ]),
    ),
    dict(buttons=list([
            dict(label = 'None',
                 method = 'restyle',
                 args = ['visible', ['legendonly', 'legendonly', 'legendonly']]),
            dict(label = 'Cluster 0',
                 method = 'restyle',
                 args = ['visible', [True, 'legendonly', 'legendonly']]),
            dict(label = 'Cluster 1',
                 method = 'restyle',
                 args = ['visible', ['legendonly', True, 'legendonly']]),
            dict(label = 'Cluster 2',
                 method = 'restyle',
                 args = ['visible', ['legendonly', 'legendonly', True]]),
            dict(label = 'All',
                 method = 'restyle',
                 args = ['visible', [True, True, True]])
        ]),
         y=0.8
    )
])

layout = dict(title='Highlight Clusters',
              showlegend=True,
              updatemenus=updatemenus,
              xaxis={'range': [0, 6]},
              yaxis={'range': [0, 8]})

fig = dict(data=data, layout=layout)
plot(fig)
