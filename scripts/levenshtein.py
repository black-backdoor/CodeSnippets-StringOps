def levenshtein_distance(word1, word2):
    len_word1 = len(word1) + 1
    len_word2 = len(word2) + 1

    # Initialize a matrix to store the distances
    matrix = [[0 for _ in range(len_word2)] for _ in range(len_word1)]

    # Initialize the first row and column of the matrix
    for i in range(len_word1):
        matrix[i][0] = i

    for j in range(len_word2):
        matrix[0][j] = j

    # Fill in the matrix
    for i in range(1, len_word1):
        for j in range(1, len_word2):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    # The bottom-right cell of the matrix contains the Levenshtein distance
    return matrix[-1][-1]

# Example usage
word1 = "em2in4ence"
word2 = "eminance"

distance = levenshtein_distance(word1, word2)
print(f"Levenshtein distance between {word1} and {word2}: {distance}")
