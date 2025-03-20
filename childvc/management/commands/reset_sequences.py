from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset all database sequences to start from 1'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Reset sequence for Contact model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_contact"', 'id'), 1, false);
            """)
            
            # Reset sequence for VaccinationRecord model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_vaccinationrecord"', 'id'), 1, false);
            """)
            
            # Reset sequence for Vaccine model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_vaccine"', 'vid'), 1, false);
            """)
            
            # Reset sequence for FAQ model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_faq"', 'fid'), 1, false);
            """)
            
            # Reset sequence for Appointment model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_appointment"', 'aid'), 1, false);
            """)
            
            # Reset sequence for Profile model
            cursor.execute("""
                SELECT setval(pg_get_serial_sequence('"childvc_profile"', 'profile_id'), 1, false);
            """)
            
        self.stdout.write(self.style.SUCCESS('Successfully reset all sequences to start from 1')) 