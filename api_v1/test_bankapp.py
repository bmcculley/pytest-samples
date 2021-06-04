import requests

class TestBankApp():
	def test_deposit(self):
		r = requests.put('http://127.0.0.1:5000/v1/deposit/100')
		assert r.status_code == 200
		data = r.json()
		assert data['deposited'] == '100.00'

	def test_withdraw(self):
		r = requests.put('http://127.0.0.1:5000/v1/withdraw/50')
		assert r.status_code == 200
		data = r.json()
		assert data['withdrew'] == '50.00'

	def test_overdraw(self):
		r = requests.put('http://127.0.0.1:5000/v1/withdraw/51')
		assert r.status_code == 200
		data = r.json()
		assert data['withdrew'] == 'Insufficient balance.'

	def test_display(self):
		r = requests.get('http://127.0.0.1:5000/v1/display')
		assert r.status_code == 200
		data = r.json()
		assert data['balance'] == '50.00'