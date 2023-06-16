class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(i,N):
                print(' ', end=" ")
            for j in range(1,i+2):
                print(j,end=" ")
            for j in range(1,i):
                print(j,end=" ")
            print()
        for i in range(N):
            for j in range(i+1):
                print(" ",end=' ')
            for j in range(i+1,N):
                print(j,end=" ")
            for j in range(i,N):
                print(j,end=" ")

            print()

# Example usage
solutions = Solution()
N = int(input("Enter the value of N: "))  # Assuming user inputs 5
solutions.printSquare(N)
