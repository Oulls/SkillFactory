import random

ch=input('X или 0?\n')
print('Пример ввода координаты:B1')
net={'A0':'-' , 'A1':'-' , 'A2':'-' , 'B0':'-' ,'B1':'-' ,'B2':'-' ,'C0':'-' ,'C1':'-' ,'C2':'-' }
All = ['A0','A1','A2','B0','B1','B2','C0','C1','C2','']
print(' / A B C \n 0 - - - \n 1 - - - \n 2 - - -')
if ch == 'X':
    for i in range(0,6):
        if (net['A0']=='X' and net['B0']=='X' and net['C0']=='X') or (net['A0']=='X' and net['A1']=='X' and net['A2']=='X') or (net['A2']=='X' and net['B2']=='X' and net['C2']=='X') or (net['C0']=='X' and net['C1']=='X' and net['C2']=='X') or (net['A0']=='X' and net['B1']=='X' and net['C2']=='X') or (net['C0']=='X' and net['B1']=='X' and net['A2']=='X') or (net['B0']=='X' and net['B1']=='X' and net['B2']=='X') or (net['A1']=='X' and net['B1']=='X' and net['C1']=='X'):
            print('Ты победил!')
            break
        elif (net['A0']=='0' and net['B0']=='0' and net['C0']=='0') or (net['A0']=='0' and net['A1']=='0' and net['A2']=='0') or (net['A2']=='0' and net['B2']=='0' and net['C2']=='0') or (net['C0']=='0' and net['C1']=='0' and net['C2']=='0') or (net['A0']=='0' and net['B1']=='0' and net['C2']=='0') or (net['C0']=='0' and net['B1']=='0' and net['A2']=='0') or (net['B0']=='0' and net['B1']=='0' and net['B2']=='0') or (net['A1']=='0' and net['B1']=='0' and net['C1']=='0'):
            print('Ты проиграл')
            break
        else:
            input_var=input('Введите координаты:')
            if net[input_var] == '-':
                for j in range(len(All)-1):
                    if All[j] == input_var:
                        All.pop(j)
                net[input_var]='X'            
                print(' / A B C \n 0 ', net['A0'], net['B0'], net['C0'], '\n 1 ', net['A1'], net['B1'], net['C1'], '\n 2', net['A2'], net['B2'], net['C2'])
                rand_var=random.choices(All[0:-1])
                for k in range(len(All)-1):
                    if All[k] == rand_var[0]:
                        All.pop(k)
                for el in rand_var:
                    str_rand_var=str(el)
                print('Ход rand_var:')
                net[str_rand_var]='0'
                '''
                print(All)
                print(rand_var)
                '''
                print(' / A B C \n 0 ', net['A0'], net['B0'], net['C0'], '\n 1 ', net['A1'], net['B1'], net['C1'], '\n 2', net['A2'], net['B2'], net['C2']) 
            else:
                print('Сюда поставить нельзя')
if ch == '0':
    for i in range(0,6):
        if (net['A0']=='X' and net['B0']=='X' and net['C0']=='X') or (net['A0']=='X' and net['A1']=='X' and net['A2']=='X') or (net['A2']=='X' and net['B2']=='X' and net['C2']=='X') or (net['C0']=='X' and net['C1']=='X' and net['C2']=='X') or (net['A0']=='X' and net['B1']=='X' and net['C2']=='X') or (net['C0']=='X' and net['B1']=='X' and net['A2']=='X') or (net['B0']=='X' and net['B1']=='X' and net['B2']=='X') or (net['A1']=='X' and net['B1']=='X' and net['C1']=='X'):
            print('Ты проиграл')
            break
        elif (net['A0']=='0' and net['B0']=='0' and net['C0']=='0') or (net['A0']=='0' and net['A1']=='0' and net['A2']=='0') or (net['A2']=='0' and net['B2']=='0' and net['C2']=='0') or (net['C0']=='0' and net['C1']=='0' and net['C2']=='0') or (net['A0']=='0' and net['B1']=='0' and net['C2']=='0') or (net['C0']=='0' and net['B1']=='0' and net['A2']=='0') or (net['B0']=='0' and net['B1']=='0' and net['B2']=='0') or (net['A1']=='0' and net['B1']=='0' and net['C1']=='0'):
            print('Ты победил!')
            break
        else:
            input_var=input('Введите координаты:')
            if net[input_var] == '-':
                for j in range(len(All)-1):
                    if All[j] == input_var:
                        All.pop(j)
                net[input_var]='0'            
                print(' / A B C \n 0 ', net['A0'], net['B0'], net['C0'], '\n 1 ', net['A1'], net['B1'], net['C1'], '\n 2', net['A2'], net['B2'], net['C2'])
                rand_var=random.choices(All[0:-1])
                for k in range(len(All)-1):
                    if All[k] == rand_var[0]:
                        All.pop(k)
                for el in rand_var:
                    str_rand_var=str(el)
                print('Ход rand_var:')
                net[str_rand_var]='X'
                '''
                print(All)
                print(rand_var)
                '''
                print(' / A B C \n 0 ', net['A0'], net['B0'], net['C0'], '\n 1 ', net['A1'], net['B1'], net['C1'], '\n 2', net['A2'], net['B2'], net['C2']) 
            else:
                print('Сюда поставить нельзя')
    

    
