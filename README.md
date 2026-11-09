# 📢 Real-Time Environmental Noise Monitoring System

> **Hệ thống giám sát tiếng ồn môi trường thời gian thực và tự động gửi thông báo cảnh báo ô nhiễm tiếng ồn.**

## 📖 Giới thiệu
Ứng dụng thu âm thanh từ micro, phân tích cường độ âm lượng (dB), phát hiện các đoạn âm thanh vượt ngưỡng quy chuẩn môi trường và lập tức kích hoạt tin nhắn cảnh báo tới người quản trị.

## ✨ Tính năng chính
- **Đo lường biên độ âm thanh**: Ghi nhận tín hiệu âm thanh liên tục qua microphone.
- **Biểu đồ hoá độ ồn**: Xuất biểu đồ trực quan mức độ ồn theo chu kỳ thời gian (`noise.png`, `example.png`).
- **Cảnh báo tự động**: Tích hợp kịch bản `sendmessage.py` để gửi thông báo khẩn cấp khi mức ồn vượt ngưỡng an toàn.

## 🛠️ Cài đặt & Chạy
```bash
pip install pyaudio numpy matplotlib requests
python index.py
```
