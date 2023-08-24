　

# Introduction：

- This is an useless program to transmitting your message.
- File name format:    Dinocolumba_{ _send/receive_ }_{ _Version name_ }

　

══════════════

# Instructions：

***(：For details, please refer to the latest version on the right!***

　
### •　Transmitting

 　- We use [socket](https://docs.python.org/3/howto/sockets.html)：
 ```python
import socket
 ```

　
### •　Encryption

 　- We use [Fernet](https://cryptography.io/en/latest/fernet/)：
 ```python
from cryptography.fernet import Fernet
 ```

 　- And also use [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) :
 ```python
def caesar_decrypt(text, shift)
# These are self-contained functions within the program, no need for imports.
 ```

　

══════════════

# VersionList：

| Version | Date | File | Content |
| --- | --- | --- | --- |
| v-1.0.0 | 23.08.22:17 | `Dinocolumba_send_I` `Dinocolumba_receive_I` | Designed the basic message transmission structure. |
| v-1.0.1 | 23.08.22:19 | `Dinocolumba_send_II` `Dinocolumba_receive_II` | Added encryption using the `Fernet` Symmetric-key algorithm method for basic security in message transmission. |
| v-1.0.2 | 23.08.23:17 | `Dinocolumba_send_IIi` `Dinocolumba_receive_IIi` | Added encryption using the `Caesar cipher` Substitution cipher method, scrambling both the public and private keys. |
| v-1.1.0 | 23.08.24:10 | `Dinocolumba_send_J` `Dinocolumba_receive_J` | Optimized the transmission process to support multiple message transmissions and removed `Fernet` for ease of future updates. |
　

══════════════

# Attention：

> [!IMPORTANT]
> •　Please enter the correct IP address ( If it's a local machine, you can send the IP address as `localhost` ) .　 　 　 　 　
> •　Please enter the correct dynamic port number ( Please enter a positive integer between `1024` and `65535` ) .

> [!WARNING]
> Please follow the instructions provided in the program's usage guide, otherwise errors may occur !

> [!NOTE]
> If you have any questions regarding this program, feel free to contact us for us to improve your experience.

　

══════════════

𝕄𝕒𝕕𝕖　𝕓𝕪： { _Лютомисл_Пахомав_ }

