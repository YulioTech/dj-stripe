from django.core.management.base import BaseCommand

from ...models import Plan

class Command(BaseCommand):
    help = "Creates Stripe plans in the database from Stripe dashboard"
    

    def handle(self, *args, **options):
        for plan in Plan.api_list():
            Plan.sync_from_stripe_data(plan)
            
        self.stdout.write(self.style.SUCCESS("Successfully synced plans from Stripe."))