# CSA Bonus Calculator
# Get monthly average and get bonus based of average and position
import payout_chart

weekly_score = []

max_bonus = 834


def csa_average(weekly_score):
    # Get average score for month
    score = 

    for weeks in weekly_score:
        score += weeks

    average = score / len(weekly_score)
    return average


def bonus_amount(max_bonus, position, average):
        # Determine bonus amount based off CSA average and position
    if position == 'Manager' or 'manager':
        payout_chart.manager(max_bonus, average)


def main():
    print("Enter Weekly Scores rounded to nearest tenth.")

    for score in weekly_score:
        score = input("Enter week score: ")
        score.append(weekly_score)

    print(csa_average(weekly_score))


main()
