import gnupg
import users
gpg = gnupg.GPG(gnupghome='/home/nova/.gnupg')


def addKey(fingerprint, user):
    users.userFingerprints[user] = fingerprint
    users.saveFingerprints()
    return users.userFingerprints


# addKey("46CC730865BB5C78EBABADCF04376F3EE0856959", "testUser")
# addKey("D97D512B3B911BF01D0DE3759EAD8A0ECA74B82B", "testUser1")

def findKey(user):

    for key in gpg.list_keys():
        if key["fingerprint"] in users.userFingerprints[user]:
            return key['keyid']

def encrypt(plainText, user):
    if len(plainText) <= 70:
        cipherText = gpg.encrypt(plainText, findKey(user))
        if cipherText.status == 'encryption ok':
            return str(cipherText)
    else:
        return "plaintext to long"


def importKey(pubKey, username):
    gpg.import_keys(pubKey)
    addKey(gpg.list_keys()[-1]['fingerprint'], username)


def decrypt(cipherText):
    return gpg.decrypt(cipherText)
# cipher = encrypt("Hello World Hello", "testUser1")
# print(cipher)
# print(decrypt(cipher))
