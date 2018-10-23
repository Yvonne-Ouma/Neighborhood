from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Neighborhood,Business,Location,Posts

# Create your tests here.

class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.prof = Profile(user_name='prof',bio = "good",profile_picture = "hoodip4/media/profiles/ttt.jpg")
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.prof, Profile))

    #testing save method

    def test_save_method(self):
        self.prof.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_method(self):
        self.prof.save()
        self.prof.delete()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) == 1)

    def test_update_method(self):
        self.prof.save_profile()
        self.prof.update_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)   

    def test_create_method(self):
        self.prof.create_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class NeighborhoodTest(TestCase):
    def setUp(self):
        self.hood=Neighborhood(name="kal",neighborhood_location="Mombasa", population=8)

    def test_instance(self):
        self.assertIsInstance(self.hood,Neighborhood)

    def test_save_Neighborhood(self):
        self.assertFalse(self.hood in Neighborhood.objects.all())
        self.hood.save()
        self.assertTrue(self.hood in Neighborhood.objects.all())
        self.hood.delete()

    def test_delete_Neighborhood(self):
        self.assertFalse(self.hood in Neighborhood.objects.all())
        self.hood.save()
        self.assertTrue(self.hood in Neighborhood.objects.all())
        self.hood.delete()

    def test_update(self):
        self.hood.save_neighborhood()
        self.hood.update_neighborhood()
        neibor = Neighborhood.objects.all()
        self.assertTrue(len(neibor) > 0)

    def test_save(self):
        self.hood.create_neighborhood()
        neibor = Neighborhood.objects.all()
        self.assertTrue(len(neibor) > 0) 


class BusinessTestClass(TestCase):
    def setUp(self):
        self.business=Business(business_name="me",business_email="tyt@gmail.com",business_pic = "hoodip4/media/business_images/gjijdi.jpg")

    def test_instance(self):
        self.assertIsInstance(self.business,Business)

    def test_save_business(self):
        self.assertFalse(self.business in Business.objects.all())
        self.business.save()
        self.assertTrue(self.business in Business.objects.all())
        self.business.delete()

    def test_delete_business(self):
        self.assertFalse(self.business in Business.objects.all())
        self.business.save()
        self.assertTrue(self.business in Business.objects.all())
        self.business.delete()

    def test_update(self):
        self.business.save_business()
        self.business.update_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_create_business(self):
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)    



class LocationTestClass(TestCase):
  
    def setUp(self):
        self.location = Location(name = 'Kampala')
        self.location.save()


    def test_instance(self):

        self.assertTrue(isinstance(self.location, Location))

    #Testing Save method

    def test_save_method(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

        # Testing delete method
    def test_delete_location(self):
        self.location.delete()
        self.assertEqual(len(Location.objects.all()), 0) 

    def test_update_location(self):
        self.location.save_location()
        self.location.update_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)    

class PostsTest(TestCase):
    # Set up method
    def setUp(self):
        self.post = Posts.objects.create(name="nairobi", image="hoodip4/media/picture/ghj.jpg", description="this is owesome")

    def test_instance(self):
        self.assertIsInstance(self.post,Posts)

    def test_save_method(self):
        post = Posts.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.post.delete()
        self.assertEqual(len(Posts.objects.all()), 0)  


    def test_update_post(self):
        self.post.save_post()
        self.post.update_post()
        post = Posts.objects.all()
        self.assertTrue(len(post) > 0)        

