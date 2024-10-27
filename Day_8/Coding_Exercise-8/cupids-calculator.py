print(r'''
 .,,. .,,.
:XXXX,XXXX:                   .SSSSSSS'
'XXXXXXXXX'                 .SSSSSSSS,WW:,  .-'':,.
 ':XXXXX:'                .SSSSSSSSSS:WWW:,       '::,
   'XXX'                 .SSSSSSSSS,WWW( )WW       '::,  '////
    ':'                  SSSSSSSSSSSS'WWWWWWWD        '::,////
                   ,.   'SSSSSSS(((SSSWWWWW<         ,WW//:.'.W.
                 ,'((()   SSSSSS(((WWWWWWWWWW)        //'W,:WWWW'
               ,'(((((()   SSSSSS((WWWWWWWWWW)      //   'WWW,WWW
            .,'(((((((())    SSSSWWWWWWWWWWW'     //     .WWWWW:,
         .,'((((((((((())),     SSWWWWWWWWWW'    //      ,WWWW' ':,
     .,'((((((((((((((())))),.,,,,WWWWWWWWWW:, //       ,WWWWW'  ':
'((((((((((((((((((((()))))WWWWWWWWWWWWWVVVV//WWWWW:,.,WWWWW'    :
   '((((((((((((((((((()))WWWWWWWWWWWWWWVVVVVVWWWWWWWWWWWWW'    '
     '((((((((((((((((()))/WWWWWWWWWWWWWVVVVVVVWWWWWWWWWWWW'
       '(((((((((((((())(()(WWWWWWWWW.VVVVVVVWWWWWWWWWWW:'
           '((((((((())) ()(WWWWWW.VVVVVVV'WWWWWWW''      .,,. .,,.
              '((((()))   ((WW,VVVVVVVVV'WWWWWWWWW       :XXXX,XXXX:
                           WVVVVVVVVVV'WWWWWWWW:'       'XXXXXXXXX'
     .,,. .,,.             VVVVVVVVV'WWWWWWWWWW          ':XXXXX:'
    :XXXX,XXXX:          .WVVVVVVV'WWWWWWWWWWWW            'XXX'
    'XXXXXXXXX'         .WWW----',WWWWWWWWWWWW:             ':'
     ':XXXXX:'        (())))WWWWWWWWWWWWWWWWW'
       'XXX'         ((())))))WWWWWWWWWWWWWW'
        ':'         ((()))))))))WWWWWWWWWWW'
                    ()WWWWWW))))))))))))))))
                    :WWWWWWWWW))))))))))))))     .,,. .,,.
                    WWWWWWWWWWW)))))))WWWWW.    :XXXX,XXXX:
                   :WWWWWWWWWW')))))WWWWWWWW.   'XXXXXXXXX'
                   WWWWWWWWWW'  'WWWWWWWWWWWW    ':XXXXX:'
         .,,:WWWW:,WWWWWWWWW'    'WWWWWWWWWWW      'XXX'
        ,WWWWWWWWWWWWWWWWWW'       'WWWWWWWWW       ':'
       ,WWWWWWWWWWWWWWWWWW'         'WWWWWWWW,
       WWWWWWW'   '':WWW:'           'WWWWWWWW
     .WWWWWWW'                      .WWWWWWWWW
     ''W'W'WW                      ,WWWWWWWWW'          .,,. .,,.
           ''                     ,WWWWWWWW'           :XXXX,XXXX:
           .,,. .,,.             .WWWWWW:'             'XXXXXXXXX'
          :XXXX,XXXX:         .WWWWWWW'                 ':XXXXX:'
          'XXXXXXXXX'         WWWWWW'                     'XXX'
           ':XXXXX:'           WWWWW'                      ':'
             'XXX'              WWWW.
              ':'               'WWWWW,
                                 '' ''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      ''')

print("Welcome To Cupid’s Calculator!")
print(" ")

partner_1 = str(input("Enter Name Of The First Individual In The Couple:\n"))
partner_2 = str(input("Enter Name Of The Second Individual In The Couple:\n"))
print(" ")

def calculate_love_score(partner_1,partner_2):
    match_percent = 0
    couple_name = (partner_1 + partner_2).upper()
    for char in couple_name:
        if char in ['T','R','U','E']:
            match_percent += 1

    match_percent *= 10

    for char in couple_name:
        if char in ['L','O','V','E']:
            match_percent += 1

    match_percent = (match_percent/110)*100

    print(f"Your Match Percentage is {match_percent}% .")
    if match_percent > 70 :
        print("You Were Meant To Be Soulmates!")
    elif 50 <= match_percent < 70 :
        print("If Your Love Is True Your Relatioship Will Survive!")
    else:
        print("Be Patient! The Right Person Will Come Along When The Time Is Right.")
        
    
    
calculate_love_score(partner_1, partner_2)