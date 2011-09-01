from pygooglechart import Axis, ScatterChart
from random import seed,randrange


def colors(points):
    c = []
    for i in xrange(len(points)):
        seed(i)
        c = c + ["%.2X%.2X%.2X" % (randrange(0, 255),
                                   randrange(0, 255), randrange(0, 255))]
    return c


def compass_url(points, width=500, height=500):
    legend = lambda p: map(lambda x: x[0], p)
    data_x = lambda p: map(lambda x: float(x[1]), p)
    data_y = lambda p: map(lambda x: float(x[2]), p)
    
    chart = ScatterChart(width, height, x_range=(-10, 10), y_range=(-10, 10))
    chart.add_data(data_x(points))
    chart.add_data(data_y(points))
    chart.set_legend(legend(points))
    chart.set_legend_position('b')
    chart.set_grid(5, 5, 5, 3)
    chart.set_colours_within_series(colors(points))
    
    axis = (chart.set_axis_labels(Axis.LEFT, ['Left']),
            chart.set_axis_labels(Axis.RIGHT, ['Right']),
            chart.set_axis_labels(Axis.TOP, ['Authoritarian']),
            chart.set_axis_labels(Axis.BOTTOM, ['Libertarian']))
    
    for a in axis:
        chart.set_axis_positions(a, [50])
        chart.set_axis_style(a, '000000', '15')

        url_bits = ['%s,%s' % (a, '-180') for a in axis]
        url = chart.get_url()
        url = url + '&chxtc=' + '|'.join(url_bits)
    return url
