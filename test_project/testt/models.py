from django.db import models


class BotUserModel(models.Model):

    registration = models.DateTimeField(
        verbose_name='Дата регистрации', auto_now_add=False, auto_now=False, null=True, blank=True)
    channel = models.CharField(
        verbose_name='Канал', max_length=250, null=True, blank=True)
    id_bothelp = models.CharField(
        verbose_name='ID BotHelp', max_length=250, null=True, blank=True)
    id_telegram = models.CharField(
        verbose_name='ID Телеграм', max_length=250, null=True, blank=True)
    username = models.CharField(
        verbose_name='Username', max_length=250, null=True, blank=True)
    first_name  = models.CharField(
        verbose_name='Имя', max_length=250, null=True, blank=True)
    last_name  = models.CharField(
        verbose_name='Фамилия', max_length=250, null=True, blank=True)
    email  = models.CharField(
        verbose_name='Email', max_length=250, null=True, blank=True)
    mobile  = models.CharField(
        verbose_name='Телефон', max_length=250, null=True, blank=True)
    link  = models.CharField(
        verbose_name='Ссылка', max_length=250, null=True, blank=True)
    utm_source  = models.CharField(
        verbose_name='utm_source', max_length=250, null=True, blank=True)
    utm_campaign  = models.CharField(
        verbose_name='utm_campaign', max_length=250, null=True, blank=True)
    utm_medium  = models.CharField(
        verbose_name='utm_medium', max_length=250, null=True, blank=True)
    utm_term  = models.CharField(
        verbose_name='utm_term', max_length=250, null=True, blank=True)
    utm_content  = models.CharField(
        verbose_name='utm_content', max_length=250, null=True, blank=True)
    utm_content  = models.CharField(
        verbose_name='utm_content', max_length=250, null=True, blank=True)
    unsubscribed = models.DateTimeField(
        verbose_name='Отписался', auto_now_add=False, auto_now=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.channel} | {self.username} | ID Телеграм: {self.id_telegram}'

    class Meta:
        verbose_name = 'Телеграм'
        verbose_name_plural = 'Телеграм'


class BotUtmLinkModel(models.Model):

    invite_link = models.CharField(
        verbose_name='Пригласительная ссылка', max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.invite_link}'

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'