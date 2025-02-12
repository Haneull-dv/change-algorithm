from flask import Flask, render_template, request
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
    
    
if __name__ == "__main__": app.run(debug=True)