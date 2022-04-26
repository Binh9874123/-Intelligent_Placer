# Intelligent_Placer
Signal processing and interpretation
## Постановка задачи
Мы создаем Intelligent_Placer :  В соответствии с входным изображением изображение предмета и картинка нарисованы на 2-х белых листах бумаги, расположенных рядом. Нам нужно проверить, находится ли объект внутри данного нарисованного изображения

### Требование 
#### **К входным данным**

#### Требования к фотографии
1. Тип Фото : .png или .jpg.
2. Фон фото : белым листом.
3. Высота съемки: от 10 до 30 см
4. Угол наклона камеры: до 5 градусов
#### Требования к многоугольнику
1. Многоугольник должен быть задан замкнутым ломаным контуром, нарисованным темным маркером на белом листе бумаги, сфотографированной вместе с предметами.
2. Число вершин многоугольника : не больше 10.
3. Количество ребер многоугольника должно быть явно различимо

#### Требования к предмету
1. Границы всех предметов должны четко выделяться на фоне белого листа бумаги.
2. Предмет всегда на левая многоугольнику
3. Предметы не должны перекрывать друг друга
5. Нельзя повернуть предмет на каколй-либо угол, но можно поступательно двигать его.
8. Высота предмета не должны быть больше 3 см.
9. Один предмет может присутствовать на фото лишь 1 раз.
10. Предметы могут иметь разные ориентации/направление.
___
#### **К выходу**

- На основании результатов, записанных на имя и результатов, полученных машиной, мы определяем, является ли точность машины через ответ : jдин из двух ответов - "True"/"False", записанный в желаемый поток вывода (файл или консоль).
___

### Сбор данных
Файл Object и Input
### План решения
1. Найти граница 
   1. Преобразование изображения в оттенки серого с помощью cv2.cvtColor() 
   2. Размытие изображения с помощью cv2.GaussianBlur()
   3. Найдите ребра с помощью cv2.Canny()
   4. Используем метод fillhole для Раскрашивание предметов и фигур
2. Четко определите объект и фигуру и сравните, есть ли объект на картинке.
	1. После метода fillhole мы удалим ребра с площадью меньше 5 получим новый фото (внутри 2 фигур ) : всегда объект левая , фигур на права . Тогда легко мы определим 
	2. Найти минимальный прямоугольник обекта и фигура 
	3. найти в размерность фигура и обекта что максимум 
	4. Если размерность максимума - это фигур то True . Если нет то False
	
 
