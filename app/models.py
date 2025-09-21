from django.db import models

class Patient(models.Model):
    # Basic Info
    uhid = models.CharField(max_length=50, unique=True, blank=True, null=True)
    registration_no = models.CharField(max_length=50, unique=True)

    # Relation
    RELATION_CHOICES = [
        ('Self', 'Self'), ('Father', 'Father'), ('Mother', 'Mother'),
        ('Spouse', 'Spouse'), ('Child', 'Child'), ('Other', 'Other')
    ]
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES)
    relation_name = models.CharField(max_length=100)

    # Contact
    address = models.TextField()
    mobile_no = models.CharField(max_length=15)

    # Occupation
    OCCUPATION_CHOICES = [
        ('Government Service','Government Service'), ('Private Service','Private Service'),
        ('Business','Business'), ('Student','Student'), ('Retired','Retired'),
        ('Unemployed','Unemployed'), ('Other','Other')
    ]
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)

    # Service
    SERVICE_CHOICES = [
        ('Full Body Checkup','Full Body Checkup'), ('General Medicine','General Medicine'),
        ('Surgery','Surgery'), ('Pediatrics','Pediatrics'), ('Orthopedics','Orthopedics'),
        ('Cardiology','Cardiology'), ('Neurology','Neurology')
    ]
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)

    # Nationality
    NATIONALITY_CHOICES = [
        ('India','India'), ('American','American'), ('British','British'),
        ('Canadian','Canadian'), ('Australian','Australian'), ('Other','Other')
    ]
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES)

    # Age
    age_years = models.IntegerField(default=0)
    age_months = models.IntegerField(default=0)
    age_days = models.IntegerField(default=0)

    # Blood Group
    BLOOD_CHOICES = [
        ('O+','O+'), ('O-','O-'), ('A+','A+'), ('A-','A-'),
        ('B+','B+'), ('B-','B-'), ('AB+','AB+'), ('AB-','AB-')
    ]
    blood_group = models.CharField(max_length=5, choices=BLOOD_CHOICES)

    # Identity as JSONField for multiple entries
    identities = models.JSONField(default=list, blank=True)
    # Example: [{"identity_type": "Aadhar No", "identity_number": "123456"}, {...}]

    # Insurance
    insurance = models.JSONField(default=list, blank=True)
    # Location
    city = models.CharField(max_length=100)
    STATE_CHOICES = [
        ('Andhra Pradesh','Andhra Pradesh'), ('Karnataka','Karnataka'), ('Kerala','Kerala'),
        ('Tamil Nadu','Tamil Nadu'), ('Maharashtra','Maharashtra'), ('Delhi','Delhi'), ('Other','Other')
    ]
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    # File / Biometric
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    biometric = models.BooleanField(default=False)

    # Referred By (radio buttons)
    REFERRED_CHOICES = [
        ('Internal','Internal'), ('External','External')
    ]
    referred_by = models.CharField(max_length=20, choices=REFERRED_CHOICES)
    referred_doctor = models.CharField(max_length=100)
    mobile_no_doctor = models.CharField(max_length=15)
    # Message to mobile
    message_to_mobile = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uhid} - {self.relation_name}"
