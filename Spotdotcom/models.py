from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    usertype = models.CharField(max_length=100,null=True,blank=True)

class TouristTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Address = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class AmalgamationTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Place = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    Image = models.FileField(blank=True, null=True)
    Description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class ParkingSpotTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    AreaName = models.CharField(max_length=30, null=True, blank=True)
    NoParking = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)        
    Status = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  

class PhotoShootTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    SpotName = models.CharField(max_length=30, null=True, blank=True) 
    Description = models.CharField(max_length=300, null=True, blank=True) 
    Type = models.CharField(max_length=300, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)       
    EntryTime = models.TimeField(null=True, blank=True)       
    ExitTime = models.TimeField(null=True, blank=True)       
    Status = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  

class ResortTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    ResortName = models.CharField(max_length=30, null=True, blank=True) 
    OwnerName = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Address = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True)  
    Type = models.CharField(max_length=50, blank=True, null=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)    

class RestaurantTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    RestaurantName = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Place = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True) 
    Type = models.CharField(max_length=30, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Image = models.FileField(blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ComplaintTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    Complaint = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Reply = models.CharField(max_length=300,null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)      
          
class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)     
          
class ResortDescriptionTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    History = models.CharField(max_length=500, blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortGalleryTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Image = models.FileField(blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class ResortFacilityTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Facility = models.CharField(max_length=300, blank=True, null=True)   
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Status = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortMenuTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    FoodName = models.CharField(max_length=50, blank=True, null=True)   
    Type = models.CharField(max_length=30, null=True, blank=True)    
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Category = models.CharField(max_length=50, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          

class ResortOfferTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    OfferName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 


class RestaurantDescriptionTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    History = models.CharField(max_length=500, blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class RestaurantGalleryTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Image = models.FileField(blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class RestaurantFacilityTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Facility = models.CharField(max_length=300, blank=True, null=True)   
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Status = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class RestaurantMenuTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    FoodName = models.CharField(max_length=50, blank=True, null=True)   
    Type = models.CharField(max_length=30, null=True, blank=True)    
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Category = models.CharField(max_length=50, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          

class RestaurantOfferTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    OfferName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True)   
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 

class RestaurantRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 

class FestivalTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    FestivalName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          

class ViewPointTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    ViewPoint = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ViewPointGalleryTable(models.Model):
    POINT = models.ForeignKey(ViewPointTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)
    
class FestivalGalleryTable(models.Model):
    FESTIVAL = models.ForeignKey(FestivalTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class AmalgamationGalleryTable(models.Model):
    AMALGAMATION = models.ForeignKey(AmalgamationTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class PhotoShootGalleryTable(models.Model):
    SHOOT = models.ForeignKey(PhotoShootTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class FestivalRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    FESTIVAL = models.ForeignKey(FestivalTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 


class ParkingRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    PARKING = models.ForeignKey(ParkingSpotTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Review = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class ViewPointRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    POINT = models.ForeignKey(ViewPointTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Feedback = models.CharField(max_length=300, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)

class AmalgamationRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    AMALGAMATION = models.ForeignKey(AmalgamationTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Review = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

