import md5
BLOCK_SIZE = md5.digest_size
O_CONST = 0x5c
I_CONST = 0x36

def hmac_MD5(key, msg):
    if len(key) > BLOCK_SIZE:
        key = md5.new(data=key).hexdigest()
    key = key + bytearray(BLOCK_SIZE - len(key))

    o_key_pad = bytearray([key[i] ^ O_CONST for i in range(BLOCK_SIZE)])

    i_key_pad = bytearray([key[i] ^ I_CONST for i in range(BLOCK_SIZE)])

    second_half = md5.new(i_key_pad + msg).hexdigest()

    return md5.new(o_key_pad + second_half).hexdigest()

print(hmac_MD5("key", "Parth Rathod"))

