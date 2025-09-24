# python_labs
## Лаба №1
### Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Картинка 1](./images/lab01/01.png)

### Задание 2
```python
a = float(input("a: "))
b = float(input("b: "))
print(f"sum={a+b:.2f}; avg={(a+b)/2:.2f}")
```
![Картинка 2](./images/lab01/02.png)

### Задание 3
```python
price, discount, vat = map(float, input("Введите price (руб.), discount (%), vat (%) через запятую: ").split(","))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![Картинка 3](./images/lab01/03.png)

### Задание 4
```python
m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```
![Картинка 4](./images/lab01/04.png)

### Задание 5
```python
m = list(input("ФИО: ").split())
print(f"Инициалы: {m[0][0]+m[1][0]+m[2][0]}.")
print(f"Длина (символов): {len(m[0])+len(m[1])+len(m[2]) + 2}")
```
![Картинка 5](./images/lab01/05.png)
