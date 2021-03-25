# Block
Blockchain has been getting a lot of popularity lately as people see it as the "future" of banking. This repo is exactly that. Implementing a blockchain with Flask and then plan on switching sha256 out with Scrypt(algo LTC uses; very efficient) and then scale it up to something bigger at some point maybe? Reading material includes papers on the algorithms in play and the first paper release on bitcoin and the brains behind it.

old_layout contains exactly how it's desribed, a glory hole of a mess of a layout with just a ton of bugs

new_layout contains a cleaned up space with no more bugs present

Reading material:
- Bitcoin: https://bitcoin.org/bitcoin.pdf
- Scrypt: https://www.tarsnap.com/scrypt/scrypt.pdf
- PoW: https://en.wikipedia.org/wiki/Hashcash?ref=hackernoon.com
- Consensus: https://www.researchgate.net/publication/330880555_Consensus_Algorithms_in_Blockchain_Comparative_Analysis_Challenges_and_Opportunities

-----
#### Interacting with the Blockchain

- Calling the chain: `curl http://127.0.0.1:5000/chain`
- Mining a block: `curl http://127.0.0.1:5000/mine`
- Adding a transaction: `curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "Enter address",
 "recipient": "Enter address", 
 "amount": 5
}' "http://localhost:5000/transactions/new"`
