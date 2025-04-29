from django.shortcuts import render, redirect
from django.contrib import messages
from .models import login , document_detail , document_security_technique , privillaged_document, contact_detail , Feedback_Detail
import random
import smtplib
import hashlib
# Create your views here.

def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')


def loginpage(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def index(request):
    user_records = document_detail.objects.all()
    total_count = user_records.count()

    private_count = document_detail.objects.filter(security_id=2)
    pricount = private_count.count()
    print(pricount)

    public_count = document_detail.objects.filter(security_id=1)
    pubcount = public_count.count()
    print(pubcount)

    privillage_count = document_detail.objects.filter(security_id=3)
    privicount = privillage_count.count()
    print(privicount)

    context = {
        'total':total_count,
        'pri':pricount,
        'pub':pubcount,
        'privi':privicount
    }



    return render(request,'index.html',context)

def public(request):
    return render(request,'public.html')

def private(request):
    return render(request,'private.html')

def privillage(request):
    return render(request,'privillage.html')

def public_document(request):
    fetchdoc = document_detail.objects.all().filter(security_id=1)
    return render(request,'public_document.html',{'docs':fetchdoc})

def private_document(request):
    fetchdoc = document_detail.objects.all().filter(security_id=2)
    return render(request, 'private_document.html', {'docs': fetchdoc})


def privillage_document(request):
    uid = request.session['log_user']
    employee_query = privillaged_document.objects.values('d_id').filter(demail=uid)
    print(employee_query)
    fetchdoc = document_detail.objects.filter(id__in=employee_query).values()
    print(fetchdoc)
    return render(request, 'privillage_document.html', {'docs': fetchdoc})


def your_document(request):
    uid = request.session['log_id']
    fetchdoc = document_detail.objects.all().filter(l_id=uid)
    return render(request, 'your_document.html', {'docs': fetchdoc})

def contact_us(request):
    return render(request,'contact_us.html')

def about_us(request):
    return render(request,'about_us.html')

def enquiry(request):
    fetchdoc = contact_detail.objects.all().filter()
    return render(request, 'enquiry.html', {'docs': fetchdoc})

def feedback(request):
    return render(request,'feedback.html')

def viewdata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("pass")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        cpassword = request.POST.get("cpass")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        # adding TLS security
        server.starttls()
        # get your app password of gmail ----as directed in the video
        passw = 'qyhbgcbqybrcvvbv'
        server.login("meetvishwasshukla@gmail.com", passw)
        # generate OTP using random.randint() function
        otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
        msg = 'Hello, Your OTP is ' + str(otp)
        sender = 'meetvishwasshukla@gmail.com'  # write email id of sender
      #  receiver = ''  # write email of receiver
        # sendi
        server.sendmail(sender, email, msg)
        server.quit()



        if password != cpassword:
            messages.error(request,'Password and Confirm Password Should be Same')
            return render(request, 'register.html')
        else:
            logindata = login(first_name=fname,last_name=lname,phone=phone,email=email,password=password,role=2)

            verification(request,logindata,otp)
            #logindata.save()
            #messages.success(request, 'You are registered successfully!')

    else:
        messages.error(request, 'error occured')
    return render(request,'verification.html')


def logout(request):
   try:
      del request.session['log_user']
      del request.session['log_id']
   except:
      pass
   return render(request,'home.html')



def checklogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = login.objects.get(email=email,password=password)
            request.session['log_user'] = user.email
            request.session['log_id'] = user.id
            request.session['log_name'] = user.first_name
            request.session.save()
        except login.DoesNotExist:
            user = None

        if user is not None:
            return redirect(index)

        else:
            messages.info(request, 'Your email or password is incorrect')
    return render(request, 'login.html')


def insertdocument(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        dname = request.POST.get("dname")
        ddesc = request.POST.get("ddesc")
        dfile = request.FILES["dfile"]
        import os.path
        extension = os.path.splitext(dfile.name)[1]

        query = document_detail(l_id=login(id=uid),d_name=dname,d_description=ddesc,d_type=extension,security_id=document_security_technique(id=1),password="",document=dfile)
        query.save()
        messages.success(request, 'Document Uploaded Succesfully')
    else:
        messages.error(request, 'error occured')

    return render(request, 'public.html')

def insertprivatedocument(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        dname = request.POST.get("dname")
        ddesc = request.POST.get("ddesc")
        dfile = request.FILES["dfile"]
        dpass = request.POST.get("dpass")

        hash_object = hashlib.md5(dpass.encode())
        hash_object = hash_object.hexdigest()

        import os.path
        extension = os.path.splitext(dfile.name)[1]
        query = document_detail(l_id=login(id=uid),d_name=dname,d_description=ddesc,d_type=extension,security_id=document_security_technique(id=2),password=hash_object,document=dfile)

        query.save()
        messages.success(request, 'Document Uploaded Securely and Sucessfully')
    else:
        messages.error(request, 'error occured')

    return render(request, 'private.html')

def insertprivillagedocument(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        dname = request.POST.get("dname")
        ddesc = request.POST.get("ddesc")
        dfile = request.FILES["dfile"]
        demail = request.POST.get("demail")
        import os.path
        extension = os.path.splitext(dfile.name)[1]
        query = document_detail(l_id=login(id=uid),d_name=dname,d_description=ddesc,d_type=extension,security_id=document_security_technique(id=3),password="",document=dfile)
        query.save()

        fetchid = document_detail.objects.last().id

        query2 = privillaged_document(d_id=document_detail(id=fetchid),l_id=login(id=uid),demail=demail,privillage_status=1)
        query2.save()
        messages.success(request, 'Document Shared Securely and Sucessfully')
    else:
        messages.error(request, 'error occured')

    return render(request, 'privillage.html')

def View_document(request):
    if request.method == 'POST':
        Id = request.session['log_id']
        Name = request.POST.get("name")
        Description = request.POST.get("desc")
        DocumentType=request.POST.get("dtype")
        SecurityType=request.POST.get("stype")
        File = request.FILES["dfile"]
        Action = request.POST.get("action")


        query = document_detail(l_id=login(id=Id),d_name=Name,d_description=Description,DocumentType='no type',SecurityTYpe=SecurityType(id=3),document=File,action=Action)
        query.save()
        messages.success(request, 'Document Shared Securely and Sucessfully')
    else:
        messages.error(request, 'error occured')

    return render(request, 'privillage.html')

def password(request,id):
    docid = id
    return render(request, 'password.html',{'id':docid})

def checkpass(request):
    if request.method == 'POST':
        password = request.POST['dname']
        docid = request.POST['docid']

        password = hashlib.md5(password.encode())
        password = password.hexdigest()

        mypath = "password/"+docid
        fetchpass = document_detail.objects.get(id=docid)
        docpass = fetchpass.password
        documets = fetchpass.document
        print(documets)

        if password == docpass:
           return render(request,"password.html",{'doclink':documets})
        else:
            messages.error(request,"Wrong Password")
    return render(request, "password.html",{'id':docid})

def enquirypage(request):
    if request.method == 'POST':
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        query = contact_detail(phone=phone,email=email,message=message)
        query.save()
        messages.success(request, 'Message Save Successfully')
    return render(request,
                  'enquiry.html')

def addfeedback(request):
    if request.method == 'POST':
        Id = request.session['log_id']
        rate = request.POST.get("rate")
        comment = request.POST.get("comment")

        query = Feedback_Detail(l_id=login(id=Id),comment=comment,rating=rate)
        query.save()
        messages.success(request, 'Feedback Save Successfully')
    return render(request, 'feedback.html')

def verification(request,logindata,oldotp):
    if request.method == 'POST':
        otp = request.POST.get("otp")
        btn = request.POST.get("check")
        if btn:
            otp = otp + 1
        else:
            logindata.save()




