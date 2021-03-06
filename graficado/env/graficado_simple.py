from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file =('Graficado_simple.html')
    fig = figure()

    total_vals = int(input('cuantos valores'))
    x_value = list(range(total_vals))
    y_value = []

    for x in x_value:
        val = int(input(f'Valor Y para {x}'))
        y_value.append(val)

    fig.line(x_value, y_value, line_width=2)
    show(fig)