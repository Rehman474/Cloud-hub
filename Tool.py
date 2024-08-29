name =str(input('Abdul REHmAn :  '))
fav_1 =int(input('9 : '))
fav_2 =int(input('4 : '))
fav_3 =int(input('18 :'))
print(f"~~Hello {name}! lets explore your favourite number ")
print('~~Lets,explore whether your favourite numbers is even or odd .Lets gooooooo!!')
print(f"your first favourite number is {fav_1} which is an {'even number' if fav_1 % 2 == 0 else 'odd number' } ") 
print(f"your second favourite number is {fav_2} which is an {'even number' if fav_2 % 2 == 0 else 'odd number'} ")
print(f"your third favoruite number is {fav_3} which is an {'even number' if fav_3 % 2 == 0 else 'odd number' } ")
print('~~Now,lets explore the square of your favoruite numbers.Lets gooooooo!!' )
print(f"your first favourite number is {fav_1} and its square is : ({fav_1},{fav_1 ** 2})")
print(f"your second favourite number is {fav_2} and its square is : ({fav_2},{fav_2 ** 2})")
print(f"your third favourite number is {fav_3} and its square is : ({fav_3},{fav_3 ** 2})")
print('~~Its time to check the sum of your favourite number . Lets gooo!')
sum= fav_1 + fav_2 + fav_3
print(f'~~WOW, the total sum of your favourite number is "{sum} which is your lucky number')
print('''~~I hope that you had fun while exploring my program.
~~Have a nice day
~~Good Bye            ''') 