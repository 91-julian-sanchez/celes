import unittest
from datetime import date
from unittest.mock import MagicMock, patch
import pandas as pd

from services.sales_service import SalesService


class TestSalesService(unittest.TestCase):

    @patch('services.sales_service.SalesRepository.get_sales_by_employee')
    def test_get_sales_by_employee(self, mock_get_sales_by_employee):
        mock_get_sales_by_employee.return_value = pd.DataFrame({
            'KeyEmployee': ['1', '1'],
            'KeyDate': ['2024-06-01', '2024-06-02'],
            'Qty': [10, 5],
            'Amount': [100.0, 50.0]
        })

        result = SalesService.get_sales_by_employee('1', date(2024, 6, 1), date(2024, 6, 2))

        self.assertEqual(result, {
            'employee': '1',
            'TotalQty': 15,
            'TotalAmount': 150.0
        })

    @patch('services.sales_service.SalesRepository.get_sales_by_product')
    def test_get_sales_by_product(self, mock_get_sales_by_product):
        mock_get_sales_by_product.return_value = pd.DataFrame({
            'KeyProduct': ['A', 'A'],
            'KeyDate': ['2024-06-01', '2024-06-02'],
            'Qty': [10, 5],
            'Amount': [100.0, 50.0]
        })

        result = SalesService.get_sales_by_product('A', date(2024, 6, 1), date(2024, 6, 2))

        self.assertEqual(result, {
            'product': 'A',
            'TotalQty': 15,
            'TotalAmount': 150.0
        })

    @patch('services.sales_service.SalesRepository.get_sales_by_store')
    def test_get_sales_by_store(self, mock_get_sales_by_store):
        mock_get_sales_by_store.return_value = pd.DataFrame({
            'KeyStore': ['X', 'X'],
            'KeyDate': ['2024-06-01', '2024-06-02'],
            'Qty': [10, 5],
            'Amount': [100.0, 50.0]
        })

        result = SalesService.get_sales_by_store('X', date(2024, 6, 1), date(2024, 6, 2))

        self.assertEqual(result, {
            'store': 'X',
            'TotalQty': 15,
            'TotalAmount': 150.0
        })


if __name__ == '__main__':
    unittest.main()
