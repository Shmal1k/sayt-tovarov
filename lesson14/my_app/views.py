from my_app.models import Tovar
from django.http import HttpResponse
from django.shortcuts import render

def add_tovar(request):
    # Добавим несколько записей в таблицу
    tovars = Tovar.objects.bulk_create([
        Tovar(name='Штатив магнитный',price=1188, info='Надежная фиксация измерительных приборов на любой металлической поверхности для точной работы', img='1.png', opisanie='В наличии'),
        Tovar(name='Вакуумный пинцет',price=95, info='Незаменимый помощник для бережной работы с миниатюрными и хрупкими компонентами', img='2.png', opisanie='В наличии'),
        Tovar(name='Медный низкоомный зажим', price=101, info='Сверхнадежный электрический контакт с минимальными потерями, идеально для тестирования', img='3.png', opisanie='В наличии'),
        Tovar(name='Налобный фонарь', price=2309, info='Свободные руки и освещенная рабочая зона с максимальным комфортом и яркостью в любых условиях', img='4.png', opisanie='В наличии'),
        Tovar(name='Шлифовальные круги', price=329, info='Для идеальной обработки поверхностей: быстро, качественно и эффективно', img='5.png', opisanie='В наличии'),
        Tovar(name='Компьютерное кресло', price=6654, info='Создайте комфортное рабочее место и забудьте об усталости даже после долгих часов работы.', img='6.png', opisanie='В наличии'),
        Tovar(name='Блок питания 12V', price=3878, info=' Стабильное и надежное питание 12В для вашей электроники и устройств.', img='7.png', opisanie='В наличии'),
        Tovar(name='HDMI Emulator', price=319, info='Да', img='8.png', opisanie='В наличии'),
        Tovar(name='Подшипники', price=1219, info='Плавное вращение и долговечность ваших механизмов. Широкий размерный ряд', img='9.png', opisanie='В наличии'),
        Tovar(name='Алюминиевый чемодан', price=1009, info='Легкий, прочный и надежный способ хранения и транспортировки инструментов или ценных вещей.', img='10.png', opisanie='В наличии'),
        Tovar(name='Угольник столярный', price=209, info='Для безупречно ровных углов и точных разметок в столярных и плотницких работах.', img='12.png', opisanie='В наличии'),
        Tovar(name='Воронка стальная', price=180, info='Прочная и долговечная воронка для быстрого и аккуратного переливания жидкостей.', img='13.png', opisanie='В наличии'),
        Tovar(name='Голубь', price=10000, info='Ну... красивый вроде, отдается бесплатно в ЧИСТЫЕ руки (будем проверять)', img='11.png', opisanie='В наличии'),
    ])
    return HttpResponse('Записи успешно добавлены!')

def delite_tovar(request):
    # Удаление записи из таблицы
    tovar = Tovar.objects.filter(id=13).delete()
    return HttpResponse('Товар удален')

def update(request):
    # обновления Данных товаров
    tovar = Tovar.objects.get(id=13)
    tovar.img = "11.png"
    tovar.save(update_fields=['img'])
    return HttpResponse('Товар обновлен!')



def base(request):
    return render(request, 'base.html')


def catalog(request):
    tovars = Tovar.objects.all().values()  # берем все свойства каждого товара и передаем
    return render(request, 'catalog.html', {'tovars': tovars})

def card(request):
    id = request.GET.get('id', 0)
    try:
        id = int(id)
        if id > 0:
            tovar = Tovar.objects.get(id=id)
            # Передаем объект  напрямую в контекст
            return render(request, 'card.html', {'tovar': tovar})
    except (ValueError, TOVAR.DoesNotExist):
        return HttpResponse('id некорректный или товар не найден!')


def corzina(request):
    id = request.GET.get('id', 0)
    try:
        id = int(id)
        if id > 0:
            tovar = Tovar.objects.get(id=id)
            # Передаем объект  напрямую в контекст
            return render(request, 'corzina.html', {'tovar': tovar})
    except (ValueError, TOVAR.DoesNotExist):
        return HttpResponse('id некорректный или товар не найден!')