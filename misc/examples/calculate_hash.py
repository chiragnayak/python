

import hashlib

with open("C:\\Users\\saanv\\Downloads\\VirtualBox-7.1.4-165100-Win.exe", "rb") as data:

    # Calculate SHA-256 digest
    digest = hashlib.sha256(data.read()).hexdigest()

    # Display the digest value
    print("SHA-256 Digest:", digest)