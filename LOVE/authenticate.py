import os
import getpass


os.system('cls')
print('\n' * 10 + ' ' * 62 + ' Welcome My Sister ')

firstName = input('\n\n\n\n' + ' ' * 66 + "Nhập Họ :\n\n" + ' ' * 78)

if (firstName == 'Phan' or firstName == 'phan' ):
    lastName = input('\n\n' + ' ' * 66 + "Nhập Tên (thích thì thêm tên đệm ko thích thì thui :D ) :\n\n" + ' ' * 77)
    if (lastName == 'Tam' or lastName =='Tue Tam' or lastName == 'tam' ):
        pin = getpass.getpass('\n\n' + ' ' * 50 + "Your birthday (for example : 2309 ) password not show ?  :\n\n" + ' ' * 78)
        if (pin == '2901' or pin =='29012003'):
            import HPBD
        else:
            print('\n' * 4 + ' ' * 73 + 'Access Denided!')
            print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
            print('\n\n' + ' ' * 73 + 'Copyright 2021')
            print('\n' * 4)
    else:
        print('\n' * 4 + ' ' * 73 + 'Access Denided!')
        print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
        print('\n\n' + ' ' * 73 + 'Copyright 2021')
        print('\n' * 4)
else:
    print('\n' * 4 + ' ' * 73 + 'Access Denided!')
    print('\n\n' + ' ' * 68 + 'A Heart Filled With Love')
    print('\n\n' + ' ' * 73 + 'Copyright 2021')
    print('\n' * 4)