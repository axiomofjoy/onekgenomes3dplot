from plotly.offline import plot
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

means = [[0,0,0], [1,2,1], [-1,0,1], [-1,1,-1]]
colors = ['rgb(124, 252, 0)', 'rgb(30, 144, 255)', 'rgb(220, 20, 60)', 'rgb(255, 69, 0)']

data = list()
for mean, color in zip(means, colors):
    x, y, z = np.random.multivariate_normal(np.array(mean), np.eye(3), 20).transpose()
    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            color=color,
            size=12,
            opacity=0.8
        )
    )
    data.append(trace)

layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

button_layer_1_height = 1.12
button_layer_2_height = 1.065

updatemenus=list([
    dict(
        buttons=list([
            dict(
                args=[{'visible': [True, False, False, False]}],
                label='Button 1',
                method='restyle'
            ),
            dict(
                args=[{'visible': [False, True, False, False]}],
                label='Button 2',
                method='restyle'
            ),
        ]),
        direction = 'left',
        pad = {'r': 10, 't': 10},
        showactive = True,
        type = 'buttons',
        x = 0.1,
        xanchor = 'left',
        y = button_layer_1_height,
        yanchor = 'top'
    ),
    dict(
        buttons=list([
            dict(
                args=[{'visible': [False, False, True, False]}],
                label='Button A',
                method='restyle'
            ),
            dict(
                args=['visible', [False, False, False, True]],
                label='Button B',
                method='restyle'
            )
        ]),
        direction = 'left',
        pad = {'r': 10, 't': 10},
        showactive = True,
        type = 'buttons',
        x = 0.1,
        xanchor = 'left',
        y = button_layer_2_height,
        yanchor = 'top'
    ),
])

layout['updatemenus']=updatemenus
fig = go.Figure(data=data, layout=layout)
plot(fig, filename='localtest.html')
