# coding: utf-8
from flask import Flask, request, render_template
from model.base import db_session

from model.order import Order

app = Flask(__name__)


@app.before_request
def pre():
    pass


@app.route('/')
def hello_world():
    return 'Hello escort!'


@app.route('/make_a_order', methods=['POST', 'GET'])
def make_a_order():
    if request.method == 'POST':
        # 从请求表单中创建变量
        title = request.form['title']
        describe = request.form['describe']
        money = request.form['money']
        send_time = request.form['send_time']
        paid_at = request.form['paid_at']
        location_x = request.form['location_x']
        location_y = request.form['location_y']
        progress = Order.progress_set['on']
        # 简单的订单创建逻辑,没有考虑恶意刷单,用户验证情况
        order = Order(title, describe, money, send_time,
                      paid_at, location_x, location_y, progress)
        db_session.add(order)
        db_session.commit()
        return render_template('result_create_order.html', result=True)
    if request.method == 'GET':
        return render_template('create_order.html')

if __name__ == '__main__':
    app.run(debug=True)
