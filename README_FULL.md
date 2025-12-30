# Blockchain Explorer

Một ứng dụng web đơn giản để khám phá, lưu trữ và hiểu về công nghệ blockchain.

## 📖 Giới thiệu

**Blockchain là gì?**
- Blockchain là một chuỗi các "block" được liên kết với nhau bằng hash cryptographic
- Mỗi block chứa dữ liệu (giao dịch), timestamp, hash, và hash của block trước
- Nếu ai cố gắng sửa đổi 1 block cũ, hash của nó sẽ thay đổi → phá vỡ chuỗi → dễ phát hiện

**Ứng dụng này cho phép bạn:**
- ✅ Thêm giao dịch (transaction)
- ✅ Khai thác block (mining) 
- ✅ Xác thực tính hợp lệ của chuỗi (validation)
- ✅ Xem chi tiết từng block (hash, giao dịch, timestamp, nonce)
- ✅ Lưu dữ liệu tự động (Persistence)
- ✅ Reset blockchain khi cần

---

## 🚀 Cài đặt

### Yêu cầu
- Python 3.8 trở lên
- pip (Python package manager)

### Các bước cài đặt

1. **Clone hoặc tải project**
```bash
cd DA_Blockchian2
```

2. **Tạo virtual environment**
```bash
python -m venv venv
```

3. **Kích hoạt virtual environment**

**Trên Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Trên Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Trên macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Cài đặt dependencies**
```bash
pip install -r requirements.txt
```

---

## 🏃 Chạy ứng dụng

Sau khi kích hoạt virtual environment:

```bash
python app.py
```

Mở trình duyệt và truy cập:
```
http://127.0.0.1:5000
```

---

## 💾 Persistence (Lưu dữ liệu)

### Cơ chế hoạt động
- Ứng dụng sử dụng **localStorage** (lưu trữ cục bộ của trình duyệt)
- Mỗi lần bạn:
  - Thêm giao dịch
  - Khai thác block
  - Reset blockchain
  
  → Dữ liệu sẽ được **lưu tự động** vào localStorage

### Ưu điểm
- ✅ Không cần database
- ✅ Dữ liệu được lưu trên máy của bạn
- ✅ Khi reload page → blockchain vẫn được khôi phục
- ✅ Tắt browser cũng không mất dữ liệu

### Cách hoạt động

**Khi page load:**
```javascript
1. Kiểm tra localStorage có dữ liệu blockchain không?
2. Nếu có → Load dữ liệu đã lưu (lấy từ lần chạy trước)
3. Nếu không → Fetch từ server (tạo blockchain mới)
```

**Mỗi thao tác (add transaction, mine, reset):**
```javascript
→ Tự động lưu vào localStorage
→ Nên kể cả khi tắt browser, dữ liệu vẫn còn
```

**Khôi phục dữ liệu:**
- Mỗi lần mở lại app trong cùng browser
- Dữ liệu blockchain sẽ được tự động load từ localStorage
- Quá trình này hoàn toàn tự động, không cần bất cứ thao tác nào

### Xóa dữ liệu lưu
- Click nút **"🔄 Reset Blockchain"** để xóa toàn bộ và bắt đầu lại
- Hoặc dùng DevTools (F12) → Application → Local Storage → Xóa key `blockchain_data`

### Lưu ý
- Persistence hoạt động **trên cùng một browser** (Chrome, Firefox, Safari,...)
- Nếu xóa cache/cookies của browser → dữ liệu sẽ mất
- Nếu đăng nhập vào tài khoản khác trên cùng browser → vẫn thấy dữ liệu cũ

---

## 📊 Hướng dẫn sử dụng

### Bước 1: Thêm giao dịch
1. Điền thông tin:
   - **Người gửi**: Tên hoặc địa chỉ của người gửi (ví dụ: "Alice")
   - **Người nhận**: Tên hoặc địa chỉ của người nhận (ví dụ: "Bob")
   - **Số tiền**: Số lượng tiền cần gửi (ví dụ: 100)
2. Click **"⚡ Gửi"**
3. Giao dịch sẽ được thêm vào mempool (chưa được khai thác)
4. Số lượng "Giao dịch chờ" sẽ tăng lên

### Bước 2: Khai thác khối (Mining)
1. Click **"⛏️ Khai thác khối"**
2. Hệ thống sẽ:
   - Lấy toàn bộ giao dịch chưa được khai thác
   - Tạo một block mới chứa các giao dịch này
   - Tính toán hash cho block (SHA-256)
   - Thêm block vào chuỗi
3. **"Giao dịch chờ"** sẽ reset về 0
4. **"Tổng số khối"** sẽ tăng 1
5. **"Tổng giao dịch"** sẽ tăng theo số giao dịch vừa khai thác
6. Dữ liệu sẽ tự động lưu vào localStorage

### Bước 3: Xem chi tiết Blockchain
1. Click **"👁️ Xem Blockchain"**
2. Trang sẽ tự động scroll xuống bảng "Dữ liệu Blockchain"
3. Bảng hiển thị:
   - **Khối**: Chỉ số block (1, 2, 3,...)
   - **Hash**: Hash của block (cắt ngắn, click để xem full)
   - **Hash trước**: Hash của block trước đó
   - **Thời gian**: Thời điểm block được tạo
   - **Giao dịch**: Danh sách giao dịch trong block
   - **Nonce**: Số thứ tự của block

### Bước 4: Xem chi tiết một Block
1. Click vào dòng bất kỳ trong bảng
2. Modal sẽ hiện ra với đầy đủ thông tin:
   - Hash đầy đủ (không cắt ngắn)
   - Hash trước đó
   - Thời gian tạo
   - Nonce
   - Proof
   - Chi tiết từng giao dịch:
     - Người gửi
     - Người nhận
     - Số tiền
     - Thời gian

### Bước 5: Xác thực Blockchain
1. Click **"✔️ Xác thực chuỗi"**
2. Hệ thống sẽ kiểm tra:
   - Mỗi block có `previous_hash` = hash của block trước không?
   - Nếu tất cả khớp → ✓ **Chuỗi hợp lệ**
   - Nếu có sai lệch → ✗ **Chuỗi không hợp lệ**

### Bước 6: Reset Blockchain
1. Click **"🔄 Reset Blockchain"**
2. Xác nhận yêu cầu reset
3. Blockchain sẽ:
   - Xóa toàn bộ block (trừ Genesis block)
   - Reset giao dịch chờ
   - Lưu state mới vào localStorage
4. Bắt đầu từ đầu

---

## 🔐 Cơ chế Blockchain trong ứng dụng

### Cấu trúc Block
```json
{
  "index": 1,
  "timestamp": "30/12/2025 22:30:43",
  "transactions": [
    {
      "sender": "Alice",
      "receiver": "Bob",
      "amount": 100,
      "timestamp": "30/12/2025 22:30:10"
    }
  ],
  "proof": 1,
  "previous_hash": "0...",
  "hash": "f7f5beba5...",
  "nonce": 1
}
```

### Hashing (SHA-256)
- Mỗi block có một hash được tính từ dữ liệu của nó
- Nếu dữ liệu thay đổi 1 byte → hash thay đổi hoàn toàn
- `hash = SHA256(block_data)`

### Chain Linking
- Block 1 (Genesis): `previous_hash = "0"`
- Block 2: `previous_hash = hash_of_block_1`
- Block 3: `previous_hash = hash_of_block_2`
- ...

Điều này tạo ra một "chuỗi" mạnh mẽ - nếu ai thay đổi block 1, thì hash của block 2 sẽ không khớp với previous_hash, làm cho blockchain trở nên không hợp lệ.

### Validation Logic
```javascript
for each block in chain (starting from block 2):
  if current_block.previous_hash != hash(previous_block):
    return "Chuỗi không hợp lệ"
return "Chuỗi hợp lệ"
```

---

## 📁 Cấu trúc thư mục

```
DA_Blockchian2/
├── app.py                  # Flask backend + Blockchain class
├── blockchain.py           # Blockchain logic (phiên bản cũ)
├── requirements.txt        # Dependencies (Flask, requests)
├── README.md              # File cơ bản
├── README_FULL.md         # File chi tiết (file này)
├── static/
│   ├── style.css          # CSS styling (gradient, card design)
│   ├── scripts.js         # JavaScript (nếu có)
│   └── favicon_io/        # Icon
├── templates/
│   └── index.html         # Giao diện chính (HTML + JavaScript)
└── venv/                  # Virtual environment
```

---

## 🛠️ Công nghệ sử dụng

| Công nghệ | Phiên bản | Mục đích |
|-----------|----------|---------|
| Python | 3.8+ | Backend |
| Flask | 3.0+ | Web framework |
| HTML5 | Latest | Giao diện |
| CSS3 | Latest | Styling (gradient, responsive) |
| JavaScript | Vanilla | Frontend logic, persistence |
| SHA-256 | hashlib | Hashing |
| localStorage | Browser API | Lưu dữ liệu cục bộ |

---

## ❓ FAQ

**Q: Nếu tắt browser, dữ liệu có bị mất không?**
A: Không! localStorage lưu dữ liệu trên máy bạn, không phụ thuộc vào browser session. Khi mở lại, dữ liệu sẽ được tự động khôi phục.

**Q: Sao không dùng database thực như MongoDB hay PostgreSQL?**
A: Vì đây là bài đồ án học tập, localStorage đơn giản hơn, không cần setup database, và đủ để học blockchain.

**Q: Nếu muốn xóa dữ liệu, làm sao?**
A: Click nút "🔄 Reset Blockchain" hoặc xóa localStorage từ DevTools (F12 → Application → Local Storage).

**Q: Có thể chạy trên mạng khác (máy khác) không?**
A: Có! Sửa `app.run(debug=True)` thành `app.run(host="0.0.0.0", port=5000)` trong app.py rồi truy cập từ IP khác (ví dụ: `http://192.168.1.100:5000`).

**Q: Persistence chỉ lưu trên browser này, máy khác không thấy được phải không?**
A: Đúng! localStorage là dữ liệu cục bộ của từng browser. Để share blockchain, cần dùng database thực hoặc API sync.

**Q: Có thể export blockchain thành file không?**
A: Có thể thêm tính năng này - export JSON hoặc CSV từ localStorage.

---

## 🎓 Bài học từ project

1. **Blockchain cơ bản**: Chuỗi block được liên kết bằng hash
2. **Cryptographic hash**: SHA-256 và tính chất không thể đảo ngược
3. **Chain validation**: Kiểm tra tính toàn vẹn của chuỗi
4. **Persistence**: Lưu dữ liệu trên client-side
5. **Web development**: Flask backend + Vanilla JS frontend

---

## 📝 License

Dự án này được tạo cho mục đích học tập.

---

## 👨‍💻 Tác giả

Bài đồ án Blockchain Explorer - Năm 2025
