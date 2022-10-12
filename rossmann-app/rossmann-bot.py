# Libraries
import json
import requests
import pandas as pd
from flask import Flask, request, Response
import os

#bot-token
TOKEN = '5641286371:AAGkJr5q8TFDLnEeEGl1YMnOWRu7I4-4-2k'

# Webhook was set
# https://api.telegram.org/bot5641286371:AAGkJr5q8TFDLnEeEGl1YMnOWRu7I4-4-2k/setWebhook?url=https://rossmann-telegram-app.onrender.com

def send_message(chat_id, text):    
    url  = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}' # adding TOKEN and chat_id to url
    r = requests.post(url, json={'text':text}) # concat url and text message
    print(f'Status Code {r.status_code}')
    return None

def load_dataset(store_id):
    # Loading data
    df10 = pd.read_csv('data/test.csv')
    df_store_raw = pd.read_csv('data/store.csv')

    # Merge test dataset + store
    df_test = pd.merge(df10, df_store_raw, how='left', on='Store')

    # Choose store for prediction
    df_test = df_test[df_test['Store']==store_id]
    
    if not df_test.empty:    
        # Remove closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1 )

        # Convert to json
        data = json.dumps(df_test.to_dict(orient='records'))    
    else:
        data = 'error'         
    return data

def predict(data):
    # API CALL
    url = 'https://rossmann-app.onrender.com/rossmann/predict' 
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post(url, data=data, headers=header)
    print(f'Status Code {r.status_code}')
   
    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())
    return d1 # predicts and return a df

def parse_message(message):
    chat_id = message['message']['chat']['iGd'] # getting the chat_id
    store_id = message['message']['text'] # getting the text message
        
    store_id = store_id.replace('/', '') # telegram requires '/' (e.g. /22, to choose store 22), hence the replacement
    
    try:
        store_id = int(store_id)
    except ValueError:
        store_id = 'error'
    return chat_id, store_id

# APP initialize
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        message = request.get_json()
                
        chat_id, store_id = parse_message(message)
        
        if store_id != 'error':
            # Loading Data
            data = load_dataset(store_id)
            
            if data != 'error':                          
                # Prediction
                d1 = predict(data)

                # Calculation
                d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()
                
                # Send Message
                msg = 'Store number {} will sell €{:,.2f} in the next 6 weeks'.format(d2['store'].values[0], d2['prediction'].values[0])

                send_message(chat_id, msg)
                return Response('Ok', status=200)   
            
            else:
                send_message(chat_id, 'Store not available')    
                return Response('Ok', status=200)
            
        else:
            send_message(chat_id, 'Please enter a valid Store ID')    
            return Response('Ok', status=200)
                    
    else:
        return '<h1> Rossmann Telegram Bot </h1>' # bot html header 
 
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)