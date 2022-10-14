from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession


def signup(request):
    # 단순 주소창에 입력했을때 'GET' (경로이동 시)
    if request.method == 'GET':
        return render(request, 'signup.html')
        
    # 회원가입 진행 (template에서 POST된 요청)
    elif request.method == 'POST':  
    
        # 아래의 변수들은 signup.html안에 input박스에서 가져온 변수(name으로 정의돼있음)
        username = request.POST.get('username')  
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        User.objects.create_user(username=username, password=password)  
        
        return redirect('user:login')
        


def login(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'login.html')
    elif request.method == 'POST':  # 로그인 요청
        username = request.POST.get('username')    # username은 login.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

    #로그인 GET or POST 작업 후 이 다음코드 진행

        if user is not None:  # user 가 존재하지 않는게 아니면 = if user (user 라면!)
            # 장고에서 제공해주는 login 기능을 as로 재정의 후 이용
            loginsession(request, user)
            return redirect('user:home')   #로그인 성공시 입력된 user 값으로 로그인 흐 user/ 로 경로이동
        else:
            return redirect('user:login')



def home(request):
    if request.user:
        return render(request, 'home.html')
    else:
        return HttpResponse('사용자가 아닙니다.')