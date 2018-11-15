# BITCOIN PARSING
### Đặc tả project
Nhiệm vụ chính của Project là từ dữ liệu của Bitcoin ở dạng nhị phân chứa trong các file ```.dat``` có thể parse thành dữ liệu có thể sử dụng để khai phá.

Project được sử dụng cho mục đích nghiên cứu khoa học ở trường Đại học Bách Khoa HCM

Ngôn ngữ sử dụng: Python (3.6)
Các thư viện sử dụng: ```hashlib```, ```struct```, ```codecs```

Tác giả: Nguyễn Duy Minh (nguyenduyminh2111@gmail.com)

### Nguồn dữ liệu
Dowload BitcoinCore tại https://bitcoin.org/en/download 

### Cấu trúc của một Block
Mỗi Block đều được bắt đầu bằng một ```Magic Number``` 
STT | Trường dữ liệu | Mô tả | Kích thước |
--- | --- | --- | --- |
1 | Magic No | luôn có giá trị 0xD9B4BEF9 | 4 bytes |
2 | Blocksize | Số bytes của một block | 4 bytes |
3 | Blockheader | Bao gồm 6 thành phần | 80 bytes |
4 | Transaction Counter | Số nguyên dương dạng VarInt | 1-9 bytes |
5 | Transactions | Danh sách các giao dịch | ~
