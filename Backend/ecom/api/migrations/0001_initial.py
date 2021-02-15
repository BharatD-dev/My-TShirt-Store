from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="bharat",
                          email="dhabekarbharat@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9922136638",
                          gender="Male"
                          )
        user.set_password("Admin@1234")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
