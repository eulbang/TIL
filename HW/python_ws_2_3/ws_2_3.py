'''
MovieTheater 클래스를 상속받는 VIPMovieTheater 클래스를 정의한다.
VIPMovieTheater 클래스는 VIP 좌석 수를 저장하는 vip_seats 인스턴스 변수를 가진다.
생성자에서 처리되어야 한다.
VIPMovieTheater 클래스는 VIP 좌석을 예약하는 reserve_vip_seat 메서드를 가진다.
reserve_vip_seat 메서드는 예약 가능한 VIP 좌석이 있는 경우, vip_seats를 1 감소시키고 예약 성공 메시지를 반환한다.
예약 가능한 VIP 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
VIPMovieTheater 클래스는 reserve_seat 메서드를 오버라이딩하여, VIP 좌석이 먼저 예약되도록 한다.
VIP 좌석이 예약 가능한 경우, reserve_vip_seat 메서드를 호출하여 VIP 좌석을 예약한다.
VIP 좌석이 예약 불가능한 경우, 부모 클래스의 reserve_seat 메서드를 호출하여 일반 좌석을 예약한다.
'''

# 아래에 코드를 작성하시오.

class MovieTheater:
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

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = int(vip_seats)
    
    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            print("예약 성공")
        else:
            print("예약 실패")
    
    def reserve_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            self.reserve_vip_seat()
        else:
            super().reserve_seat()


theater = MovieTheater('cgv', '200')
print(theater)
theater.reserve_seat()
theater.current_status()

viptheater = VIPMovieTheater('MEGABOX', '200', '10')
print(viptheater)
viptheater.reserve_seat()
viptheater.current_status()