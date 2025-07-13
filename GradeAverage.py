# Get 5 test scores from user
scores = []

print("Enter 5 test scores:")
for i in range(5):
    score = float(input(f"Score {i+1}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

# Check individual pass condition (e.g., minimum 40 in each subject)
individual_pass = all(score >= 40 for score in scores)

# Final result
if individual_pass and average >= 50:
    result = "Pass"
else:
    result = "Fail"

# Display results
print("\n--- Result ---")
print("Scores:", scores)
print("Average:", average)
print("Result:", result)
