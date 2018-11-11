import pickle


userFingerprints = pickle.load(open("userFingerprints.p", "rb"))


def saveFingerprints():
    pickle.dump(userFingerprints, open("userFingerprints.p", "wb"))

