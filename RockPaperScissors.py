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
