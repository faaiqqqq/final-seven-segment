# Muhammad Faaiq Fadhlurrahman
# D121231101

def seven_segment(num):
    segments = {
        '0': ["###", "# #", "# #", "# #", "###"],
        '1': ["#  ", "#  ", "#  ", "#  ", "#  "],
        '2': ["###", "  #", "###", "#  ", "###"],
        '3': ["###", "  #", "###", "  #", "###"],
        '4': ["# #", "# #", "###", "  #", "  #"],
        '5': ["###", "#  ", "###", "  #", "###"],
        '6': ["###", "#  ", "###", "# #", "###"],
        '7': ["###", "  #", "  #", "  #", "  #"],
        '8': ["###", "# #", "###", "# #", "###"],
        '9': ["###", "# #", "###", "  #", "###"]
    }

    segments_to_display = segments[num]

    for line in segments_to_display:
        print(line)

def display_seven_segment_table(num):
    segments = [
        [1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1]   # 9
    ]

    headers = ["Decimal", "A", "B", "C", "D", "E", "F", "G"]
    data = [segments[num]]

    print(f"{'Decimal':<8} {'A':<3} {'B':<3} {'C':<3} {'D':<3} {'E':<3} {'F':<3} {'G':<3}")
    print("=" * 38)
    print(f"{num:<8}", end=" ")
    for segment in segments[num]:
        print(segment, end="   ")
    print()


input_number = int(input("Masukkan angka (0-9): "))
if 0 <= input_number <= 9:
    # Panggil fungsi untuk menampilkan tabel dan angka seven-segment
    display_seven_segment_table(input_number)
    seven_segment(str(input_number))
else:
    print("Angka yang dimasukkan tidak valid.")