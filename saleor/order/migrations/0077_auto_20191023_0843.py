# Generated by Django 2.2.6 on 2019-10-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0076_auto_20191018_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderevent',
            name='type',
            field=models.CharField(choices=[('DRAFT_CREATED', 'draft_created'), ('DRAFT_ADDED_PRODUCTS', 'draft_added_products'), ('DRAFT_REMOVED_PRODUCTS', 'draft_removed_products'), ('PLACED', 'placed'), ('PLACED_FROM_DRAFT', 'placed_from_draft'), ('OVERSOLD_ITEMS', 'oversold_items'), ('CANCELED', 'canceled'), ('ORDER_MARKED_AS_PAID', 'order_marked_as_paid'), ('ORDER_FULLY_PAID', 'order_fully_paid'), ('UPDATED_ADDRESS', 'updated_address'), ('EMAIL_SENT', 'email_sent'), ('PAYMENT_CAPTURED', 'payment_captured'), ('PAYMENT_REFUNDED', 'payment_refunded'), ('PAYMENT_VOIDED', 'payment_voided'), ('PAYMENT_FAILED', 'payment_failed'), ('FULFILLMENT_CANCELED', 'fulfillment_canceled'), ('FULFILLMENT_RESTOCKED_ITEMS', 'fulfillment_restocked_items'), ('FULFILLMENT_FULFILLED_ITEMS', 'fulfillment_fulfilled_items'), ('TRACKING_UPDATED', 'tracking_updated'), ('NOTE_ADDED', 'note_added'), ('CUSTOMER_NOTE_UPDATED', 'customer_note_updated'), ('OTHER', 'other')], max_length=255),
        ),
    ]
