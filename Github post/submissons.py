import json
from collections import defaultdict


with open('db/submissions.json', 'r') as file:
    data = json.load(file)


total_attempts = len(data['results'])
print(f'Totalt antall forsøk: {total_attempts}\n')


correct_attempts = 0
incorrect_attempts = 0

for submission in data['results']:
    submission_type = submission['type']
    if submission_type == 'correct':
        correct_attempts += 1
    else:
        incorrect_attempts += 1

print(f'Korrekte forsøk: {correct_attempts}')
print(f'Inkorrekte forsøk: {incorrect_attempts}')

if total_attempts > 0:
    correct_percentage = (correct_attempts / total_attempts) * 100
    print(f'Prosent: {correct_percentage:.2f}%')
else:
    print("No attempts recorded.")


attempts_per_user = defaultdict(int)

for submission in data['results']:
    user_id = submission['user_id']
    attempts_per_user[user_id] += 1


sorted_users = sorted(attempts_per_user.items(), key=lambda x: x[1], reverse=True)

print("\nBrukere med flest forsøk:")
for user_id, attempts in sorted_users:
    print(f'User ID: {user_id}, Attempts: {attempts}')


attempts_per_challenge = defaultdict(int)

for submission in data['results']:
    challenge_id = submission['challenge_id']
    attempts_per_challenge[challenge_id] += 1


sorted_challenges = sorted(attempts_per_challenge.items(), key=lambda x: x[1], reverse=True)


print("\nChallenges sorted by the number of attempts:")
for challenge_id, attempts in sorted_challenges:
    print(f'Challenge ID: {challenge_id}, Attempts: {attempts}')
