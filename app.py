from flask import Flask, render_template, request
from com.haneull.bag.bag_controller import BagController
from com.haneull.bag.bag_model import BagModel
from com.haneull.exchange.exchange_controller import ExchangeController
from com.haneull.exchange.exchange_model import ExchangeModel



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dollar')
def exchange_dollar():
    return render_template('exchange_dollar.html')

@app.route('/won')
def exchange_won():
    return render_template('exchange_won.html')

@app.route('/exchange', methods=["POST", "GET"] )
def exchange():
    print("💲환전💲")
    if request.method == "POST" :
        print("😊POST 접근😊")
        currency = request.form.get('currency') #USD,WON 상수
        total = int(request.form.get('total'))
        print("currency: ", currency)
        print("total: ", total)

        controller = ExchangeController(total = total, currency = currency)
        resp: ExchangeModel = controller.get_result()
 
        render_html = '<h1>결과보기</h1>'
        render_html += resp.result

        if resp.currency == 'USD':
            return render_template("exchange_dollar.html", render_html = render_html)

        elif resp.currency == 'WIB':
            return render_template("exchange_won.html", render_html = render_html)
        
        else:
            print("잘못한 화폐단위입니다.")

    else:
        pass

@app.route('/bag', methods = ["POST", "GET"])
def bag():
    print("배낭")
    if request.method == "POST":
        print("😊POST 접근😊")
        total = int(request.form.get('total')) # 상수
        it_w1 = int(request.form.get('it_w1'))
        it_w2 = int(request.form.get('it_w2'))
        it_w3 = int(request.form.get('it_w3'))
        it_w4 = int(request.form.get('it_w4'))
        it_p1 = int(request.form.get('it_p1'))
        it_p2 = int(request.form.get('it_p2'))
        it_p3 = int(request.form.get('it_p3'))
        it_p4 = int(request.form.get('it_p4'))
        print("total: ", total)
        print("it_w1:", it_w1)
        print("it_p1:", it_p1)

        controller = BagController(total = total, it_w1 = it_w1, it_w2 = it_w2,
        it_w3 = it_w3, it_w4 = it_w4, it_p1 = it_p1, it_p2 = it_p2, it_p3 = it_p3, it_p4 = it_p4)
        resp: BagModel = controller.get_result()

        render_html = '<h1>결과보기</h1>'
        render_html += str(resp.total_profit)
        return render_template('bag/bag.html', render_html = render_html)
    
    else: 
        return render_template('bag/bag.html')
    
    
if __name__ == "__main__": app.run(debug=True)