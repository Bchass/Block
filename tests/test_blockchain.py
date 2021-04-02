from blockchain import *
import unittest

class BlockchainTestCase(unittest.TestCase):
    def test_status(self):
        self.blockchain = bc
    
    def test_new_block(self,proof=1234, previous_hash='xyz'):
        self.blockchain = bc.create_block(proof,previous_hash)
    
    def test_new_transactions(self, sender='x', recipient='y', amount='z'):
        self.blockchain = bc.new_transactions(
            sender=sender,
            recipient=recipient,
            amount=amount
            )