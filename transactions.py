import ecdsa as EC
from base64 import b64encode, b64decode

#TODO: Get running up on another machine
class Transaction:
    def __init__(self, sender, recipient, amount, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {
            "sender": b64encode(self.sender).decode(),
            "recipient": b64encode(self.recipient).decode(),
            "amount": self.amount,
            "signauture": b64encode(self.signaute)
            }

    def verified_signature(self):
        verification_key = self.send_public_key
        try:
           verification_key.verify(signature=self.signature, data=str(self.raw_transaction).encode())
        except EC.BadSignatureError:
           return False
        return True

    def create_signature(self, private_key: EC.SigningKey):
        transaction_data = self.raw_transaction
        sender_verifying_key = EC.VerifyingKey.from_string(transaction_data.get('sender'))

        if sender_verifying_key != private_key.get_verifying_key():
            raise ValueError('SigningKey is invalid')
        self.signature = self.sign(private_key)

    def sign(self, private_key: EC.SigningKey):
        transaction_data = str(self.raw_transaction).encode()
        return private_key,sign(transaction_data)

    def sender_public_key(self) -> EC.VerifyingKey:
        public_key = EC.VerifyingKey.from_string(self.sender)
        return public_key

    def raw_transaction(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}

    def from_dict(cls, sender, recipient, amount, signature):
        sender = b64decode(sender)
        recipient = b64decode(recipient)
        signature = b64decode(signature)
        return Transaction(sender, recipient, amount, signature)
