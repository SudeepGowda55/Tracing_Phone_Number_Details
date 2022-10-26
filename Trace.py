import phonenumbers, folium
from phonenumbers import timezone, carrier, geocoder
from opencage.geocoder import OpenCageGeocode

geocodersInstance = OpenCageGeocode('Enter OpenCage Geocoding API here')

print("Please Enter the phone number with the country code :", end='\t')

enteredPhoneNumber = input()
phoneNumber = phonenumbers.parse(enteredPhoneNumber)

print("-"*90)
print("Scanning For Timezone, Telecomm company, and the Location ")

timeZone = timezone.time_zones_for_number(phoneNumber)
telecomm =  carrier.name_for_number(phoneNumber, 'en')
region = geocoder.description_for_number(phoneNumber, 'en')

responseData = geocodersInstance.geocode(str(region))

latitude = responseData[0]['geometry']['lat']
longitude = responseData[0]['geometry']['lng']

htmlPage = folium.Map(location=[latitude, longitude], zoom_start=13)
folium.Marker([latitude, longitude], popup="<i>Location Traced</i>", tooltip="This is the location").add_to(htmlPage)

htmlPage.save("index.html")

print("You have entered the phone number with ",phoneNumber)
print(timeZone, "is the Timezone")
print(telecomm, "is the company that has provided the SIM ")
print(region, "is the region of the phone number")
print(latitude, "is the Longitude")
print(longitude, "is the latitude")
print("In this same directory a file called as index.html is created. Open it in your Browser. The Latitude and Longitude may not be correct, so location may not be perfect. This is still in development")