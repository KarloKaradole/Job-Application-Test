"""
Select the statements qabout SSH key_based authentication that are correct:

a) All SHH key logins require a passphrase be used when logging into a server.
b) The -/.ssh/authorized_keys file can be modified to allow only specific users to login.
c) The -/.ssh/authorized_keys file contiants all authorized private keys.
d) The -/.ssh/known_hosts file can be used by a client to authenticate a server 
"""

"""

Here is the correct assessment of each statement regarding SSH key-based authentication:

a) Incorrect. Passphrases are optional when generating an SSH key pair. You can choose to have no passphrase, meaning the private key can be used without further authentication.
   Passphrases add an extra layer of security but are not mandatory.

b) Incorrect. The ~/.ssh/authorized_keys file is used to specify which public keys are authorized to log in to a particular user account on the server.
   However, it does not control which users can log in, only which keys are allowed for that specific user. User-based restrictions are typically handled through other means, such as system configurations or SSH settings like AllowUsers.

c) Incorrect. The ~/.ssh/authorized_keys file contains public keys, not private keys.
   It is used by the server to verify whether an incoming connection has a corresponding private key.
   
d) CORRECT. The ~/.ssh/known_hosts file stores the public keys of servers that the client has previously connected to.
   When connecting to a server, the client uses this file to verify the server's identity, ensuring it is connecting to the correct and trusted server.

"""

"""

SSH key-based authentication is a secure method for logging into a server without needing a password.
It uses a pair of cryptographic keys: a private key (kept secure on the client) and a public key (stored on the server).
When the client initiates a connection, the server uses the public key to verify the client by requesting proof of the corresponding private key.

Key-based authentication offers enhanced security, as the private key never leaves the client, and it can be further protected with a passphrase.
Once set up, this method allows passwordless, secure access to remote systems.

"""