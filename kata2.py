def solution(S):
    # Create a dictionary to count the occurrences of each letter in the string.
    letter_count = {}
    
    # Count the occurrences of each letter in the string.
    for letter in S:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    deletions_needed = 0
    
    # Iterate through the letter counts while checking for odd occurrences returning the total number of deletion to word even.
    for count in letter_count.values():
        if count % 2 != 0:
            deletions_needed += 1
    
    return deletions_needed

def reverse_words(S):
    # Split the input string into words based on spaces.
    words = S.split()
    
    # Reverse each word and join them with spaces.
    reversed_words = ' '.join([word[::-1] for word in words])
    
    return reversed_words





# Test cases
print(solution("acbcbba"))  # Output: 1
print(solution("axxaxa"))   # Output: 2

S = "we test coders"
print(reverse_words(S))  # Output: "ew tset sredoc"
