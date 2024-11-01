# Đá, Giấy, Kéo - Trò Chơi Kinh Điển! ✊✋✌️

Chào mừng bạn đến với dự án **Đá, Giấy, Kéo**! Đây là một trò chơi đơn giản nhưng vô cùng thú vị, giúp bạn cải thiện kỹ năng lập trình và hiểu hơn về logic điều kiện trong mã nguồn. Hãy tham gia và xem bạn có thể đánh bại máy tính hay không! 💪

## Mô Tả Dự Án 📝

Trong trò chơi "Đá, Giấy, Kéo", bạn sẽ chơi đối kháng với máy tính. Bạn sẽ chọn một trong ba lựa chọn: Đá, Giấy hoặc Kéo, và máy tính sẽ đưa ra lựa chọn của riêng mình. Trò chơi sẽ xác định ai là người chiến thắng dựa trên quy tắc đơn giản:

- Đá thắng Kéo ✊ > ✌️
- Kéo thắng Giấy ✌️ > ✋
- Giấy thắng Đá ✋ > ✊

## Cách Chạy Dự Án 🚀

1. **Cài đặt Python**: Đảm bảo bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

2. **Chạy Mã Nguồn**: Sao chép mã nguồn từ và mở tệp Python (.py) trong một trình soạn thảo mã. Sau đó, chạy chương trình:
   ```bash
   python RockPaperScissors.py
   ```

## Mã Nguồn 📄

Dưới đây là mã nguồn chính của dự án:

```python
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("🎉 Chào mừng đến với trò chơi Đá, Giấy, Kéo! 🎊")
    
    while True:
        user_choice = input("Nhập 'rock' ✊, 'paper' 📝, hoặc 'scissors' ✂️ (hoặc 'quit' để thoát): ").lower()
        
        if user_choice == 'quit':
            print("✌️ Cảm ơn bạn đã chơi! Hẹn gặp lại lần sau! 💖")
            break
        
        if user_choice not in choices:
            print("🚫 Lựa chọn không hợp lệ! Xin vui lòng thử lại.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🤖 Máy tính đã chọn: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 Hòa! Cả hai đều chọn", user_choice)
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 Bạn thắng! Tuyệt vời! 🏆")
        else:
            print("😢 Bạn thua! Máy tính thắng.")

# Chạy trò chơi
rock_paper_scissors()
```

## Ghi Chú 📌

- **Khám Phá Thêm**: Hãy thử thay đổi các quy tắc hoặc thêm tính năng như chơi nhiều vòng hoặc lưu điểm số!
- **Chia Sẻ Sáng Tạo**: Nếu bạn tạo ra phiên bản độc đáo của trò chơi, đừng quên chia sẻ với bạn bè và cộng đồng nhé! 🌍

## Liên Hệ 🤝

Nếu bạn có bất kỳ câu hỏi nào hoặc cần hỗ trợ, hãy liên hệ với chúng tôi qua [Fanpage CodeThinkers](https://www.facebook.com/CodeThinkers).

---

Hãy cùng nhau khám phá và sáng tạo với lập trình nhé! 💖
```
