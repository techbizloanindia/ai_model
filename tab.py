# # Set table size
# size = 10

# # Print header row
# print("     ", end="")
# for i in range(1, size + 1):
#     print(f"{i:4}", end="" )
# print()
# print("-" * (5 + 4 * size))

# # Print table rows
# for i in range(1, size + 1):
#     print(f"{i:4} |", end="")
#     for j in range(1, size + 1):
#         print(f"{i*j:4}", end="")
#     print()

# for i in range(1, size + 1):
#     print(f"{i:4} |", end="")
#     for j in range(1, size + 1):
#         if j == size:  # Last column
#             print(f"{i * j:4}\n", end="")  # Add \n here
#         else:
#             print(f"{i * j:4}", end="")
#     # Remove the print() line entirely


