'''
User 클래스를 정의한다.
User 클래스는 사용자의 이름과 이메일을 인자로 받는 생성자 메서드를 정의한다.
각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
User 클래스는 사용자의 정보를 출력하는 show_info 인스턴스 메서드를 정의한다.
AdminUser 클래스를 정의하고, User 클래스를 상속받는다.
AdminUser 클래스는 추가적으로 관리자의 권한을 나타내는 permissions 변수를 가지며, 생성자 메서드에서 이를 초기화한다.
AdminUser 클래스는 show_info 메서드를 오버라이딩하여, 사용자 정보와 함께 권한 정보를 출력한다.
2개 이상의 User 인스턴스와 1개 이상의 AdminUser 인스턴스를 생성하고, 각 인스턴스의 show_info 메서드를 호출하여 정보를 출력한다.
'''

# 아래에 코드를 작성하시오.

class User:
    user_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_count += 1

    def show_info(self):
        print(f"이름 : {self.name}, 이메일 : {self.email}")

class AdminUser(User):
    def __init__(self, name, email, permossions):
        super().__init__(name, email)
        self.permissions = permossions
    
    def show_info(self):
        print(f"이름 : {self.name}, 이메일 : {self.email}, 권한 : {self.permissions}")

june = AdminUser('june', 'june@gmail.com', 'admin')
hyung = AdminUser('hyung', 'hyung@gmail.com', 'guest')

june.show_info()
hyung.show_info()
