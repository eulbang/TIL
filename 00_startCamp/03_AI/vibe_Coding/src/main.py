from seat_manager import SeatManager
from animation import BallAnimation
from ui import SeatUI
import tkinter as tk
import os

if __name__ == "__main__":
    seat_manager = SeatManager()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "students.csv")
    students = seat_manager.load_students(data_path)
    animation = BallAnimation(seat_manager, students)

    root = tk.Tk()
    root.title("좌석 할당 애니메이션")
    app = SeatUI(root, seat_manager, animation)
    root.mainloop()
