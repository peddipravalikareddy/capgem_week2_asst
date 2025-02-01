#12
#Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`,
#  `PayPalPayment`, and `BitcoinPayment` that override the method differently.

class Payment:
    def process_payment(self):
        print("Process payment is still pending...")
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using credit card")
class PayPalPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using PayPal")
class BitcoinPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using Bitcoin")
creditcard = CreditCardPayment()
creditcard.process_payment()
paypal = PayPalPayment()
paypal.process_payment()
bitcoin = BitcoinPayment()
bitcoin.process_payment()
