import pickle

try:
    userFingerprints = pickle.load(open("userFingerprints.p", "rb"))
except IOError:
    pass


def saveFingerprints():
    pickle.dump(userFingerprints, open("userFingerprints.p", "wb"))
