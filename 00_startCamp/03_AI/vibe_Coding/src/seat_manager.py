from typing import List, Optional
import csv

class SeatManager:
    def __init__(self, rows: int = 7, cols: int = 5):
        self.rows = rows
        self.cols = cols
        self.seats = self._create_seat_map()

    def _create_seat_map(self) -> List[List[Optional[str]]]:
        # None: 비활성화, "": 빈 좌석, str: 학생 이름
        seats = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        # 예시: 중앙 세로줄 비활성화, 맨 아래 중앙 3칸 비활성화
        for r in range(self.rows):
            seats[r][2] = None
        for c in range(1, 4):
            seats[6][c] = None
        return seats

    def load_students(self, filepath: str) -> List[str]:
        students = []
        with open(filepath, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # 헤더 스킵
            for row in reader:
                if row and row[0].strip():
                    students.append(row[0].strip())
        return students

    def assign(self, row: int, col: int, name: str):
        if self.seats[row][col] == "":
            self.seats[row][col] = name

    def is_active(self, row: int, col: int) -> bool:
        return self.seats[row][col] is not None

    def is_empty(self, row: int, col: int) -> bool:
        return self.seats[row][col] == ""
