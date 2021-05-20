from blockchain import *
import unittest

class BlockchainTestCase(unittest.TestCase):
    def test_status(self):
        self.blockchain = bc
        self.blockchain = block
    
    def test_new_block(self,proof=1234, previous_hash='xyz'):
        self.blockchain = bc.create_block(proof,previous_hash)

    # Just to prove that the genesis block is randomized each time for a new chain
    def test_genesis_block(self):
        self.blockchain = block.genesis_block = random.randint(0,100)
    
    def test_transactions(self, sender='x', recipient='y', amount=1):
        self.blockchain = bc.new_transactions(
            sender=sender,
            recipient=recipient,
            amount=amount
            )

class TestBlock(BlockchainTestCase):
    def test_block(self):
        self.test_new_block()
        self.blockchain = bc
        Lblock = self.blockchain.last_block
                
        #TODO: Figure out previous_hash for Argon2
        assert len(self.blockchain.chain) == 3 
        assert Lblock['index'] == len(self.blockchain.chain)
        assert Lblock['timestamp'] != 0
        assert Lblock['proof'] == 1234
        assert Lblock['previous_hash'] == 0

    def test_new_transactions(self):
        self.test_transactions()
        self.blockchain = bc
        transaction = self.blockchain.current_transactions[-1]
        
        assert transaction
        assert transaction['sender'] == 'x'
        assert transaction['recipient'] == 'y'
        assert transaction['amount'] == 1



    
