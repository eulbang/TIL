'''
3433번 문제에서 작성한 코드에서 이어서 작성한다.

MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.
MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다
add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
description 메서드는 아래 문장을 출력한다.
'"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
"영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."
'''

# 아래에 코드를 작성하시오.

class MovieTheater:
    total_movies = 0

    def add_movie(self):
        MovieTheater.total_movies += 1
        print("영화 추가 완료")

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = int(total_seats)
        self.reserved_seats = 0

    def __str__(self):
        return self.name
    
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            print("예약 성공")
        else:
            print("예약 실패")

    def current_status(self):
        print(f"총 좌석 수 : {self.total_seats}, 예약 좌석 수 : {self.reserved_seats}")

    @staticmethod
    def description():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

theater = MovieTheater('cgv', '200')
print(theater)

theater.reserve_seat()

theater.current_status()

theater.add_movie()

theater.description()