from django.core.mail import send_mail
from mailing.models import Mailing, Client
from config import settings
import datetime


def get_mailing_list():
    mailing_list = []
    queryset_list = list(Mailing.objects.filter(at_work='True'))
    now = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=3)
    offset = datetime.timedelta(minutes=2)
    start = now - offset
    end = now + offset
    for mail in queryset_list:
        print(f"{mail.title}")
        try:
            if start < mail.next_send_date < end:
                print(f"метка следующей отправки {mail.next_send_date}")
                mailing_list.append(mail)
                print(f"попало в рассылку")
            else:
                print(f"не попало в рассылку")
        except:
            print(f"не имеет метки")
            if start < mail.departure_date < end:
                print(f"дата начала рассылки {mail.departure_date}")
                mailing_list.append(mail)
                print(f"попало в рассылку")
            else:
                print(f"не попало в рассылку")

    return mailing_list


def get_client_list(lst):
    client_list = []
    for client in lst:
        client_list.append(client.email)
    return client_list


def send_mailing():
    mailing_list = get_mailing_list()
    # print(f"start looking mailing")
    # for mail in mailing_list:
    #     user_pk = mail.user.pk
    #     lst = list(Client.objects.filter(user__pk=user_pk))
    #     client_list = get_client_list(lst)
    #     send_mail(
    #         subject=mail.title,
    #         message=mail.content,
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=client_list,
    #         fail_silently=False,
    #         auth_user=settings.EMAIL_HOST_USER,
    #         auth_password=settings.EMAIL_HOST_PASSWORD)
    #     if mail.next_send_date:
    #         next_send = mail.next_send_date + datetime.timedelta(days=mail.periodicity)
    #         mail.next_send_date = next_send
    #         #mail.save()
    #         print(f"mail {mail.title} send success! next send at {mail.next_send_date}")
    #     else:
    #         date = datetime.datetime.now(datetime.timezone.utc)
    #         now = date + datetime.timedelta(hours=3)
    #         mail.next_send_date = now + datetime.timedelta(days=mail.periodicity)
    #         print(f"mail {mail.title} send success! next send at {mail.next_send_date}")
    #         #mail.save()
