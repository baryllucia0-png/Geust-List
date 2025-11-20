guests=['Rose','Lucy','Carol']
print(guests)

#inviting each guest to the dinner
print('Hi there',guests[0],'i am inviting you for dinner')
print('Hi there',guests[1],'i am inviting you for dinner')
print('Hi there',guests[2],'i am inviting you for dinner')
#naming the guest who could not make it

print(guests[1],'had an emergency and could not make it')
#replacing the guest with an emergency

guests[1]='Baryl'
print(guests)

#printing a new invitation for each available guest
print('Hi there',guests[0],'i am inviting you for dinner')
print('Hi there',guests[1],'i am inviting you for dinner')
print('Hi there',guests[2],'i am inviting you for dinner')

#informing guests that i have found a bigger dinner table
print('Hey',guests[0],'i just found a bigger dinner table')
print('Hey',guests[1],'i just found a bigger dinner table')
print('Hey',guests[2],'i just gound a bigger dinner table')

#adding new guests
guests.insert(0,'Lucien')
guests.insert(2,'Delron')
guests.append('Marlene')
print(guests)

#printing new invitations for each guest
print('Hi',guests[0],'i am inviting you for dinner')
print('Hi',guests[1],'i am inviting you for dinner')
print('Hi',guests[2],'i am inviting you for dinner')
print('Hi',guests[3],'i am inviting you for dinner')
print('Hi',guests[4],'i am inviting you for dinner')
print('Hi',guests[5],'i am inviting you for dinner')


