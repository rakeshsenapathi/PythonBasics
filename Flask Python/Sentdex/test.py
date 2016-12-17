from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph(chartID='chart_ID', chart_type='line', chart_height=500):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Label1', "data": [1, 2, 3]},
              {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


if(__name__ == "__main__"):
    app.run(debug=True)
