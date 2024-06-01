import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, output_file, save
import pandas as pd
import os



# def generate_plot1(data):

#     df = pd.read_excel(data)
    

#     #plot current data
#     plt.figure(figsize=(15, 6))
#     plt.plot(df.iloc[:,0])
#     plt.plot(df.iloc[:,1])
#     plt.plot(df.iloc[:,2])
#     plt.title('Representation of Current Data')
#     plot_filename = 'plot.png'
#     plot_path = os.path.join('static', plot_filename)
#     plt.savefig(plot_path)


#     #plot iqid data
    

#     plot_url = f'/static/{plot_filename}'
#     return plot_url

def generate_plot1(data):
    df = pd.read_excel(data)
    
    # Create a new plot with a title and axis labels
    p = figure(title="Representation of Current Data", x_axis_label='Index', y_axis_label='Value')
    
    # Add line renderers with legend and line thickness
    p.line(df.index, df.iloc[:,0], legend_label='IA', line_width=2, color='blue')
    p.line(df.index, df.iloc[:,1], legend_label='IB', line_width=2, color='red')
    p.line(df.index, df.iloc[:,2], legend_label='IC', line_width=2, color='green')
    
    # Save the plot as an HTML file
    plot_filename = 'plot.html'
    plot_path = os.path.join('static', plot_filename)
    output_file(plot_path)
    save(p)
    
    plot_url = f'/static/{plot_filename}'
    return plot_url


def generate_plot2(data):

    plt.figure(figsize=(5, 5))
    plt.plot(data.iloc[:,3],data.iloc[:,4])
    plt.title('Representation of IQ and ID')    
    filename = 'plot1.png'
    plot_path = os.path.join('static', filename)
    plt.savefig(plot_path)

    
    plot_iqid = f'/static/{filename}'
    return plot_iqid

def generate_plot3(data,data1):

    plt.figure(figsize=(5, 5))
    plt.plot(data.iloc[:,3],data.iloc[:,4], c='yellow')
    plt.scatter(data1.iloc[0,0], data1.iloc[0,1], c='red', marker='x', label='Midpoint')
    plt.scatter(data1.iloc[0,2], data1.iloc[0,3], c='red', marker='x', label='Midpoint')
    plt.scatter(data1.iloc[0,4], data1.iloc[0,5], c='red', marker='x', label='Midpoint')
    plt.scatter(data1.iloc[0,6], data1.iloc[0,7], c='red', marker='x', label='Midpoint')
    plt.scatter(data1.iloc[0,8], data1.iloc[0,9], c='red', marker='x', label='Midpoint')
    plt.title('Representation of IQ and ID')    
    filename = 'plot2.png'
    plot_path = os.path.join('static', filename)
    plt.savefig(plot_path)

    
    plot = f'/static/{filename}'
    return plot