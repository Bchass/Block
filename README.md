# Block
Blockchain has been getting a lot of popularity lately as people see it as the "future" of currency. This repo is exactly that. Implemented a blockchain with Flask and using Argon2d for hashing (much better than Scrypt). There are three flavors of Argon2, though in the original paper (linked below), it's suggested Argon2d is recommended for crypto, but Argon2id has shown better results when measuring the current environment running `100 times` (this will differ with different environments) with argon2-cffi.

-----

### Reading material:
- Bitcoin: https://bitcoin.org/bitcoin.pdf
- Argon2: https://www.password-hashing.net/argon2-specs.pdf
- PoW: https://en.wikipedia.org/wiki/Hashcash?ref=hackernoon.com
- Consensus: https://www.researchgate.net/publication/330880555_Consensus_Algorithms_in_Blockchain_Comparative_Analysis_Challenges_and_Opportunities
- argon2-cffi: https://argon2-cffi.readthedocs.io/en/stable/cli.html
- ecdsa: https://www.cs.miami.edu/home/burt/learning/Csc609.142/ecdsa-cert.pdf

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

(Argon2 parameters)
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

(ecsda parameters with gmpy2)
```
siglen    keygen   keygen/s      sign     sign/s    verify   verify/s  no PC verify  no PC verify/s
        NIST192p:     48   0.00020s   4896.05   0.00022s   4539.08   0.00040s   2488.49       0.00085s        1177.47
        NIST224p:     56   0.00026s   3914.07   0.00027s   3728.40   0.00050s   1987.71       0.00106s         944.28
        NIST256p:     64   0.00028s   3519.21   0.00030s   3313.72   0.00058s   1717.35       0.00121s         825.27
        NIST384p:     96   0.00048s   2062.38   0.00050s   1983.13   0.00097s   1035.16       0.00211s         472.93
        NIST521p:    132   0.00086s   1167.88   0.00088s   1142.15   0.00174s    576.16       0.00378s         264.49
       SECP256k1:     64   0.00029s   3508.38   0.00030s   3346.74   0.00055s   1832.90       0.00117s         853.35
 BRAINPOOLP160r1:     40   0.00017s   5737.02   0.00019s   5309.18   0.00035s   2838.45       0.00071s        1410.32
 BRAINPOOLP192r1:     48   0.00021s   4848.52   0.00022s   4565.43   0.00041s   2411.63       0.00084s        1194.92
 BRAINPOOLP224r1:     56   0.00026s   3913.12   0.00027s   3767.25   0.00048s   2080.59       0.00152s         656.56
 BRAINPOOLP256r1:     64   0.00035s   2891.04   0.00034s   2933.36   0.00061s   1650.34       0.00129s         775.78
 BRAINPOOLP320r1:     80   0.00042s   2409.02   0.00040s   2513.19   0.00076s   1311.25       0.00167s         597.24
 BRAINPOOLP384r1:     96   0.00049s   2033.40   0.00050s   1993.90   0.00097s   1032.34       0.00220s         455.23
 BRAINPOOLP512r1:    128   0.00076s   1311.02   0.00077s   1296.79   0.00156s    641.41       0.00341s         292.83
       SECP112r1:     28   0.00011s   9406.58   0.00012s   8528.14   0.00020s   4903.17       0.00043s        2350.81
       SECP112r2:     28   0.00010s   9533.88   0.00012s   8552.52   0.00020s   4882.94       0.00041s        2418.49
       SECP128r1:     32   0.00012s   8309.43   0.00013s   7539.98   0.00023s   4255.48       0.00048s        2062.45
       SECP160r1:     42   0.00018s   5689.90   0.00019s   5326.23   0.00034s   2912.27       0.00074s        1354.65

                       ecdh     ecdh/s
        NIST192p:   0.00063s   1578.83
        NIST224p:   0.00079s   1273.70
        NIST256p:   0.00092s   1085.46
        NIST384p:   0.00159s    629.04
        NIST521p:   0.00278s    359.67
       SECP256k1:   0.00087s   1145.03
 BRAINPOOLP160r1:   0.00054s   1842.28
 BRAINPOOLP192r1:   0.00063s   1575.01
 BRAINPOOLP224r1:   0.00083s   1201.55
 BRAINPOOLP256r1:   0.00090s   1113.56
 BRAINPOOLP320r1:   0.00124s    808.11
 BRAINPOOLP384r1:   0.00159s    627.77
 BRAINPOOLP512r1:   0.00258s    387.35
       SECP112r1:   0.00030s   3296.98
       SECP112r2:   0.00030s   3306.87
       SECP128r1:   0.00035s   2820.61
       SECP160r1:   0.00052s   1924.27
```


-----
### Acknowledgments
- Tutorials: 
   - https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
