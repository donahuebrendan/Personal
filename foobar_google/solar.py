import math
square_list = []

def run():
    solution(500)
    solution(12)

def recursion_square(number):
    # Awesome Recursion Function
    float_number = float(number)
    largest_possible = int(math.sqrt(float_number))
    return largest_possible * largest_possible
    
def solution(area):
    square_list = []
    print area
    while area > 3:
        sq = recursion_square(area)
        area = area - sq
        square_list.append(sq)
        
    for i in range(area):
        square_list.append(1)
    print square_list
    return square_list

if __name__ == "__main__":
        run()
