from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from Spotdotcom.models import AmalgamationTable, LoginTable, ParkingSpotTable, PhotoShootTable, ResortTable, RestaurantTable, TouristTable, UserTable

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request,"business/Login.html")
    
    def post(self,request):
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        Login_obj=LoginTable.objects.get(username=username,password=password)
        print(Login_obj)
        if Login_obj.usertype=="admin":
            return HttpResponse('''<script>alert("welcom home");window.location='/adminhome'</script>''')
        
class admindashboard(View):
    def get(self,request):
        return render(request,'adminstrator/admin_dashboard.html')
                                

class userlist(View):
    def get(self,request):
        obj=UserTable.objects.all()
        return render(request,'adminstrator/userlist.html',{'val':obj})

class manage_tourist(View):
    def get(self,request):
        obj=TouristTable.objects.all()
        return render(request,'adminstrator/manage_tourist.html',{'val':obj})

class manage_Restaurent(View):
    def get(self,request):
        obj=RestaurantTable.objects.all()
        return render(request,'adminstrator/manage_Restaurent.html',{'val':obj})
    
class manage_Resort(View):
    def get(self,request):
        obj=ResortTable.objects.all()
    
        return render(request,'adminstrator/manage_Resort.html',{'val':obj})
    
class manage_photoarea(View):
    def get(self,request):
        obj=PhotoShootTable.objects.all()
        print(obj)
        return render(request,'adminstrator/manage_photoarea.html',{'val':obj})
    
class manage_ParkingSpot(View):
    def get(self,request):
        obj=ParkingSpotTable.objects.all()
        return render(request,'adminstrator/manage_ParkingSpot.html',{'val':obj})
    
class manage_Amalgamation(View):
    def get(self,request):
        obj=AmalgamationTable.objects.all()
        return render(request,'adminstrator/manage_Amalgamation.html',{'val':obj})
        