from hashids import Hashids
from snussum.settings import HASHIDS_DATING_SALT


def get_dating_hashid_object():
    return Hashids(salt=HASHIDS_DATING_SALT, min_length=4)


def get_encoded_dating_hashid(id):
    hashid = get_dating_hashid_object()
    return hashid.encode(id)


def get_decoded_dating_hashid(hash_id):
    hashid = get_dating_hashid_object()
    return hashid.decode(hash_id)[0]