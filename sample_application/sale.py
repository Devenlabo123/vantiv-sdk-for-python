from vantivsdk import *
import cgi
from flask.globals import request
form = cgi.FieldStorage()
searchterm =  form.getvalue('Report_Group')
print('strating sale.py')
conf = utils.Configuration()

transaction = fields.sale()
transaction.reportGroup = form.getvalue('Report_Group')
transaction.orderId = form.getvalue('Order_ID')
transaction.amount = form.getvalue('Amount')
transaction.orderSource = form.getvalue('Order_Source')
transaction.id = form.getvalue('ID')

card = fields.cardType()
card.number = form.getvalue('Card_Number')
card.expDate = form.getvalue('Exp_Date')
card.type = "MC"

transaction.card = card

response = online.request(transaction, conf)

response['saleResponse']['response']