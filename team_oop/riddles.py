
class Riddle:
    def __init__(self, riddle, answer):
        self.riddle = riddle
        self.answer = answer

    def solve_riddle(self, answer):
        response = input(f"{self.riddle}")
        if response.lower() == "fire":
            print("Congratulations! You solved the riddle.")
            return 1
        else:
            print("Sorry, that's not the correct answer. Please try again.")
            return 0
        

riddle1 = Riddle("I am not alive, but I grow. I don't have lungs, but I need air. I don't have a mouth, but water kills me. What am I?", "fire") 

# class riddle2:
#     def __init__(self):
#         self.riddle = "What can be touched, but never seen?"

#     def solve_riddle(self, answer):
#         if answer.lower() == "hearts":
#             print("Congratulations! You solved the riddle.")
#         else:
#             print("Sorry, that's not the correct answer. Please try again.")
#     exit()
# import time
# class riddle3:
#     def __init__(self):
#         self.riddle = "What can run, but never walk?"

#     def solve_riddle(self, answer):
#             time = time.time()
#         if answer.lower() == "river":
#             end_time = time.time()
#             elapsed_time = end_time - start_time
#             print(f"Congratulations! You solved the riddle in {elapsed_time:.2f} seconds.")
#         else:
#             print("Sorry, that's not the correct answer. Please try again.")

# # Example usage:
# if __name__ == "__main__":
#     riddle = riddle3()
#     print(riddle.riddle)
#     user_answer = input("Your answer: ")
#     riddle.solve_riddle(user_answer)
