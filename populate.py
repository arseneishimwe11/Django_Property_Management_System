import random
from faker import Faker
from properties.models import Property
from tenants.models import Tenant

fake = Faker()

for _ in range(100):
    Property.objects.create(
        name=fake.name(),
        address=fake.address(),
        rent=fake.random_int(min=30000, max=500000),
        is_available=fake.boolean(),
    )

#
# tenants
# Ensure there are existing properties to assign tenants to
if not Property.objects.exists():
    print("No properties found! Create some properties first.")
else:
    properties = list(Property.objects.all())  # Get all existing properties

    for _ in range(100):  # Generate 100 sample tenants
        # Select random properties for ManyToManyField
        random_properties = random.sample(properties, random.randint(1, 90))  # 1 to 3 properties per tenant

        # Select a random property for the ForeignKey field
        random_property = random.choice(properties)

        # Create tenant
        tenant = Tenant.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number()[:15],
            claim_date=fake.date_between(start_date="-2y", end_date="today"),  # Random date in the past 2 years
            property=random_property,
        )

        # Assign ManyToMany relationships
        tenant.properties.set(random_properties)

    print("100 sample tenants created!")


print("Sample data created!")
