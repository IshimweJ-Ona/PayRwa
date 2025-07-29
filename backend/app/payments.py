import os
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def process_payment(data):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(data['amount']) * 100,
            currency=data['currency'],
            payment_method_types=["card"]
        )
        return {'success': True, 'client_secret': intent.client_secret}
    except Exception as e:
        return {'success': False, 'error': str(e)}
    