import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import flask
import dash
from dash import dcc
from dash import html



#  Load data from CSV
df = pd.read_csv('customers-100.csv')

# Or fetch data from API (example)
'''response = requests.get('https://api.crossref.org/journals?query=pharmacy+health')
df = pd.DataFrame(response.json())'''




# Example: Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Id', y='Website', data=df)
plt.title('Customers Data')
plt.xlabel('Name of Customers')
plt.ylabel('Serial No')
plt.savefig('plot.png')  # Save plot as image file

'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render HTML template for dashboard

if __name__ == '__main__':
    app.run(debug=True)


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Dashboard Title'),
    dcc.Graph(id='example-graph', figure=your_figure_object),
])

if __name__ == '__main__':
    app.run_server(debug=True)'''
    
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Dashboard Title'),
    dcc.Graph(id='example-graph', figure={
        'data': [{'x': df['Customer Id'], 'y': df['Website'], 'type': 'bar'}],
        'layout': {'title': 'Customers Data'}
    }),
])

if __name__ == '__main__':
    app.run_server(debug=True)