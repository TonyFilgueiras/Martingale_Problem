from random import randint
from Cores import cores
import pandas as pd

for j in range(800):
    df = pd.read_csv("coin_flip_results.csv")
    six = df['Times 6 streak appeared']
    seven = df['Times 7 streak appeared']
    eight = df['Times 8 streak appeared']
    nine = df['Times 9 streak appeared']
    ten = df['Times 10 streak appeared']
    coin_side = ['Heads', 'Tails']
    streak_count = 1
    previous_flip = ' '



    def checking_streaks(number_of_streaks, number:int, streak_count,contained_six,  count=0):
        if streak_count >= number:
            number_of_streaks += 1 
            count += 1
        if count >0:
            contained_six += 1
        return number_of_streaks, contained_six

    def applying_color(new_flip):
        if new_flip == 'Heads':
            color = '\033[31m'
        else:
            color = '\033[32m'
        return color

    def percentage_calculator(number_of_streaks,contained, total = df['Total games played']):
        if number_of_streaks > 0:
            contained += 1
        percentage = ((contained/total) * 100).round(2)
        return percentage, contained


    # SCRIPT

    contained_six=contained_seven=contained_eight=contained_nine=contained_ten=0 #variable made to verify if a game contained a certain amount of streak

    # 200 coin toss sequence
    for i in range(200):
        new_flip = coin_side[randint(0,1)]
        color = applying_color(new_flip)
        if new_flip == previous_flip:
            streak_count += 1
        else:
            streak_count = 1
        print(f'{streak_count} {color}{new_flip}', cores('nula'))
        previous_flip = new_flip
        six, contained_six = checking_streaks(six, 6, streak_count, contained_six)
        seven, contained_seven = checking_streaks(seven, 7, streak_count, contained_seven)
        eight, contained_eight = checking_streaks(eight, 8, streak_count, contained_eight)
        nine, contained_nine = checking_streaks(nine, 9, streak_count, contained_nine)
        ten, contained_ten = checking_streaks(ten, 10, streak_count, contained_ten)

    df['Total games played'] += 1


    # Calculating percentages and averages
    df['Contained a 6 streak %'], df['Contained a 6 streak'] = percentage_calculator(contained_six, df['Contained a 6 streak'])
    df['Contained a 7 streak %'], df['Contained a 7 streak'] = percentage_calculator(contained_seven, df['Contained a 7 streak'])
    df['Contained a 8 streak %'], df['Contained a 8 streak'] = percentage_calculator(contained_eight, df['Contained a 8 streak'])
    df['Contained a 9 streak %'], df['Contained a 9 streak'] = percentage_calculator(contained_nine, df['Contained a 9 streak'])
    df['Contained a 10 streak %'], df['Contained a 10 streak'] = percentage_calculator(contained_ten, df['Contained a 10 streak'])
    df["6 streak average"] = (df['Times 6 streak appeared'] / df ['Total games played']).round(2)
    df["7 streak average"] = (df['Times 7 streak appeared'] / df ['Total games played']).round(2)
    df["8 streak average"] = (df['Times 8 streak appeared'] / df ['Total games played']).round(2)
    df["9 streak average"] = (df['Times 9 streak appeared'] / df ['Total games played']).round(2)
    df["10 streak average"] = (df['Times 10 streak appeared'] / df ['Total games played']).round(2)

    df = df[["Times 6 streak appeared","Contained a 6 streak", "Contained a 6 streak %",'6 streak average','Times 7 streak appeared','Contained a 7 streak','Contained a 7 streak %','7 streak average','Times 8 streak appeared','Contained a 8 streak','Contained a 8 streak %','8 streak average','Times 9 streak appeared','Contained a 9 streak','Contained a 9 streak %','9 streak average','Times 10 streak appeared','Contained a 10 streak','Contained a 10 streak %','10 streak average','Total games played']]

    df.to_csv("coin_flip_results.csv", index=False)
    print(df)
