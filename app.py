scale = 4
size = (320, 224)
width = size[0]
height = size[1]

elapsed_time = 0.0

max_stage = 7
stage = None
map = None
num_monster = None

best_score = None
score = None

dragon = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b or right_a < left_b or top_a < bottom_b or bottom_a > top_b:
        return False
    return True
