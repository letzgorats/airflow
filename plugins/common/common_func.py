def get_sftp():
    print("sftp 작업을 시작합니다")


def register(name,gender,*args):
    print(f'이름:{name}')
    print(f'성별:{gender}')
    print(f'기타옵션들:{args}')

def register2(name,gender,*args,**kwargs):
    print(f'이름:{name}')
    print(f'성별:{gender}')
    print(f'기타옵션들:{args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)