from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
with open('model_pickle', 'rb') as f:
    model,vectorizer = pickle.load(f)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    text = request.form['text_field']
    text = [text]
    text_vectorizer=vectorizer.transform(text)
    output = model.predict(text_vectorizer)
    if(output == 1):
        return render_template('index.html', prediction_text='It is a spam message')
    else: 
        return render_template('index.html', prediction_text='It is not a spam message')
if __name__=="__main__":
    app.run(debug=True)