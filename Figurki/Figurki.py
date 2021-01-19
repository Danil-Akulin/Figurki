
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(-8, 4, 1)  # x - массив np.array
y1 = x**2 + 4*x - 5  # парабола 
y2 = [9] * len(x)    # Прямая линия


plt.subplots()
plt.title("y = abs(x**2 + 4*x - 5)") # заголовок
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.tick_params(axis="x", direction="in",length=20, width=5,color="red",labelsize=10, labelrotation=20) # красная хуйня и кол столбов, цвет
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.xticks(np.arange(-8, 4, 1))
plt.grid(True)# Отображение сетки на координатной плоскости




plt.plot(x,y1 ,'--r',linewidth=5,label="Парабола")# График красного цвета
plt.plot(x,y2,'-.g',marker="d",label="Прямая линия")


plt.legend()
plt.text(-7, 24.5, "На диаграмме 2 графика:\nпарабола и линия экстремума")

plt.annotate(r"Экстремум функции = $\frac{-b}{2a} = \frac{-4}{2} = -2$", #-4 числитель 2 знаменатель
                xy=(-2, 9), xytext=(-5, 15),
                arrowprops=dict(facecolor="black", shrink=0.05))

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран


x = np.arange(-25,-10,1)
y2 = [1] * len(x)

plt.subplots()
plt.title("Кит")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="blue", alpha=.3, linewidth=6, linestyle=':')
plt.xticks(np.arange(-20, 15, 5))
plt.yticks(np.arange(-20,15,5))
plt.grid(True)

x = np.arange(0,9,1)
y1 = ((2/27)**2) - 3

x = np.arange(-10,0,1)
y3= (0.04)* x**2 - 3

x = np.arange(-9,-3,1)
y4 = (2/9) * ((x+6)**2) + 1

x = np.arange(-3,9,1)
y5= -1*(1/12)*((x-3)**2) + 6

x = np.arange(5,8,3)
y6 = (1/9)*((x-5)**2) +2

x = np.arange(5,8,5)
y7 = (1/8)*((x-7)**2) +1,5

x = np.arange(-13,-9,1)
y8 = -1*(0.75)*((x+11)**2) + 6

x = np.arange(-15,13,1)
y9 = -1*(0.5)*((x+13)**2)+3

#x = np.arange(-15,-10,1)
#y10 = [1] * len(x)

x = np.arange(3,4,1)
y11= [3] * len(x)


plt.show()


x = np.arange(-25,-10,1)
y2 = [1] * len(x)

plt.subplots()
plt.title("Очки")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="red", alpha=.3, linewidth=6, linestyle=':')
plt.xticks(np.arange(-10, 10, 2))
plt.yticks(np.arange(-10, 10, 2))
plt.grid(True)

x = np.arange(-9, -1, 1)
y1 = -(1/16)*((x+5)**2)+2

x = np.arange(1,9,1)
y3= (1/16)*((x-5)**2) + 2

x = np.arange(-9,-1,1)
y4 = (1/4)*((x+5)**2) - 3

x = np.arange(1,9,1)
y5= (1/4)*((x-5)**2) - 3

x = np.arange(-9, -6, 1)
y6 = (-(x+7)**2) + 5

x = np.arange(6,9,1)
y7 = (-(x-7)**2) + 5

x = np.arange(-1,1,1)
y8 = (-(0.5)**2) + 5

plt.show()


x = np.arange(-25,-10,1)
y2 = [1] * len(x)

plt.subplots()
plt.title("Зонтик")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="blue", alpha=.3, linewidth=6, linestyle=':')
plt.xticks(np.arange(-15, 15, 5))
plt.yticks(np.arange(-15, 15, 5))
plt.grid(True)

x = np.arange(-12, 12, 1)
y1 = (-(1/18)**2)+ 12

x = np.arange(-4,4,1)
y3= (-(1/8)**2) + 6

x = np.arange(-12,-4,1)
y4 = -(1/8)*((x+5)**2) - 3

x = np.arange(4,12,1)
y5= (1/4)*((x-8)**2) + 6

x = np.arange(-4, -0.3, 1)
y6 = 2*((x+3)**2) - 9

x = np.arange(-4, 0.2, 1)
y7 = 1.5*((x+3)**2) - 10

plt.show()