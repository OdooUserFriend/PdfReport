from odoo import api, fields, models, tools, _


class AccMove(models.Model):
    _inherit = "account.move"


    def convert_to_arabic(self, number):
        arabic_numbers = {
            '0': '٠',
            '1': '١',
            '2': '٢',
            '3': '٣',
            '4': '٤',
            '5': '٥',
            '6': '٦',
            '7': '٧',
            '8': '٨',
            '9': '٩'
            }
        return ''.join(arabic_numbers.get(digit, digit) for digit in str(number))

    def get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'convert_to_arabic': self.convert_to_arabic,
            }
