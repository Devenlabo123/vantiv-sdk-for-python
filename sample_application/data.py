from vantivsdk import *

def processAuth(result, conf):
    authorization = fields.authorization()
    authorization.reportGroup = result['auth_report_group']
    authorization.orderId = result['order_id']
    authorization.amount = result['auth_amount']
    authorization.orderSource = result['auth_order_source']
    authorization.id = result['auth_id']

    card = fields.cardType()
    card.number = result['card_number']
    card.expDate = result['exp_date']
    card.type = result['card_type']

    authorization.card = card
    

    response = online.request(authorization, conf)
    return response

def processCapture(result, conf):
    transactions = fields.capture()
    transactions.reportGroup = result['capture_report_group']
    transactions.cnpTxnId= result['cnp_txn_id']
    transactions.amount = result['capture_amount']
    transactions.payPalNotes= result['paypal_notes']
    transactions.orderSource = result['capture_order_source']
    transactions.pin = result['pin']
    transactions.id = result['capture_id']

    response = online.request(transactions, conf)
    return response


def getConfig(result):
    conf = utils.Configuration()
    conf.url = result['url']
    conf.multiSiteUrl1 = result['url']
    conf.multiSiteUrl2 = result['url']
    conf.proxy = result['proxy']
    conf.user = result['user']
    conf.password = result['password']
    conf.merchantId = result['merchant_id']
    return conf



    