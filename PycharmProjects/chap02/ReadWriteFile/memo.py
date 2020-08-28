def write_your_memo(mode) :
    f = open('memo.txt', mode)
    memo = input('Input your memo > ') + '\r\n'
    f.write(memo)
    f.close()

mode = input('w : New memo note, a : Append your memo ?')

if mode == 'w' or mode == 'a' :
    write_your_memo(mode)
    if mode == 'w' :
        print('Wrote your memo to a new note\n')
    else :
        print('Appended your memo\n')
else :
    print('Wrong input')

