# Block
Blockchain has been getting a lot of popularity lately as people see it as the "future" of currency. This repo is exactly that. Implemented a blockchain with Flask and using Argon2d for hashing (much better than Scrypt). There are three flavors of Argon2, though in the original paper (linked below), it's suggested Argon2d is recommended for crypto, but Argon2id has shown better results when measuring the current environment running `100 times` (this will differ with different environments) with argon2-cffi.

-----

### Reading material:
- Bitcoin: https://bitcoin.org/bitcoin.pdf
- Argon2: https://www.password-hashing.net/argon2-specs.pdf
- PoW: https://en.wikipedia.org/wiki/Hashcash?ref=hackernoon.com
- Consensus: https://www.researchgate.net/publication/330880555_Consensus_Algorithms_in_Blockchain_Comparative_Analysis_Challenges_and_Opportunities
- argon2-cffi: https://argon2-cffi.readthedocs.io/en/stable/cli.html

-----
### Dependencies
- Python 3.8+ is recommended
- Flask

-----
### Interacting with the Blockchain

- Calling the chain: `curl http://127.0.0.1:5000/chain`

- Mining a block: `curl http://127.0.0.1:5000/mine`
- Creating new nodes: `curl http://127.0.0.1:5000/nodes/register`

- Adding a transaction: `curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "Enter address",
 "recipient": "Enter address", 
 "amount": 5 
}' "http://localhost:5000/transactions/new"`

- Resolve conflicts: `curl http://127.0.0.1:5000/nodes/resolve`

-----
### Environment
- MacBook Pro (13-inch, 2020):
- Processor: 1.4 Ghz Quad-Core Intel Core i5
- Memory: 8GB @ 2133 MHz

Benchmarks:
```
Best results:
M = 256 MB, T = 3, d = 16, Time = 0.946 s
M = 128 MB, T = 6, d = 16, Time = 0.96 s
M = 64 MB, T = 12, d = 16, Time = 0.902 s
M = 32 MB, T = 27, d = 16, Time = 1 s
M = 16 MB, T = 53, d = 16, Time = 0.999 s
M = 8 MB, T = 108, d = 16, Time = 0.993 s
M = 4 MB, T = 208, d = 16, Time = 0.989 s
M = 2 MB, T = 440, d = 16, Time = 0.996 s
M = 1 MB, T = 1024, d = 16, Time = 0.989 s
```

-----
### Acknowledgments
- Tutorials: 
   - https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
