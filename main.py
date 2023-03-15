import requests
import csv
import time

with open('script_jakeonemobile_billpayment_s11.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row["tgltrx"]+','+row["jamtrx"]+','+row["jenistrx"])
        url = 'http://35.240.236.152:5080/api/cep/fds.bill_payment/response'

        data = '''{
                    "account_id" : "'''+row["user_profile_id"]+'''",
                    "transaction_amount" : '''+row["nilai"]+''',
                    "transaction_date" : "'''+row["tgltrx"]+'''",
                    "transaction_time" : "'''+row["jamtrx"]+'''",
                    "transaction_type" : "'''+row["jenistrx"]+'''",
                    "product_category" : "'''+row["tipetrx"]+'''",
                    "transaction_channel" : "'''+row["channel"]+'''",
                    "dest_phone_number" : "'''+row["destinationaccount"]+'''",
                    "transaction_status" : "'''+row["respon"]+'''",
                    "transaction_id" : "'''+row["transaction_id"]+'''",
                    "phone_number" : "'''+row["terminal"]+'''"
                }'''
        print(data)
        time.sleep(1)
        response = requests.post(url, data=data)
        print(response.text)