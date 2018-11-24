# BITCOIN PARSING

### Đặc tả project
Nhiệm vụ chính của Project là từ dữ liệu của **Bitcoin** ở dạng nhị phân chứa trong các file ```.dat``` có thể parse thành dữ liệu có thể sử dụng để khai phá.

Project được sử dụng cho mục đích nghiên cứu khoa học ở trường Đại học Bách Khoa HCM

Ngôn ngữ sử dụng: **Python** (3.6)
Các thư viện sử dụng: ```hashlib```, ```struct```, ```codecs```

Tác giả: **Nguyễn Duy Minh** (nguyenduyminh2111@gmail.com)

### Các công việc cần thực hiện 

- [x] Tìm hiểu kiến thức nền về Blockchain 
- [x] Lấy dữ liệu full node của Bitcoin 
- [x] Tìm hiểu cấu trúc block của Bitcoin
- [x] Parse được các dữ liệu cơ bản của một Block
- [ ] Parse chi tiết một Block
- [ ] Chuyển dữ liệu về dạng dữ liệu quan hệ
- [ ] Khai phá dữ liệu Bitcoin (Gồm nhiều công việc nhỏ)
- [ ] ......

### Nguồn dữ liệu
Dowload **BitcoinCore** tại https://bitcoin.org/en/download 

### Cấu trúc của một Block
Mỗi Block đều được bắt đầu bằng một ```Magic Number``` 


| STT | Trường dữ liệu | Mô tả | Kích thước |
| --- | --- | --- | --- |
| 1 | Magic No | Luôn có giá trị 0xD9B4BEF9 | 4 bytes |
| 2 | Blocksize | Số bytes của một block | 4 bytes |
| 3 | Blockheader | Bao gồm 6 thành phần | 80 bytes |
| 4 | Transaction Counter | Số nguyên dương dạng VarInt | 1-9 bytes |
| 5 | Transactions | Danh sách các giao dịch | ~ |


### Block sau khi đã được parse
Block genesis sau khi parse sẽ có giá trị như sau

```
{
    "block_header": {
        "bits": "1d00ffff",
        "hash_merkel_root": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
        "hash_prev_block": "0000000000000000000000000000000000000000000000000000000000000000",
        "none": 2083236893,
        "time": "2009-01-03 18:15:05",
        "version": 1
    },
    "block_size": 285,
    "magic_no": "f9beb4d9",
    "transaction_counter": 1,
    "transactions": [
        {
            "in_counter": 1,
            "inputs": [
                {
                    "prev_trans_hash": "0000000000000000000000000000000000000000000000000000000000000000",
                    "prev_txout_index": "ffffffff",
                    "sequence_no": "ffffffff",
                    "txin_script": "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73",
                    "txin_script_length": 77
                }
            ],
            "lock_time": "00000000",
            "out_counter": 1,
            "outputs": [
                {
                    "txout_script": "4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac",
                    "txout_script_length": 67,
                    "value": "5000000000 Satoshi (50.0 BTC)"
                }
            ],
            "version": 1
        }
    ]
}
```

Giá trị hash của block là `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`

### Tính Merkle Root của một Block

Ví dụ tính Merkle Root của Block #0

Đoạn hex string của Transaction là:
`01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000`

Bước 1: **sha256** lần 1
`27362e66e032c731c1c8519f43063fe0e5d070db1c0c3552bb04afa18a31c6bf`

Bước 2: **sha256** lần 2 
`3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a`

Bước 3: **Convert Endian**
`4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`

Vậy merkle root là: `4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`

