from flask import Blueprint, render_template, request, redirect, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, add_transaction, get_transactions
from app.payments import process_payment
from app.exchange import convert_currency
from app.qr import generate_qr, read_qr
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html', user=current_user)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username', '').strip()
        email = data.get('email')
        password = data.get('password', '').strip()
        currency = data.get('currency', '').strip()
        if not username or not email or not password:
            return jsonify({'success': False,'error': 'Missing required fields'})
        if User.get_by_username(username):
            return jsonify({'success': False, 'error': 'Username already exists'})
        user = User.create(username, email, password, currency)
        if user:
            login_user(user)
            return jsonify({'success': True, 'message': 'User registered and logged in successfully'})
        else:
            return jsonify({'succeess': False, 'error': 'Registration failed'})
    return render_template('register.html', user=current_user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.get_by_username(username)
        if not user or not user.check_password(password):
            return jsonify({'success': False, 'message': 'Invalid credentials'})
        login_user(user)
        return jsonify({'success': True, 'message': 'Login successful'})
    if current_user.is_authenticated:
        return redirect('/')
    return render_template('login.html', user=current_user)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@main.route('/pay', methods=['GET', 'POST'])
@login_required
def pay():
    if request.method == 'POST':
        data = request.get_json()
        result = process_payment(data)
        if result.get('success'):
            add_transaction(
                user_id=current_user.id,
                amount=data['amount'],
                paid_to=current_user.username,
                date=datetime.now().isformat()
            )
        return jsonify(result)
    return render_template('pay.html', user=current_user)

@main.route('/exchange', methods=['GET', 'POST'])
@login_required
def exchange():
    data = request.get_json()
    result = convert_currency(data)
    return jsonify(result)

@main.route('/generate_qr', methods=['POST'])
@login_required
def generate():
    data = request.get_json()
    url = generate_qr(data['info'])
    return jsonify({'qr_url': url})

@main.route('/read_qr', methods=['POST'])
@login_required
def read():
    file = request.files['file']
    result = read_qr(file)
    return jsonify(result)

@main.route('/history')
@login_required
def history():
    transcations = get_transactions(current_user.id)
    if request.get('Accept') == 'application/json':
        return jsonify({'transactions': transcations})
    return render_template('history.html', user =  current_user, transactions=transcations)
