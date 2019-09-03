import csv
import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/abatements.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    # print(type(csv_obj))
    csv_list = list(csv_obj)
    return csv_list


@app.template_filter()
def numberFormat(value):
    return '$' + format(int(value), ',d')


@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    total = sum(int(i['abatement_value']) for i in object_list)
    format_str = '%d-%b-%Y'
    ap_format_str ='%B %d, %Y'
    dates = []
    for i in range(len(object_list)):
        datetime_obj = datetime.datetime.strptime(object_list[i]['date_of_status'], format_str)
        dates.append(datetime_obj)
    latest_item = (max(dates))
    latest_item = latest_item.strftime(ap_format_str)
    return render_template(template, object_list=object_list, total=total, latest_item=latest_item)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

