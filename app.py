from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"] )
def paid():
    print("💰거스름돈 계산기💰")

    if request.method == "POST" :
        print("😊POST 접근😊")       
        total = request.form.get('total')
        paid = request.form.get('paid')
        print("total:", total)
        print("paid: ", paid)
        amount = int(paid) - int(total)
        print("amount: ", amount)
        
        if amount < 0 :
            error ="🔥금액을 더 지불하지 않을래?🔥"
            return render_template("index.html", error=error)
        
        else:
            COIN_500 = 500
            COIN_100 = 100
            COIN_50 = 50
            COIN_10 = 10

            coin500 = amount // COIN_500
            coin500_nmg = amount % COIN_500
            coin100 = coin500_nmg // COIN_100
            coin100_nmg = coin500_nmg % COIN_100
            coin50 = coin100_nmg // COIN_50
            coin50_nmg = coin100_nmg % COIN_50
            coin10 = coin50_nmg // COIN_10     
            return render_template('index.html', 
                                   total=total, paid=paid, coin500=coin500, coin100=coin100, coin50=coin50, coin10=coin10, amount=amount)

    else:
         print("😊GET 접근😊")
         return render_template('index.html')
    
if __name__ == "__main__": app.run(debug=True)