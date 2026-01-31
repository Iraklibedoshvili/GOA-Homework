#2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ
#  ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას 
# გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის
#  მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები 
# snake_case-ის სტილში)


Book1 = 47
Book2 =39
Book3 =58     #normal prize
Book4 =27
Book5 =34

BOOK1 = 27
BOOK2 =29
BOOK3 =45       #sale prize
BOOK4 =12
BOOK5 =19



normalprize_minus_saleprize1 = Book1-BOOK2
normalprize_minus_saleprize2 = Book2-BOOK2
normalprize_minus_saleprize3 = Book3-BOOK3                 #normal prize - sale prize
normalprize_minus_saleprize4 = Book4-BOOK4
normalprize_minus_saleprize5 = Book5-BOOK5


print(normalprize_minus_saleprize1)
print(normalprize_minus_saleprize2)
print(normalprize_minus_saleprize3)
print(normalprize_minus_saleprize4)
print(normalprize_minus_saleprize5)