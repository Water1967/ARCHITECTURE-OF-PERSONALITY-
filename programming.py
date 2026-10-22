"""Deterministic, inspectable architectural programming; NOT a floor-plan generator."""
from collections import Counter

def build_program(residents, brief):
    completed={n:a for n,a in residents.items() if a}
    def hits(qid, substr):
        return [n for n,a in completed.items() if substr.lower() in a.get(qid,'').lower()]
    def room(key,name,area,why,priority='предварителен',evidence=None):
        return {'id':key,'name':name,'area_range_m2':area,'priority':priority,'reason':why,'evidence':evidence or [],'status':'хипотеза; изисква потвърждение'}
    rooms=[room('entry','Вход и комуникации',[9,16],'Базова функционална необходимост; стойността е ориентировъчна.'),room('living','Дневна и хранене',[24,36],'Обща жилищна зона; начинът на хранене се уточнява.',evidence=['B.01','B.03']),room('kitchen','Кухня',[9,15],'Базова функционална необходимост.'),room('bed','Спална зона',[13,18],'Минимум една спална зона, броят се уточнява.'),room('bath','Санитарни помещения',[5,9],'Базова функционална необходимост.'),room('storage','Склад и технически площи',[4,9],'Предварителен резерв за съхранение и обслужване.',evidence=['H.02'])]
    if hits('D.02','кабинет') or hits('D.02','бюро') or hits('D.03','всеки ден'):
        rooms.append(room('office','Работна зона / кабинет',[7,13],'Заявена работа или концентрация у дома.','висок',['D.02','D.03']))
    if hits('D.02','ателие') or hits('D.01','практическа'):
        rooms.append(room('studio','Ателие / работилница',[10,20],'Заявена практическа или творческа дейност; уточняват се оборудване и шум.','висок',['D.01','D.02']))
    if hits('C.02','отделна стая') or hits('C.01','шум'):
        rooms.append(room('retreat','Зона за уединение',[5,10],'Потребност от уединение; може да се комбинира с друга зона.','висок',['C.01','C.02']))
    outdoor=[]
    if hits('G.01','двор') or hits('G.02','градин') or hits('G.02','игри'):
        outdoor.append({'name':'Двор с обособени дейности','evidence':['G.01','G.02'],'note':'Външна площ; не се включва в РЗП.'})
    if hits('G.03','веранда'):
        outdoor.append({'name':'Покрита веранда','evidence':['G.03'],'note':'Площ и включване в РЗП се проверяват по конкретния проект.'})
    edges=[('entry','living','близост','Основна комуникация'),('living','kitchen','пряка връзка','Хранене и обслужване'),('bed','bath','близост','Нощно използване'),('entry','storage','близост','Съхранение')]
    ids={r['id'] for r in rooms}
    if 'office' in ids:edges.append(('office','living','контролирано разделяне','Концентрация срещу социални дейности'))
    if 'studio' in ids:edges.append(('studio','entry','контролирана връзка','Материали, инструменти и евентуален шум'))
    if 'retreat' in ids:edges.append(('retreat','living','визуално/акустично разделяне','Уединение и общуване'))
    if hits('F.03','без пряка видимост'):edges.append(('bed','living','без пряка видимост','F.03'))
    gross_min=sum(r['area_range_m2'][0] for r in rooms);gross_max=sum(r['area_range_m2'][1] for r in rooms)
    # These are provisional room allocation envelopes, NOT calculated RZP.
    warnings=['Диапазоните са ориентировъчни площи на функционални зони, не нормативни минимуми или изчислена РЗП.','Някои зони могат да се припокриват; не сумирайте автоматично като обща площ на сградата.']
    missing=[]
    for field,label in [('site_area','площ на имота'),('target_area','целева РЗП'),('budget','бюджет'),('site_orientation','ориентация и достъп'),('site_constraints','теренни и нормативни ограничения')]:
        if not str(brief.get(field,'')).strip():missing.append(label)
    if len(completed)<len(residents):warnings.append('Има непопълнени профили; не се правят заключения за тези обитатели.')
    if len(completed)<2:warnings.append('Няма два попълнени профила за надеждно сравнение на съвместното обитаване.')
    target=None
    try:target=float(brief.get('target_area'))
    except (ValueError,TypeError):pass
    area_check={'target_area_m2':target,'sum_zone_min_m2':gross_min,'sum_zone_max_m2':gross_max,'status':'непроверено'}
    if target is not None:
        area_check['status']='необходима оптимизация' if target<gross_min else 'ориентировъчно съвместимо, без проверка на РЗП'
        if target<gross_min:warnings.append('Целевата РЗП е по-малка от сумата на минималните зони; прегледайте комбиниране на функции и действителната площ.')
    if missing:warnings.append('Липсва информация: '+', '.join(missing)+'.')
    return {'rooms':rooms,'outdoor':outdoor,'links':[{'from':a,'to':b,'relation':c,'reason':d} for a,b,c,d in edges], 'area_check':area_check,'warnings':warnings,'profile_count':len(residents),'completed_profiles':len(completed),'method':'Правила v0.4; предложенията не са чертеж или окончателно архитектурно задание.'}
