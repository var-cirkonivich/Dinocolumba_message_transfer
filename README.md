　

# Introduction：

- This is an useless program to transmitting your message.

　

══════════════

# Instructions：

***(：For details, please refer to the latest version on the right!***

　
### •　Transmitting

 　- [socket](https://docs.python.org/3/howto/sockets.html)：
 ```python
import socket
 ```

 　- [subprocess](https://docs.python.org/3/library/subprocess.html)：
 ```python
import subprocess
 ```

 　- [ast](https://docs.python.org/3/library/ast.html)：
 ```python
import ast
 ```

　
### •　Encryption

 　- [Fernet](https://cryptography.io/en/latest/fernet/)：
 ```python
from cryptography.fernet import Fernet
 ```

 　- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) :
 ```python
def caesar_decrypt(text, shift)
# These are self-contained functions within the program, no need for imports.
 ```

 　- [Random](https://docs.python.org/3/library/random.html)：
 ```python
import random
 ```

 　- [nltk](https://pypi.org/project/nltk/)：
 ```python
import nltk
from nltk.corpus import words
 ```
　

══════════════

# VersionList：

| Version | Date | File | Content |
| --- | --- | --- | --- |
| v-1.0.0 | 23.08.22:17 | `Dinocolumba_send_I` `Dinocolumba_receive_I` | Designed the basic message transmission structure. |
| v-1.0.1 | 23.08.22:19 | `Dinocolumba_send_II` `Dinocolumba_receive_II` | Added encryption using the `Fernet` Symmetric-key algorithm method for basic security in message transmission. |
| v-1.0.2 | 23.08.23:17 | `Dinocolumba_send_IIi` `Dinocolumba_receive_IIi` | Added encryption using the `Caesar cipher` Substitution cipher method, scrambling both the public and private keys. |
| v-1.1.0 | 23.08.24:10 | `Dinocolumba_send_J` `Dinocolumba_receive_J` | Optimized the transmission process to support multiple message transmissions and removed `Fernet` for ease of future updates. |
| v-1.2.0 | 23.08.25:09 | `Dinocolumba_send_1.2.0` `Dinocolumba_receive_1.2.0` `Dinocolumba_commcode_I` `Dinocolumba_decode_I`| This program includes the addition of a feature to generate the `Communication code`, utilizing `Fernet` for Symmetric-key algorithm encryption and generating `key words`. |
　

══════════════

# Attention：

> [!IMPORTANT]
> - Please enter the correct IP address ( If it's a local machine, you can send the IP address as `localhost` ) .　 　 　 　 　
> - Please enter the correct `Communication code`, otherwise the program will close automatically ( Using the `Dinocolumba_commcode` program to create the Communication code ) .
> - Both parties must ensure to securely store the `Communication code`, otherwise the connection between the two parties will not be established.

> [!WARNING]
> - Please follow the instructions provided in the program's usage guide, otherwise errors may occur !
> - For detailed precautions, please refer to its version !

> [!NOTE]
> If you have any questions regarding this program, feel free to contact us for us to improve your experience.

　

══════════════

𝕄𝕒𝕕𝕖　𝕓𝕪： { _Лютомисл_Пахомав_ }, { _alexlorance129_ }

