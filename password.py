def sau_dang_nhap():
    while True:
        try:
            print()
            chon = int(input("Bạn có muốn đang xuất không\n1.Có\n2.Không\nChọn (1,2): "))

            if chon == 1:
                break
            
            elif chon == 2:
                print()

            else:
                print("\nKhông hợp lệ")
        except:
            print("\nKhông hợp lệ")

def dang_nhap():
    kp = False
    while True:
        print()
        name = input("Nhập tên của bạn: ")

        for i in dic:
            if i["username"] == name:
                kp = True
        
        if kp == True:
            kp = False
            break

        else:
            print("\nTên đăng nhập không hợp lệ!")
    
    while True:
        print()
        email = input("Nhập email: ")

        for i in dic:
            if i["email"] == email:
                kp = True
        
        if kp == True:
            kp = False
            break

        else:
            print("\nKhông tìm thấy địa chỉ email!")
    
    while True:
        print()
        password = input("Nhập mật khẩu: ")

        for i in dic:
            if i["password"] == password:
                kp = True
        
        if kp == True:
            kp = False
            break

        else:
            print("\nMật khẩu không đúng!")
    
    print("\nĐăng nhập đã thành công")
    sau_dang_nhap()
    
            
def dang_ky():
    while True:
        username = input("Nhập tên: ")
        print()

        if username == "" or username == " ":
            print("Vui lòng nhập tên")
            print()

        else:
            break
    
    while True:
        email = input("Nhập email: ")
        print()

        if email == "" or email == " " or "@gmail.com" in email == False:
            print("Vui lòng nhập đúng gmail")
            print()

        else:
            break
    
    while True:
        password = input("Nhập password: ")
        print()

        if password == "" or password == " ":
            print("Vui lòng nhập mật khẩu")
            print()
        else:
            break
    
    print("Bước đăng ký đã hoàn thành\n")

    return username, email, password

def main():
    while True:
        try:
            print()
            chon = int(input("1.Đăng Nhập\n2.Đăng ký\n3.Thoát\nChọn (1,2,3): "))
            print()

            if chon == 1:
                dang_nhap()

            elif chon == 2:
                username,email,password = dang_ky()

                dic.append({})

                new_dic = dic[-1]
                new_dic["username"] = username
                new_dic["email"] = email
                new_dic["password"] = password

            elif chon == 3:
                print("Cảm ơn bạn đã sử dụng ^_^\n")
                return False
            
            else:
                print("Vui lòng nhập đúng")

        except:
            print("Vui lòng nhập đúng")

if __name__ == "__main__":
    run = True
    dic = []

    while run:
        run = main()

        if run == False:
            break