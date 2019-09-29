from django.db import models
import hashlib

class Worker(models.Model):
    Person = models.CharField("ФИО сотрудника", max_length = 255)
    SerialPassport = models.IntegerField("Серия паспорта")
    NumberPassport = models.IntegerField("Номер паспорта")
    Education = models.TextField("Образование")
    StartDate = models.DateField("В компании с")
    Position = models.CharField("Должность", max_length = 255)
    Status = models.IntegerField("Статус работника")
    Avatar = models.ImageField("Фотография работника")
    # 0 - Всё нормально
    # 1 - В красной зоне
    # 2 - На переквалификации
    def __str__(self):
        return self.Person
    def getAvatar(self):
        return self.Avatar

class User(models.Model):
    login = models.CharField("Логин", max_length = 20, unique = True)
    password = models.CharField("Пароль", max_length = 128)
    type = models.IntegerField("Тип пользователя")
    # 0 - Руководитель
    # 1 - HR
    Person = models.CharField("Фамилия и имя пользователя", max_length = 255)
    def save(self, *args, **kwargs):
        newPass = hashlib.sha512(self.password.encode('utf-8')).hexdigest()
        self.password = newPass
        super(User, self).save()
    def __str__(self):
        return self.Person

class Tag(models.Model):
    title = models.CharField("Название тега", max_length = 70, unique = True)
    def __str__(self):
        return self.title

class Profession(models.Model):
    title = models.CharField("Название профессии", max_length = 70, unique = True)
    def __str__(self):
        return self.title

class Relation(models.Model):
    Worker_relate = models.ForeignKey(Worker, related_name = "Worker_id", on_delete = models.CASCADE)
    Profession_relate = models.ForeignKey(Profession, related_name = "Prof_id", on_delete = models.CASCADE)
    Type = models.IntegerField("Тип тега")
    Tag_relate = models.ForeignKey(Tag, related_name = "Tag_id", on_delete = models.CASCADE)

class Retrain(models.Model):
    Profession1 = models.ForeignKey(Profession, related_name = "Prof_id_from", on_delete = models.CASCADE)
    Profession2 = models.ForeignKey(Profession, related_name = "Prof_id_to", on_delete = models.CASCADE)
    TargetWorker = models.ForeignKey(Worker, related_name = "Worker_target_id", on_delete = models.CASCADE, unique = True)
