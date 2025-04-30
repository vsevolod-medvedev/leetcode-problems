
# private key: (p,q)
# public key: (x=NOD(p,q), y=NOK(p,q))

def get_private_key_count_by_public_key(x, y):
    return 0


def test():
    for i, (x, y, expected) in enumerate((
            (5, 10, 2),  # (5, 10), (10, 5)
            (10, 11, 0),  # (10, 11)
            (527, 9486, 4),  # (527, 9486), (1054, 4743), (4743, 1054), (9486, 527)
    )):
        actual = get_private_key_count_by_public_key(x, y)
        assert actual == expected, f"case #{i}: {x}, {y}: expected {expected}, got {actual}"
    print("Test passed!")


test()
