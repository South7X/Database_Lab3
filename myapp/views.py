from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Userinfo, Usertype, Bookhouse, Buyer, \
    Agencycomp, Agencyinfo, Decoration, Houseinfo, Housetype, \
    Ownership, Publishhouse, Starhouse
# Create your views here.
import time
import re

def register(request):
    status = 'Success!'
    username = ''
    password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        typ = request.POST.get('type')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        address = request.POST.get('address')
        dic = {"0":"buyer", "1":"agency"}
        usertype = Usertype(usertype_name=dic[typ], usertype_id=typ)
        usertype.save()
        if Userinfo.objects.filter(user_no=username):
            messages.error(request, '用户名已存在')
            return HttpResponseRedirect('/register/')
        if re.match(r'^d{11}$', phone) is None:
            messages.error(request, '手机号码格式错误')
            return HttpResponseRedirect('/register/')
        user = Userinfo(user_no=username,user_psw=password)
        user.usertype = usertype
        user.save()
        if int(typ) == 0:    # buyer
            length = Buyer.objects.count()
            buyer = Buyer(buyer_id=str(length + 1), buyer_name=name,
                          buyer_gender=sex, buyer_phone=phone)
            buyer.user_no = user
            buyer.save()
        else:   # agency
            length = Agencyinfo.objects.count()
            agen = Agencyinfo(agency_id=str(length + 1), agency_name=name, agency_gender=sex,
                              agency_phone=phone)
            if company != '':
                query = Agencycomp.objects.filter(company_name=company)
                flag = False
                for q in query:
                    comp = q
                    agen.agencycomp = comp
                    flag = True
                if flag is False:  # 新注册公司
                    comp_len = Agencycomp.objects.count()
                    comp_id = str(comp_len + 1)
                    comp = Agencycomp(company_name=company, company_id=comp_id, company_address=address)
                    comp.save()
                    agen.agencycomp = comp
            agen.user_no = user
            agen.save()
        request.session['username'] = username
        return redirect('/login/')
    else:
        return render(request, 'register.html')



def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        result = Userinfo.objects.filter(user_no=username)
        for user in result:
            if user.user_psw == password:
                request.session['username'] = username
                request.session['type'] = user.usertype_id

                return redirect('/index/')
            else:
                return HttpResponse("Password incorrect")
        return HttpResponse("It is not a user, %s" % username)

    return render(request,'login.html')


def index(request):
    username = request.session.get('username')
    typ = request.session.get('type')
    star_houses = []
    book_houses = []
    if typ == '0':
        buyer = Buyer.objects.get(user_no=username)
        star_list = Starhouse.objects.filter(buyer=buyer)
        book_list = Bookhouse.objects.filter(buyer=buyer)
        for s in star_list:
            star_houses.append(s.house)
        for b in book_list:
            book_houses.append(b.house)
    house_list = Houseinfo.objects.all()
    context = {'house_list': house_list, 'username':username, 'type':typ,
               'starhouses': star_houses, 'bookhouses': book_houses}
    return render(request, "index.html", context)


def logout(request):
    request.session.clear()
    return redirect('/login/')


def publish(request):
    if request.POST:
        house_name = request.POST.get('house_name')
        price = request.POST.get('price')
        size = request.POST.get('size')
        typ = request.POST.get('type')
        ownership = request.POST.get('ownership')
        decoration = request.POST.get('decoration')
        typ_dic = {'0':'一室', '1':'二室','2':'三室','3':'四室及以上'}
        ownership_dic = {'0': '商品房', '1':'公房', '2': '经适房', '3':'其他'}
        decoration_dic = {'0':'精装修','1':'普通装修','2':'毛胚房'}
        housetype = Housetype(housetype_id=typ, housetype_name=typ_dic[typ])
        housetype.save()
        houseowner = Ownership(ownership_id=ownership, ownership_type=ownership_dic[ownership])
        houseowner.save()
        deco = Decoration(decoration_id=decoration, decoration_type=decoration_dic[decoration])
        deco.save()

        length = Houseinfo.objects.count()
        house = Houseinfo(house_id=str(length+1), house_name=house_name, house_price=price, house_size=size)
        house.housetype = housetype
        house.decoration = deco
        house.ownership = houseowner
        house.save()

        username = request.session.get('username')
        alist = Agencyinfo.objects.filter(user_no=username)
        for a in alist:
            agency = a
        tim = time.strftime("%Y-%m-%d", time.localtime())
        pub = Publishhouse(publish_time=tim)
        pub.house = house
        pub.agency = agency
        pub.save()

        return redirect('/index/')
    return render(request, 'publish.html')


def mystar(request):
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    if buyer is not None:
        star_list = Starhouse.objects.filter(buyer=buyer)
        return render(request, 'mystar.html', {'star_list':star_list})
    return render(request, 'mystar.html')


@csrf_exempt
def starhouse(request):
    housename = request.POST.get('housename')
    house = Houseinfo.objects.get(house_name=housename)
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    tim = time.strftime("%Y-%m-%d", time.localtime())
    star = Starhouse(buyer=buyer, house=house, star_time=tim)
    star.save()
    return HttpResponse('success')

@csrf_exempt
def concelstar(request):
    housename = request.POST.get('housename')
    house = Houseinfo.objects.get(house_name=housename)
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    Starhouse.objects.get(house=house, buyer=buyer).delete()
    return render(request, 'mystar.html')


def book(request):
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    if buyer is not None:
        book_list = Bookhouse.objects.filter(buyer=buyer)
        return render(request, 'book.html', {'book_list':book_list})
    return render(request, 'book.html')


@csrf_exempt
def bookhouse(request):
    housename = request.POST.get('housename')
    house = Houseinfo.objects.get(house_name=housename)
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    tim = time.strftime("%Y-%m-%d", time.localtime())
    book = Bookhouse(buyer=buyer, house=house, book_time=tim)
    book.save()
    return render(request, 'index.html')


@csrf_exempt
def concelbook(request):
    housename = request.POST.get('housename')
    house = Houseinfo.objects.get(house_name=housename)
    username = request.session.get('username')
    buyer = Buyer.objects.get(user_no=username)
    Bookhouse.objects.get(house=house, buyer=buyer).delete()
    return render(request, 'book.html')


def bookrecord(request):
    username = request.session.get('username')
    agency = Agencyinfo.objects.get(user_no=username)
    pub_list = Publishhouse.objects.filter(agency=agency)
    all_houses = []
    book_houses = []
    for pub in pub_list:
        all_houses.append(pub.house)
    book_list = Bookhouse.objects.all()
    for book in book_list:
        if book.house in all_houses:
            tim = book.book_time
            buyer = book.buyer.buyer_name
            phone = book.buyer.buyer_phone
            house = book.house.house_name
            book_houses.append({'house_name':house, 'buyer_name':buyer, 'buyer_phone':phone, 'book_time':tim})
    return render(request, 'bookrecord.html', context={'books': book_houses})


def mypublish(request):
    username = request.session.get('username')
    agency = Agencyinfo.objects.get(user_no=username)
    if agency is not None:
        pub_list = Publishhouse.objects.filter(agency=agency)
        return render(request, 'mypublish.html', {'pub_list': pub_list})
    return render(request, 'mypublish.html')


@csrf_exempt
def concelpublish(request):
    housename = request.POST.get('housename')
    house = Houseinfo.objects.get(house_name=housename)
    username = request.session.get('username')
    agency = Agencyinfo.objects.get(user_no=username)
    Publishhouse.objects.get(house=house, agency=agency).delete()
    if Bookhouse.objects.filter(house=house):
        Bookhouse.objects.filter(house=house).delete()
    if Starhouse.objects.filter(house=house):
        Starhouse.objects.filter(house=house).delete()
    Houseinfo.objects.get(house_name=house.house_name).delete()
    return render(request, 'mypublish.html')