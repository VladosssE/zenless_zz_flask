from extensions import db
from models.table_bangboo import Bangboo_stats

def seed_bangboo():
    bangboos = [
        ('1', 'Щелкун', '0', '0', 'S', 'Snap.webp'),
	('2', 'Красный Моккус', '0', '0', 'S', 'Red_Moccus.webp'),
	('3', 'Револьвербу', '0', '0', 'S', 'Bangvolver.webp'),
	('4', 'Резонабу', '0', '0', 'S', 'Resonaboo.webp'),
	('5', 'Амиллион', '0', '0', 'S', 'Amillion.webp'),
	('6', 'Госпожа Эсме', '0', '0', 'S', 'Miss_Esme.webp'),
	('7', 'Деталькабу', '0', '0', 'A', 'Bild_N.webp'),
	('8', 'Перерабу', '0', '0', 'A', 'Overtimeboo.webp'),
	('9', 'Борьбу', '0', '0', 'A', 'Brawlerboo.webp'),
	('10', 'Рыцарьбу', '0', '0', 'A', 'Knightboo.webp'),
	('11', 'Злобнобу', '0', '0', 'A', 'Baddieboo.webp'),
	('12', 'Магнитобу', '0', '0', 'A', 'Magnetiboo.webp'),
	('13', 'Вельзебу', '0', '0', 'A', 'Devilboo.webp'),
	('14', 'Баробу', '0', '0', 'A', 'Booressure.webp'),
	('15', 'Электробу', '0', '0', 'A', 'Electroboo.webp'),
	('16', 'Яблочкобу', '0', '0', 'A', 'Boollseye.webp'),
	('17', 'Авокабу', '0', '0', 'A', 'Avocaboo.webp'),
	('18', 'Плаксабу', '0', '0', 'A', 'Cryboo.webp'),
	('19', 'Пакетник', '0', '0', 'A', 'Bagboo.webp'),
	('20', 'Бумабу', '0', '0', 'A', 'Paperboo.webp'),
	('21', 'Сумобу', '0', '0', 'A', 'Sumoboo.webp'),
	('22', 'Искатель', '0', '0', 'A', 'Exploreboo.webp'),
	('23', 'Пингвибу', '0', '0', 'A', 'Penguinboo.webp'),
	('24', 'Бирклик', '0', '0', 'S', 'Birkblick.webp'),
	('25', 'Меркурий', '0', '0', 'S', 'Mercury.webp'),
	('26', 'Львец', '0', '0', 'S', 'Belion.webp'),
	('27', 'Робин', '0', '0', 'S', 'Robin.webp'),
	('28', 'Агент Гулливер', '0', '0', 'S', 'Agent_Gulliver.webp'),
	('29', 'Офицер Цуй', '0', '0', 'S', 'Officer_Cui.webp'),
	('30', 'Мажордом', '0', '0', 'S', 'Butler.webp'),
	('31', 'Акулабу', '0', '0', 'S', 'Sharkboo.webp'),
	('32', 'Штекербу', '0', '0', 'S', 'Plugboo.webp'),
	('33', 'Ракетабу', '0', '0', 'S', 'Rocketboo.webp'),
	('34', 'Прорабу', '0', '0', 'S', 'Safety.webp'),
	('35', 'Экскалибу', '0', '0', 'A', 'Excaliboo.webp'),
	('36', 'Счастливчик', '0', '0', 'A', 'Luckyboo.webp'),
        ('37', 'Тестовый', '0', '0', 'A', '000.webp')
        ]

    added = 0
    updated = 0
    
    for bid, bname, blevel, bstars, bclass, burl in bangboos:
        bangboo = db.session.get(Bangboo_stats, bid)
        if bangboo:
            bangboo.bangboo_name = bname
            bangboo.bangboo_class = bclass
            bangboo.bangboo_url = burl
            updated += 1
        else:
            db.session.add(Bangboo_stats(
                bangboo_id = bid,
                bangboo_name = bname,
                bangboo_level = blevel,
                bangboo_stars = bstars,
                bangboo_class = bclass,
                bangboo_image_url = burl
            ))
            added += 1
    db.session.commit()
    print(f"[ 001 ][ {'Банбу':<20} ][ {(added):>03d} записей добавлено ][ {(updated):>03d} записей просмотрено ]")
