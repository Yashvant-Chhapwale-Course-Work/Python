def calculate_love_score(name1,name2):
    match_percent = 0
    for name1.upper() in ['T','R','U','E'] or name2.upper() in ['T','R','U','E']:
        match_percent += 1

    match_percent *= 10
    for name1.upper() in ['L','O','V','E'] or name2.upper() in ['L','O','V','E']:
        match_percent += 1
        
    print(match_percent)
    
calculate_love_score("Kanye West", "Kim Kardashian")