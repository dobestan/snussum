from hashids import Hashids
from snussum.settings import HASHIDS_USER_PROFILE_SALT


def get_user_profile_hashid_object():
    return Hashids(salt=HASHIDS_USER_PROFILE_SALT, min_length=4)


def get_encoded_user_profile_hashid(id):
    hashid = get_user_profile_hashid_object()
    return hashid.encode(id)


def get_decoded_user_profile_hashid_object(hash_id):
    hashid = get_user_profile_hashid_object()
    return hashid.decode(hash_id)[0]
