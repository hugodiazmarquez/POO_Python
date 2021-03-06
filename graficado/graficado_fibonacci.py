from bokeh.plotting import figure, output_file, show

def fibonacci(total_vals):
    i = 1
    if total_vals == 0:
        fib = []
    elif total_vals == 1:
        fib = [1]
    elif total_vals == 2:
        fib = [1,1]
    elif total_vals > 2:
        fib = [1,1]
        # print(fib)
        while i < (total_vals - 1):
            fib.append(fib[i] + fib[i-1])
            # print(fib)
            i += 1
    return fib

if __name__ == '__main__':
    output_file =('Graficado_simple.html')
    fig = figure()

    total_vals = int(input("¿cuantos valores?:"))
    x_value = list(range(total_vals))


    fig.line(x_value, fibonacci(total_vals), line_width=2)
    show(fig)
