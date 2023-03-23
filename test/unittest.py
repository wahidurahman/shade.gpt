# Test suite for transaction records match script

# Import the necessary modules and functions
import unittest
from transaction_records_match import match_transactions

class TestTransactionRecordsMatch(unittest.TestCase):

    # Test case for matching two identical transactions
    def test_matching_identical_transactions(self):
        transaction1 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Paycheck'}
        transaction2 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Paycheck'}
        self.assertTrue(match_transactions(transaction1, transaction2))

    # Test case for matching two transactions with different dates
    def test_matching_transactions_with_different_dates(self):
        transaction1 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Paycheck'}
        transaction2 = {'date': '2022-01-02', 'amount': 100.00, 'description': 'Paycheck'}
        self.assertFalse(match_transactions(transaction1, transaction2))

    # Test case for matching two transactions with different amounts
    def test_matching_transactions_with_different_amounts(self):
        transaction1 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Paycheck'}
        transaction2 = {'date': '2022-01-01', 'amount': 50.00, 'description': 'Paycheck'}
        self.assertFalse(match_transactions(transaction1, transaction2))

    # Test case for matching two transactions with different descriptions
    def test_matching_transactions_with_different_descriptions(self):
        transaction1 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Paycheck'}
        transaction2 = {'date': '2022-01-01', 'amount': 100.00, 'description': 'Bonus'}
        self.assertFalse(match_transactions(transaction1, transaction2))

if __name__ == '__main__':
    unittest.main()
