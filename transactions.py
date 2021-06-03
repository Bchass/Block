import ecdsa as EC

class Transaction:
    def __init__(self, sender, recipient, amount, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def _dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "signauture": self.signaute
            }

    def verified_signature(self):
        unv_transaction = {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}
        verification_key = self.send_public_key
        try:
           verification_key.verify(message=raw_transaction, signature=self.signature)
        except EC.BadSignatureError:
           return False
        return True

    def send_public_key(self) -> EC.VerifyingKey:
       public_key = EC.VerifyingKey.from_string(self.sender)
       return public_key
