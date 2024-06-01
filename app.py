from flask import Flask, render_template, request
from FeatureExtraction.feature import *
from FeatureExtraction.visualise import *
import pickle
import numpy as np

app = Flask(__name__)

with open('RandomForestModel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        file = request.files['file']
        data = get_Iq_Id(file)
        data1 = get_features(data, data['IQ'], data['ID'])
        data2 = get_array(data1)

        output = model.predict(data2)
        dic = {'healthy_data':"No Switch is open", 'open1':"1st Switch is Open", 'open2':"2nd Switch is Open",'open3':"3rd Switch is Open",
               'open4':"4th Switch is Open", 'open5':"5th Switch is Open", 'open6':"6th Switch is Open", 'open12':"Switch 1st and 2nd is Open", 
               'open13':"Switch 1st and 4th is Open", 'open14':"Switch 1st and 4th is Open",'open15':"Switch 1st and 5th is Open", 'open16':"Switch 1st and 6th is Open"}
        if output[0] in dic:
            outputs = dic[output[0]]

        
        plot_url= generate_plot1(file)
        plot_iqid= generate_plot2(data)
        plot= generate_plot3(data,data1)
        return render_template('index.html', message=outputs, plot_url=plot_url, plot_iqid=plot_iqid, plot=plot)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)