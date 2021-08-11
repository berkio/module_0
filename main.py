import numpy as np

def game_core_v3(number):
	predict = np.random.randint(1,101) # Для начала выбираем предсказанием любое число из диапазона
	min = 1 #устанавливаем минимальные и максимальные значения по границам диапазона
	max = 101
	count = 1
	while number != predict: #пока наше предсказание не равно загаданному числу
		count+=1 #увеличиваем число попыток
		if number > predict: #если загаданное число больше предсказания, то меньше этого предсказания нет смысла искать
			min = predict #устанавливаем минимальное значение диапазона равным предсказанию
			predict = round((max-min)/2) + min #предсказание берем посередине диапазона, округляем чтобы не получить float       
		elif number < predict: #если загаданное число меньше предсказания, то больше этого предсказания нет смысла искать
			max = predict #устанавливаем максимальное значение диапазона равным предсказанию
			predict = round((max-min)/2) + min #предсказание берем посередине диапазона, округляем чтобы не получить float 
	return(count) #возвращаем число попыток
def score_game(game_core):
	'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
	count_ls = []
	np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
	random_array = np.random.randint(1,101, size=(1000))
	for number in random_array:
		count_ls.append(game_core(number))
	score = int(np.mean(count_ls))
	print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
	return(score)
score_game(game_core_v3)