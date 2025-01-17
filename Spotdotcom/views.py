from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from Spotdotcom.models import AmalgamationTable, LoginTable, ParkingSpotTable, PhotoShootTable, ResortTable, RestaurantGalleryTable, RestaurantTable, TouristTable, UserTable

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
        
        elif Login_obj.usertype=="Restaurant":
            return HttpResponse('''<script>alert("welcom home");window.location='/RestaurantDash'</script>''')
        
        #////////////////////////////////////// ADMIN ////////////////////////////////////////

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
    

        

class deleteamal(View):
    def get(self,request,id):
        obj=AmalgamationTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_Amalgamation'</script>''')
    

class deletepark(View):
    def get(self,request,id):
        obj=ParkingSpotTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_ParkingSpot'</script>''')
    
class deletephoto(View):
    def get(self,request,id):
        obj=PhotoShootTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_photoarea'</script>''')
    
class deleteresort(View):
    def get(self,request,id):
        obj=ResortTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_Resort'</script>''')
    
class deleterestaurent(View):
    def get(self,request,id):
        obj=RestaurantTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_Restaurent'</script>''')
    
class deletetourist(View):
    def get(self,request,id):
        obj=TouristTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/manage_tourist'</script>''')
    
class deleteuser(View):
    def get(self,request,id):
        obj=UserTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location='/userlist'</script>''')
    
#///////////////////////////////////////////// RESTAURANT ///////////////////////////////////////////////////////\

class RestaurantDash(View):
    def get(self,request):
        return render(request,'Restaurant/RestaurantDash.html')
 
class RestaurantGallery(View):
    def get(self,request):
        obj=RestaurantGalleryTable.objects.get(id=id)
        return render(request,'Restaurant/manage_gallery.html',{'val':obj})