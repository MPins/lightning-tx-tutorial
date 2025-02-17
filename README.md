# lightning-tx-tutorial

This repo contains a series of python jupyter-notebooks to explain how lightning transactions are created. The notebooks will start up an instance of bitcoind in regtest mode so that transactions can be validated and broadcasted on regtest.

## Prerequisite knowledge
- A high level understanding of the bitcoin. e.g. [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook), in particular [Chapter 6](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch06.asciidoc).
- A conceptual understanding of [hash functions](https://www.thesslstore.com/blog/what-is-a-hash-function-in-cryptography-a-beginners-guide).
- [Hexadecimal notation](https://inst.eecs.berkeley.edu/~cs61bl/r//cur/bits/decimal-binary-hex.html?topic=lab28.topic&step=2&course=) and [endianness](https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/).
- A high level understanding of the lightning e.g. [Mastering Lightning Network](https://github.com/lnbook/lnbook), in particular [Chapter7](https://github.com/lnbook/lnbook/blob/develop/07_payment_channels.asciidoc), [Chapter 8](https://github.com/lnbook/lnbook/blob/develop/08_routing_htlcs.asciidoc) and [Chapter 9](https://github.com/lnbook/lnbook/blob/develop/09_channel_operation.asciidoc).

## Chapter

+ Chapter 0: [Key Derivation](https://github.com/MPins/lightning-tx-tutorial/blob/master/Chapter%200%20-%20Key%20Derivation)
+ Chapter 1: [Funding Transaction](https://github.com/MPins/lightning-tx-tutorial/blob/master/Chapter%201%20-%20Funding%20Transaction)
+ Chapter 2: [Commitment Transaction](https://github.com/MPins/lightning-tx-tutorial/blob/master/Chapter%202%20-%20Commitment%20Transactions)
+ Chapter 3: [Closing Transaction](https://github.com/MPins/lightning-tx-tutorial/blob/master/Chapter%203%20-%20Closing%20Transaction)
 
## Setup
### Python3
This project requires Python 3.6 (or greater) to be [installed](https://www.python.org/downloads/) on your machine already. All other dependencies will be installed automatically with pip3.

To verify your Python version, run
```sh
python3 --version
```
If it is properly installed, you should see something like:
```sh
Python 3.9.13
```

To copy the repository to your local machine you can download the files directly from [GitHub](https://github.com/MPins/lightning-tx-tutorial), there are no further dependencies on `git`.

```sh
git clone https://github.com/MPins/lightning-tx-tutorial
cd lightning-tx-tutorial
```

To create a virtual environment and install all dependencies:
```sh
python3 -m venv myenv
source myenv/bin/activate
pip install bip-utils base58 ecdsa
```

Finally, to launch the interactive notebook:
```sh
jupyter lab
```
### Bitcoin core
The notebooks in this repo use bitcoin core's `TestShell` from its test framework. The `TestShell` is used to create a local test instance of a bitcoin node (and blockchain) against which we can test our manually created transactions. The notebooks in this repo have been tested with [bitcoin core v24.0.1](https://github.com/bitcoin/bitcoin/releases/tag/v24.0.1).

## Acknowledgements
- A lot of the code and inspiration for this tutorial comes from the following places:
  - Darius Parvin's [bitcoin-tx-tutorial](https://github.com/chaincodelabs/bitcoin-tx-tutorial)
  - Jimmy Song's [Programming Bitcoin exercises](https://github.com/jimmysong/pb-exercises).
