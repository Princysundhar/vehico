# from django.http import HttpResponse
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from VECHI_CO_APP.models import *




#.......FORGOT PASSWORD

def forgot_password(request):
    return render(request,"forgot_password.html")

def forgot_password_post(request):
    email = request.POST['textfield2']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        # s.login("riss.princytv@gmail.com", "dnsb yopn jqxq hrko")
        s.login("demo@gmail.com", "dnsb yopn jqxq hrko")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "demo@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for Easy rent project"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('Email sended');window.location='/'</script>")
    return HttpResponse("<script>alert('Mail Incorrect');window.location='/'</script>")

def Login(request):
    return render(request, 'login_index.html')


def login_post(request):
    user = request.POST['textfield']
    pas = request.POST['textfield2']
    res = login.objects.filter(username=user, password=pas)
    if res.exists():
        loginid = res[0].id
        request.session['logid'] = loginid
        request.session['lg'] = "lin"
        if res[0].usertype == 'admin':
            request.session['lid'] = res[0].id
            request.session['lg'] = "lin"
            return redirect('/admin_home')
        elif res[0].usertype == "service_provider":
            return redirect('/service_provider_home')
        else:

            return HttpResponse('<script>alert("invalid details");window.location="/"</script>')
    return HttpResponse('<script>alert("invalid user");window.location="/"</script>')


def logout(request):
    request.session['lg'] = ""
    return redirect('/')


def admin_home(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    return render(request, 'admin/admin_index.html')


def serviceprovider_home(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    return render(request, 'service provider/provider_indexx.html')

# SERVICE MANAGEMENT..........

def add_service(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    return render(request, 'admin/add service.html')


def add_service_post(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    s = request.POST['select']

    if service.objects.filter(service_name__iexact=s).exists():
        return HttpResponse("<script>alert('Already Exist!'); location='/add_service'</script>")

    obj = service()
    obj.service_name = s
    obj.save()
    return HttpResponse('<script>alert("added sucsessfully");window.location="/add_service#aa"</script>')


def view_service(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = service.objects.all()
    return render(request, 'admin/view service.html', {'data': res})


def update_service(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = service.objects.get(id=id)
    return render(request, 'admin/update service.html', {'id': id, 'data': res})


def update_service_post(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    u = request.POST['select']
    service.objects.filter(id=id).update(service_name=u)
    return HttpResponse('<script>alert("updated sucsessfully");window.location="/view_service#aa"</script>')

def delete_service(request,id):
    if request.session['lg'] != "lin":
        return redirect('/')
    service.objects.get(id=id).delete()
    return HttpResponse('<script>alert("Deleted sucsessfully");window.location="/view_service#aa"</script>')


def view_serviceprovider_and_verify(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = serviceprovider.objects.filter(LOGIN__usertype='pending')
    return render(request, 'admin/view sevice provider.html', {'data': res})



def approve_serviceprovider(request, ajoy):
    if request.session['lg'] != "lin":
        return redirect('/')
    login.objects.filter(id=ajoy).update(usertype='service_provider')
    return HttpResponse('<script>alert("approved sucsessfully");window.location="/view_serviceprovider_and_verify#aa"</script>')


def reject_serviceprovider(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    login.objects.filter(id=id).update(usertype='rejected')
    return HttpResponse('<script>alert("rejected sucsessfully");window.location="/view_serviceprovider_and_verify#aa"</script>')


def view_verified_serviceprovider(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = serviceprovider.objects.filter(LOGIN__usertype='service_provider')
    return render(request, 'admin/view verified service provider.html', {'data': res})


def view_users(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = user.objects.all()
    return render(request, 'admin/view user.html', {'data': res})


def view_complaint(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = complaint.objects.all()
    return render(request, 'admin/view complaint.html', {'data': res})

def send_reply(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    return render(request, "admin/send reply.html", {'id': id})


def send_reply_post(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    r = request.POST['textarea']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    complaint.objects.filter(id=id).update(reply=r, replydate=d)
    return HttpResponse('<script>alert("reply send sucsessfully");window.location="/view_complaint"</script>')


def view_feedback(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = feedback.objects.all()
    return render(request, 'admin/view feedback.html', {'data': res})


def view_rating_and_review(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = rating.objects.all()
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    data = []

    for rt in res:
        print(rt)
        a = float(rt.rating)
        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })
        print(data, "data")

    return render(request, 'admin/view rating and review.html', {'data': res})


def change_password(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    return render(request, 'admin/change password.html')

def change_password_post(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    old = request.POST['oldpsd']
    new = request.POST['newpsd']
    con = request.POST['conform']
    nirmal = login.objects.filter(password=old)
    if nirmal.exists():
        if nirmal[0].usertype == 'admin':
            if new == con:
                login.objects.filter(id=request.session['lid']).update(password=con)
                return HttpResponse('<script>alert("password updated sucsessfully");window.location="/"</script>')
            else:
                return HttpResponse('<script>alert("error not updated");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("error go back");window.location="/"</script>')


#...SERVICE PROVIDER....................

def register_servuceprovider(request):
    return render(request, "provider_register.html")


def register_servuceprovider_post(request):
    name = request.POST['textfield2']
    contactnumber = request.POST['textfield3']
    Lattitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    place = request.POST['textfield10']
    email = request.POST['textfield2']
    password = request.POST['textfield6']

    obj = login()
    obj.username = email
    obj.password = password
    obj.usertype = 'pending'
    obj.save()

    obj2 = serviceprovider()
    obj2.service_name = name
    obj2.contactnumber = contactnumber
    obj2.lattitude = Lattitude
    obj2.longitude = longitude
    obj2.place = place
    obj2.email = email
    obj2.LOGIN = obj
    obj2.save()
    return HttpResponse('<script>alert("Registered successfully");window.location="/"</script>')


def view_profile_and_update(request):
    res = serviceprovider.objects.get(LOGIN_id=request.session['logid'])
    return render(request, 'service provider/View profile.html', {'data': res})


def view_profile_and_update_post(request, id):
    if request.session['lg'] != "lin":
        return redirect('/')
    name = request.POST['textfield2']
    contactnumber = request.POST['textfield3']
    Lattitude = request.POST['textfield4']
    longitude = request.POST['longitude']
    place = request.POST['textfield5']
    email = request.POST['textfield6']
    serviceprovider.objects.filter(id=id).update(service_name=name, contactnumber=contactnumber, lattitude=Lattitude,
                                                 longitude=longitude, place=place, email=email)
    return HttpResponse('<script>alert("updated successfully");window.location="/view_profile_and_update"</script>')


def provider_add_services(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    ser = service.objects.all()
    return render(request, 'service provider/view_services.html', {'data': ser})


def provider_add_own_service(request,id):
    data = service.objects.all()
    return render(request,"service provider/add_own_service.html",{"data":data,"id":id})


def provider_own_service_post(request,id):
    if request.session['lg'] != "lin":
        return redirect('/')
    sid = request.POST['select']
    amount = request.POST['textfield']
    obj = ownservice()
    obj.SERVICE_id = sid
    obj.SERVICEPROVIDER = serviceprovider.objects.get(LOGIN_id=request.session['logid'])
    obj.amount = amount
    obj.save()
    return HttpResponse("<script>alert('ADDED SUCESSFULLY');window.location='/provider_add_services'</script>")


def view_payment_history(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = payment.objects.all()
    return render(request, "service provider/view payment history.html", {"data": res})


def view_previous_history(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    res = booking.objects.filter(date__lt=d)
    print(res,d)
    return render(request, "service provider/view previous history.html", {"data": res})



def view_request(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = booking.objects.all()
    return render(request, "service provider/view request.html", {"data": res})

def approve_request(request,id):
    booking.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert('APPROVED SUCESSFULLY');window.location='/view_request'</script>")

def reject_request(request,id):
    booking.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('REJECTED SUCESSFULLY');window.location='/view_request'</script>")

def updation_completion_status(request,id):
    return render(request,"service provider/view time.html",{"id":id})

def updation_completion_status_post(request,id):
    time=request.POST["textfield"]
    booking.objects.filter(id=id).update(completionstatus=time)

    return HttpResponse("<script>alert('UPDATE COMPLETION STATUS ');window.location='/view_request'</script>")

def service_provider_change_password(request):
    return render(request,"service provider/change password.html")

def service_provider_change_password_post(request):
    old = request.POST['oldpsd']
    new = request.POST['newpsd']
    con = request.POST['conform']
    nirmal = login.objects.filter(id=request.session['logid'])
    nirmal=nirmal[0]
    if nirmal.password==old:
        if new == con:
            login.objects.filter(id=nirmal.id).update(password=con)
            return HttpResponse('<script>alert("password updated sucsessfully");window.location="/"</script>')
        else:
            return HttpResponse('<script>alert("error not updated");window.location="/service_provider_change_password"</script>')

    else:
        return HttpResponse('<script>alert("error go back");window.location="/service_provider_change_password"</script>')


def view_review_and_rating(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = rating.objects.all()
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    data = []

    for rt in res:
        print(rt)
        a = float(rt.rating)
        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            data.append({
                'USER': rt.USER,
                'SERVICE': rt.SERVICE,
                'review': rt.review,
                'date': rt.date,
                'rating': ar,

            })
        print(data, "data")

    return render(request, "service provider/view review and rating.html", {"data": data})


def provider_view_services(request):
    if request.session['lg'] != "lin":
        return redirect('/')
    res = ownservice.objects.filter(SERVICEPROVIDER__LOGIN=request.session['logid'])
    return render(request, "service provider/View service.html", {"data": res})
def delete_provider_service(request, id):
    ownservice.objects.get(id=id).delete()
    return  HttpResponse("<script>alert('DELETE SUCESSFULLY');window.location='/provider_view_services'</script>")



#............................................................................. ANDROID(USER)

def and_login(request):
    uname=request.POST["usn"]
    pword=request.POST["psw"]
    res = login.objects.filter(username=uname, password=pword, usertype='user')
    if res.exists():
        return JsonResponse({'status': 'ok', 'lid': res[0].id,'type':res[0].usertype})
    else:
        return JsonResponse({'status': 'no'})


def and_signup(request):
    name=request.POST["nme"]
    contact=request.POST["con_no"]
    email=request.POST["e_mail"]
    pword=request.POST["pass"]
    log = login()
    log.password=pword
    log.username=email
    log.usertype = 'user'
    log.save()
    obj = user()
    obj.username = name
    obj.contact = contact
    obj.Email = email
    obj.LOGIN = log
    obj.save()
    return JsonResponse({'status': 'ok'})


def and_view_service_provider(request):
    ser = serviceprovider.objects.filter(LOGIN__usertype='service_provider')
    li = []
    for i in ser:
        li.append({'id': i.id,
                   'nme': i.service_name,
                   'con': i.contactnumber,
                   'eml': i.email,
                   'lat':i.lattitude,
                   'lon':i.longitude,
                   'plc':i.place })
    print(li)
    return JsonResponse({'status': 'ok', 'data': li})


def and_view_booking(request):
    lid = request.POST['lid']
    res=booking.objects.filter(USER__LOGIN=lid,completionstatus='Done')
    li = []
    for i in res:
        li.append(
            {
                'id': i.id,
                'service': i.OWNSERVICE.SERVICE.service_name,
                'date': i.date,'payment':i.paymentstatus,
                'note':i.note,
                'status':i.completionstatus,
                'latitude':i.lattitude,
                'longitude':i.longitude,
                'amount':i.amount
            }
        )
    print(li)
    return JsonResponse({'status': 'ok', 'data': li})

def and_send_complaint(request):
    lid = request.POST['lid']
    comp = request.POST['complaint']

    obj = complaint()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    obj.complaint = comp
    obj.reply = 'pending'
    obj.replydate = 'pending'

    obj.save()

    return JsonResponse({'status': 'ok'})

def and_view_service(request):
    id = request.POST['id']
    res = service.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "sid":i.id,
                "service_name":i.service_name
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_view_reply(request):
    sid = request.POST['sid']
    res = complaint.objects.filter(SERVICEPROVIDER=sid)
    ar = []
    for i in res:
        ar.append(
            {
                'cid': i.id,
                "complaint": i.complaint,
                "compliant_date": i.date,
                "replay": i.reply,
                "replay_date": i.replydate,
            }
        )
    return JsonResponse({"status":"ok","data":ar})




def and_send_feedback(request):
    lid = request.POST['lid']
    fed= request.POST['feedback']
    # rat= request.POST['rating']

    obj = feedback()
    obj.feedbacks = fed
    obj.date = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()


    return JsonResponse({'status': 'ok'})




def and_book_service(request):
    lid = request.POST['lid']
    sid = request.POST['sid']
    req = request.POST['note']
    amt = request.POST['amount']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    obj = booking()
    obj.OWNSERVICE_id = sid
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    obj.status = 'pending'
    obj.paymentstatus = 'pending'
    obj.completionstatus = 'pending'
    obj.lattitude = latitude
    obj.longitude = longitude
    obj.note = req
    obj.amount =amt
    obj.save()
    return JsonResponse({"status":"ok"})

def android_send_rating(request):
    rate = request.POST['rate']
    review = request.POST['review']
    lid = request.POST['lid']
    sid = request.POST['sid']
    obj = rating()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.rating = rate
    obj.date = datetime.datetime.now().strftime('%d/%m/%Y-%H/%M/%S')
    obj.review = review
    obj.SERVICE_id = sid
    obj.save()
    return JsonResponse({"status":"ok"})


def android_offline_payment(request):
    lid = request.POST['lid']
    # mode = request.POST['mode']
    amount = request.POST['amount']
    bid = request.POST['bid']
    obj = payment()
    obj.payment_status = 'offline'
    obj.amount = amount
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.BOOKING = booking.objects.get(id=bid)
    obj.save()
    booking.objects.filter(id=bid).update(paymentstatus='offline')
    return JsonResponse({"status":"ok"})


# def android_online_payment(request):
#     lid = request.POST['lid']
#     # mode = request.POST['mode']
#     amount = request.POST['amount']
#     bid = request.POST['bid']
#     obj = payment()
#     obj.payment_status = 'online'
#     obj.amount = amount
#     obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
#     obj.USER = user.objects.get(LOGIN=lid)
#     obj.BOOKING = booking.objects.get(id=bid)
#     obj.save()
#     booking.objects.filter(id=bid).update(paymentstatus='paid')
#
#
#     return JsonResponse({"status": "ok"})


# USER PAYMENT ...................



def android_make_payment(request):
    payment_mode = request.POST['mode']
    rid = request.POST['rid']
    booking.objects.filter(id=rid).update(payment_status=payment_mode)
    return JsonResponse({"status": "ok"})

# Bank Management..............

def android_add_bank(request):
    lid = request.POST['lid']
    logininstance = login.objects.get(id = lid)

    bank_name = request.POST['bank_name']
    account_no = request.POST['account_no']
    ifsc_code = request.POST['ifsc_code']
    amount = request.POST['amount']
    obj = bank()
    obj.bank_name = bank_name
    obj.account_no = account_no
    obj.IFSC_code = ifsc_code
    obj.amount = amount
    obj.LOGIN = logininstance
    obj.save()
    return JsonResponse({"status":"ok"})


def android_view_bank(request):
    lid = request.POST['lid']
    logininstance = login.objects.get(id = lid)
    res = bank.objects.filter(LOGIN = logininstance)
    ar = []
    for i in res:
        ar.append(
            {
                "id": i.id,
                "bank_name": i.bank_name,
                "account_no": i.account_no,
                "ifsc_code": i.IFSC_code,
                "amount": i.amount
            }
        )
    return JsonResponse({"status": "ok", "data": ar})

def android_delete_bank(request):
    bid = request.POST['bid']
    bank.objects.get(id=bid).delete()
    return JsonResponse({"status":"ok"})
#
# def android_online_payment(request):
#     lid = request.POST['lid']
#
#     # wid = request.POST['wid']
#
#     bank_name = request.POST['bank_name']
#     account_no = request.POST['account_no']
#     ifsc_code = request.POST['ifsc_code']
#     amount = request.POST['amount']
#     logininstance = login.objects.get(id=lid)
#
#     data = bank.objects.filter(bank_name = bank_name, account_no = account_no, IFSC_code = ifsc_code,LOGIN = logininstance)
#     if data.exists():
#         res = bank.objects.get(LOGIN=lid)
#         amt1 = res.amount
#         balance1 = amt1 - int(amount)
#         bank.objects.filter(LOGIN=lid).update(amount=balance1)
#
#         data1 = serviceprovider.objects.get(LOGIN=lid)
#         provider_id = data1.LOGIN
#         res2 = bank.objects.get(LOGIN=provider_id)
#         amt2 = res2.amount
#         balance2 = amt2 + int(amount)
#         # print("bbvvvvvvv", balance2)
#         bank.objects.filter(LOGIN=provider_id).update(amount=balance2)
#         booking.objects.filter(id=lid).update(payment_status='online')
#         return JsonResponse({"status": "okk"})
#
#     else:
#         return JsonResponse({"status": "no"})



def android_online_payment(request):
    lid = request.POST['lid']
    # print(lid,"lid")
    bid = request.POST['bid']
    # branch_id = request.POST['branch_id']

    bank_name =request.POST['bank_name']
    account_no = request.POST['account_no']
    ifsc_code = request.POST['ifsc_code']
    amount = request.POST['amount']

    # print("b",bank_name,"a",account_no,ifsc_code)

    data = bank.objects.filter(bank_name=bank_name, account_no=account_no, IFSC_code=ifsc_code, LOGIN=lid)
    print("kkkk",data)
    if data.exists():
        # data2 = booking.objects.filter(USER__LOGIN=lid,status='Done')
        data2 = booking.objects.filter(USER__LOGIN=lid,status='approved')
        res = data[0]
        amount1 = res.amount
        print("nn  ",amount1)
        print("mm  ",data2)
        if int(amount1) >= int(amount):
            for i in data2:

                res = bank.objects.get(LOGIN=lid)  # user bank
                amount1 = res.amount
                balance1 = int(amount1) - int(i.amount)
                bank.objects.filter(LOGIN=lid).update(amount=balance1)
                # qry1 = user.objects.get(LOGIN=lid)
                # aid = i.OWNSERVICE
                # qry2 = service.objects.get(id=aid)
                bid = i.OWNSERVICE.SERVICEPROVIDER_id
                print(lid, bid)


                data1 = serviceprovider.objects.get(id=bid)
                serviceprovider_id = data1.LOGIN
                res2 = bank.objects.get(LOGIN=serviceprovider_id)  # service provider  bank
                amount2 = res2.amount
                balance2 = int(amount2) + int(i.amount)

                bank.objects.filter(LOGIN=serviceprovider_id).update(amount=balance2)
                # bill.objects.filter(LOGIN=branch_id).update(status = 'paid')
                booking.objects.filter(id=i.id).update(paymentstatus='paid')

            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "insufficient"})

    else:
        return JsonResponse({"status": "no"})







