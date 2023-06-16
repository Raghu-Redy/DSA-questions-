class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(i,N):
                print("*", end=" ")
            print()

# Example usage
solutions = Solution()
N = int(input("Enter the value of N: "))  # Assuming user inputs 5
solutions.printSquare(N)
