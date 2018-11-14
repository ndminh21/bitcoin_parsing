# import sys, re, json
# from bitcoin.transaction import deserialize
import struct, codecs
from datetime import datetime
import pprint

data = "f9beb4d91d0100000100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000f9beb4d9d7000000010000006fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000982051fd1e4ba744bbbe680e1fee14677ba1a3c3540bf7b1cdb606e857233e0e61bc6649ffff001d01e362990101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0104ffffffff0100f2052a0100000043410496b538e853519c726a2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781e62294721166bf621e73a82cbf2342c858eeac00000000f9beb4d9d7000000010000004860eb18bf1b1620e37e9490fc8a427514416fd75159ab86688e9a8300000000d5fdcc541e25de1c7a5addedf24858b8bb665c9f36ef744ee42c316022c90f9bb0bc6649ffff001d08d2bd610101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d010bffffffff0100f2052a010000004341047211a824f55b505228e4c3d5194c1fcfaa15a456abdf37f9b9d97a4040afc073dee6c89064984f03385237d92167c13e236446b417ab79a0fcae412ae3316b77ac00000000f9beb4d9d700000001000000bddd99ccfda39da1b108ce1a5d70038d0a967bacb68b6b63065f626a0000000044f672226090d85db9a9f2fbfe5f0f9609b387af7be5b7fbb7a1767c831c9e995dbe6649ffff001d05e0ed6d0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d010effffffff0100f2052a0100000043410494b9d3e76c5b1629ecf97fff95d7a4bbdac87cc26099ada28066c6ff1eb9191223cd897194a08d0c2726c5747f1db49e8cf90e75dc3e3550ae9b30086f3cd5aaac00000000f9beb4d9d7000000010000004944469562ae1c2c74d9a535e00b6f3e40ffbad4f2fda3895501b582000000007a06ea98cd40ba2e3288262b28638cec5337c1456aaf5eedc8e9e5a20f062bdf8cc16649ffff001d2bfee0a901010000000100000000000000000000000000000000ffffffff0704ffff001d011affffffff0100f2052a01000000434104184f32b212815c6e522e66686324030ff7e5bf08efb21f8b00614fb7690e19131dd31304c54f37baa40db231c918106bb9fd43373e37ae31a0befc6ecaefb867ac00000000f9beb4d9d70000000100000085144a84488ea88d221c8bd6c059da090e88f8a2c99690ee55dbba4e00000000e11c48fecdd9e72510ca84f023370c9a38bf91ac5cae88019bee94d24528526344c36649ffff001d1d03e4770101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0120ffffffff0100f2052a0100000043410456579536d150fbce94ee62b47db2ca43af0a730a0467ba55c79e2a7ec9ce4ad297e35cdbb8e42a4643a60eef7c9abee2f5822f86b1da242d9c2301c431facfd8ac00000000f9beb4d9d700000001000000fc33f596f822a0a1951ffdbf2a897b095636ad871707bf5d3162729b00000000379dfb96a5ea8c81700ea4ac6b97ae9a9312b2d4301a29580e924ee6761a2520adc46649ffff001d189c4c970101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0123ffffffff0100f2052a0100000043410408ce279174b34c077c7b2043e3f3d45a588b85ef4ca466740f848ead7fb498f0a795c982552fdfa41616a7c0333a269d62108588e260fd5a48ac8e4dbf49e2bcac00000000f9beb4d9d7000000010000008d778fdc15a2d3fb76b7122a3b5582bea4f21f5a0c693537e7a03130000000003f674005103b42f984169c7d008370967e91920a6a5d64fd51282f75bc73a68af1c66649ffff001d39a59c860101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d012bffffffff0100f2052a01000000434104a59e64c774923d003fae7491b2a7f75d6b7aa3f35606a8ff1cf06cd3317d16a41aa16928b1df1f631f31f28c7da35d4edad3603adb2338c4d4dd268f31530555ac00000000f9beb4d9d7000000010000004494c8cf4154bdcc0720cd4a59d9c9b285e4b146d45f061d2b6c967100000000e3855ed886605b6d4a99d5fa2ef2e9b0b164e63df3c4136bebf2d0dac0f1f7a667c86649ffff001d1c4b56660101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d012cffffffff0100f2052a01000000434104cc8d85f5e7933cb18f13b97d165e1189c1fb3e9c98b0dd5446b2a1989883ff9e740a8a75da99cc59"


def big_endian_2_int(string_value):
    byte_value = codecs.decode(string_value, "hex")
    return struct.unpack("<I", byte_value)[0]


def big_endian_2_int_1(string_value):
    byte_value = codecs.decode(string_value, "hex")
    return struct.unpack("<B", byte_value)[0]


def big_endian_2_int_2(string_value):
    byte_value = codecs.decode(string_value, "hex")
    return struct.unpack("<H", byte_value)[0]


def big_endian_2_int_8(string_value):
    byte_value = codecs.decode(string_value, "hex")
    return struct.unpack("<Q", byte_value)[0]

def cal_trans_count(check):
    check_1 = check[:2]
    count_1 = big_endian_2_int_1(check_1)
    check_2 = check[2:6]
    count_2 = big_endian_2_int_2(check_2)
    check_3 = check[2:10]
    count_3 = big_endian_2_int(check_3)
    check_4 = check[2:18]
    count_4 = big_endian_2_int_8(check_4)
    if count_1 < 253:
        return count_1, 1
    elif count_2 < 65535:
        return count_2, 3
    elif count_3 < 4294967295:
        return count_3, 5
    else:
        return count_4, 9


MAP_ENDIAN = {
    2: "<B",
    4: "<H",
    8: "<I",
    16: "<Q",
}


def little_endian_2_int(string_value):
    string_len = len(string_value)
    format_int = MAP_ENDIAN.get(string_len)
    byte_value = codecs.decode(string_value, "hex")
    return struct.unpack(format_int, byte_value)[0]


def cal_var_int(string_value):
    check_1 = string_value[:2]
    count_1 = big_endian_2_int_1(check_1)
    check_2 = string_value[2:6]
    count_2 = big_endian_2_int_2(check_2)
    check_3 = string_value[2:10]
    count_3 = big_endian_2_int(check_3)
    check_4 = string_value[2:18]
    count_4 = big_endian_2_int_8(check_4)
    if count_1 < 253:
        return count_1, 1
    elif count_2 < 65535:
        return count_2, 3
    elif count_3 < 4294967295:
        return count_3, 5
    else:
        return count_4, 9


MAGIC_BYTES = 4
BLOCK_SIZE_BYTES = 4
BLOCK_HEADER_BYTES = 80
CHECK_BYTES = 9


def get_block_header_component_string(block_header_string):
    version_string = block_header_string[:4 * 2]
    block_header_string = block_header_string[4*2:]
    hash_prev_block_string = block_header_string[:32 * 2]
    block_header_string = block_header_string[32 * 2:]
    hash_merkle_root_string = block_header_string[:32 * 2]
    block_header_string = block_header_string[32 * 2:]
    time_stamp_string = block_header_string[:4 * 2]
    block_header_string = block_header_string[4 * 2:]
    bits_string = block_header_string[:4 * 2]
    block_header_string = block_header_string[4 * 2:]
    nonce_string = block_header_string[:4 * 2]
    return {
        'version': version_string,
        'hash_prev_block': hash_prev_block_string,
        'hash_merkel_root': hash_merkle_root_string,
        'time_stamp': time_stamp_string,
        'bits': bits_string,
        'nonce': nonce_string
    }


def parse_block_header(block_header_string):
    header_string = get_block_header_component_string(block_header_string)

    return {
        'version': little_endian_2_int(header_string.get('version')),
        'hash_prev_block': header_string.get('hash_prev_block'),
        'hash_merkel_root': header_string.get('hash_merkel_root'),
        'time': datetime.utcfromtimestamp(little_endian_2_int(header_string.get('time_stamp'))).strftime('%Y-%m-%d %H:%M:%S'),
        'bits': header_string.get('bits'),
        'none': header_string.get('nonce')
    }


def parse_1_input(input_string):
    prev_trans_hash_string = input_string[:32*2]
    input_string = input_string[32*2:]

    prev_txout_index_string = input_string[:4*2]
    input_string = input_string[4*2:]

    txin_script_length_string = input_string[:9*2]
    txin_script_length, length = cal_var_int(txin_script_length_string)
    input_string = input_string[length*2:]

    txin_script_string = input_string[:txin_script_length*2]
    # TODO: parse txin script
    input_string = input_string[txin_script_length*2:]

    sequence_no_string = input_string[:4*2]
    sequence_no = little_endian_2_int(sequence_no_string)
    input_string = input_string[4*2:]

    return {
        "prev_trans_hash": prev_trans_hash_string,
        "prev_txout_index": prev_txout_index_string,
        "txin_script_length": txin_script_length,
        "txin_script": txin_script_string,
        "sequence_no": sequence_no_string
    }, input_string


def parse_input(input_string, input_count):
    inputs = []
    for i in range(0, input_count):
        input_trans, input_string = parse_1_input(input_string)
        inputs.append(input_trans)
    return inputs, input_string


def parse_1_output(output_string):
    value_string = output_string[:8*2]
    value = little_endian_2_int(value_string)
    output_string = output_string[8*2:]

    txout_script_length_check = output_string[:9*2]
    txout_script_length, length = cal_var_int(txout_script_length_check)
    output_string = output_string[length*2:]

    txout_script_string = output_string[:txout_script_length*2]
    # TODO: parse txout scrip
    output_string = output_string[txout_script_length*2:]

    return {
        "value": "{satoshi} Satoshi ({btc} BTC)".format(satoshi=value, btc=value/10**8),
        "txout_script_length": txout_script_length,
        "txout_script": txout_script_string

    }, output_string


def parse_output(output_string, output_count):
    outputs = []
    for i in range(0, output_count):
        output_trans, output_string = parse_1_output(output_string)
        outputs.append(output_trans)
    return outputs, output_string


def parse_1_transaction(trans_string):
    version_string = trans_string[:4 * 2]
    trans_string = trans_string[4*2:]

    in_counter_check = trans_string[:9*2]
    in_counter, length = cal_var_int(in_counter_check)
    trans_string = trans_string[length * 2:]

    inputs, trans_string = parse_input(trans_string, in_counter)

    out_counter_check = trans_string[:9 * 2]
    out_counter, length = cal_var_int(out_counter_check)
    trans_string = trans_string[length * 2:]

    outputs, trans_string = parse_output(trans_string, out_counter)

    lock_time_string = trans_string[:4*2]
    lock_time = datetime.utcfromtimestamp(little_endian_2_int(lock_time_string)).strftime('%Y-%m-%d %H:%M:%S')
    trans_string = trans_string[4*2:]

    return {
        "version": little_endian_2_int(version_string),
        "in_counter": in_counter,
        "inputs": inputs,
        "out_counter": out_counter,
        "outputs": outputs,
        "lock_time": lock_time_string
    }, trans_string


def parse_transaction(trans_string, trans_count):
    trans = []
    for i in range(0, trans_count):
        transaction, trans_string = parse_1_transaction(trans_string)
        trans.append(transaction)
    return trans


def parse_block(block_string):
    # Magic No, value always 0xD9B4BEF9, 4 bytes
    macgic_no_string = block_string[:MAGIC_BYTES*2]

    # Cut block string 4 bytes
    block_string = block_string[MAGIC_BYTES*2:]

    # Block size, number of bytes following up to end of block, 4 bytes
    block_size_string = block_string[:BLOCK_SIZE_BYTES*2]
    block_size = little_endian_2_int(block_size_string)

    # Cut block string 4 bytes
    block_string = block_string[BLOCK_SIZE_BYTES * 2:]

    # Block header, consists of 6 items, 80 bytes
    block_header_string = block_string[:BLOCK_HEADER_BYTES*2]
    block_header = parse_block_header(block_header_string)
    block_string = block_string[BLOCK_HEADER_BYTES*2:]

    # Transaction counter, positive integer VI = VarInt, 1-9 bytes
    trans_counter_string_check = block_string[:CHECK_BYTES*2]
    trans_counter, length = cal_var_int(trans_counter_string_check)
    block_string = block_string[length*2:]

    trans = parse_transaction(block_string, trans_counter)

    return {
        "magic_no": macgic_no_string,
        "block_size": block_size,
        "block_header": block_header,
        "transaction_counter": trans_counter,
        "transactions": trans
    }


def slip(data):
    # print("Magic Number", data[:8])

    block_size_string = data[8:16]
    block_size = big_endian_2_int(block_size_string)
    print("Block Size:", block_size, "bytes")

    block_header = data[16:176]
    verson_string = block_header[:8]
    verson = big_endian_2_int(verson_string)
    print("Version:", verson)

    print("Hash of previous block's header", block_header[8:72])
    print("Merkle root:", block_header[72:136])

    time_stamp_string = data[136:144]
    time_stamp = big_endian_2_int(time_stamp_string)
    time = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    print("Time:", time)

    nbits_string = data[144:152]
    nbits = big_endian_2_int(nbits_string)
    print("nBits:", nbits)

    nonce_string = block_header[152:]
    nonce = big_endian_2_int(nonce_string)
    print("nonce:", nonce)

    length_block = block_size * 2 + 8
    block = data[:length_block]
    block_data = block[176:]
    print(length_block)

    check = block_data[:18]
    transaction_count, count_len = cal_trans_count(check)
    print("Number of transactions in the block (including unmatched ones):", transaction_count)

    trans_data = block_data[count_len*2:]
    print('----Transaction----')
    trans_version_string = trans_data[:8]
    trans_version = big_endian_2_int(trans_version_string)
    print('Version', trans_version)
    trans_data = trans_data[8:]

    in_counter_string = trans_data[:18]
    in_counter, in_counter_len = cal_trans_count(in_counter_string)
    print("In counter", in_counter)
    trans_data = trans_data[in_counter_len*2:]

    print("    ----List of Inputs----")

    previous_transaction_hash = trans_data[:64]
    print("Previous Transaction Hash", previous_transaction_hash)
    trans_data = trans_data[64:]

    previous_txout_index_string = trans_data[:8]
    previous_txout_index = big_endian_2_int(previous_txout_index_string)
    print("Previous Txout Index:", previous_txout_index_string, previous_txout_index)
    trans_data = trans_data[8:]

    check = trans_data[:18]
    txin_sxript_length, txin_sxript_bytes = cal_trans_count(check)
    print("Txin Script Lenght:", txin_sxript_length)
    trans_data = trans_data[txin_sxript_bytes*2:]

    # TODO: Skip txin length
    trans_data = trans_data[txin_sxript_length*2:]

    sequence_no_string = trans_data[:8]
    sequence_no = big_endian_2_int(sequence_no_string)
    print("Sequence no:", sequence_no_string, sequence_no)
    trans_data = trans_data[8:]

    print("    ----End List of Inputs----")

    out_counter_string = trans_data[:18]
    out_counter, out_counter_len = cal_trans_count(out_counter_string)
    print("Out counter", out_counter)
    trans_data = trans_data[out_counter_len * 2:]

    print("    ----List of Outputs----")

    value_string = trans_data[:16]
    value = big_endian_2_int_8(value_string)
    print("Value:", value/10**8, "BTC")
    trans_data = trans_data[16:]

    check = trans_data[:18]
    txout_script_length, txout_bytes = cal_trans_count(check)
    print("Txout-script length", txout_script_length)
    trans_data = trans_data[txout_bytes*2:]

    # TODO: Skip txout length
    trans_data = trans_data[txout_script_length * 2:]

    print("    ----End List of Outputs----")

    # lock_time_string = trans_data[:8]
    # lock_time_stamp = big_endian_2_int(lock_time_string)
    # lock_time = datetime.utcfromtimestamp(lock_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    # print("Lock time", lock_time)


    # total_transaction_string = block_data[:8]
    # total_transaction = big_endian_2_int(total_transaction_string)
    # print("Number of transactions in the block (including unmatched ones)", total_transaction)
    #
    # print(codecs.decode(total_transaction_string, "hex"))
    # for i in range(1, 10):
    #     trans = block_data[:i*2]
    #     print(big_endian_2_int(trans))

    # print("Block Data", data[176:])

    # print(bytes.fromhex(data[:8]).decode('utf-8'))

    # print(bytes.fromhex(b'f9beb4d9').decode('utf-8'))
    # print(convert(data))


if __name__ == "__main__":
    # slip(data)
    pprint.pprint(parse_block(data[:578+8]))
    # https: // coinlogic.wordpress.com / 2014 / 02 / 18 / the - protocol - 1 - block /
    # https: // en.bitcoin.it / wiki / Protocol_documentation  # Variable_length_integer