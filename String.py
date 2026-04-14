import utils.session
m="hello world"
new_m=m.replace('world','panda')
print(m)
print(new_m)

gretting='hello'
name='panda'
print(gretting+' '+name)
# msg='{}, {}. Welcome!'.format(gretting,name)
# msg=f'{gretting}, {name}. Welcome!'
msg=f'{gretting}, {name.upper()}. Welcome!'
print(msg)
print(dir(msg))
print(help(str))


#comment on python

msg1='miki\'s'
msg2="miki\'s"
msg3="""miki\'suehfbfb
kijdhfghgfn"""

# print(len(msg1))
# print(msg1[11])
# print(msg1[0:4])
# print(msg1[:5])
# print(msg1[6:])
# print(msg2)
# print(msg3)
print(msg1.lower())
print(msg1.upper())
print(msg1.count('i'))
print(m.find('world'))
print(m.find('people'))
print(m)