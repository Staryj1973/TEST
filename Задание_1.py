# Ваш код здесь
target_word = 'в'
target_chapter = 10
# Создаем список для словарей с tf по главам
list_tf_chapter =[]
# Разворачиваем список со словарями
for i in range(len(chapter_data)):
# Забираем словари с количеством употребления слова в каждой главе   
  word_count = chapter_words_count[i]
# Определяем количество слов в каждой главе  
  count_word_chapt = len(chapter_data[i])
# Создаем новый словарь со значениями tf для каждой главы
  dict_chapt_tf = {}
# Проходимся по каждому слову в главе и считаем для него tf и заносим в словарь  
  for word in word_count:
    tf = word_count[word] / count_word_chapt
    dict_chapt_tf[word] = tf
# Добавляем словарь в список tf по главам
    list_tf_chapter.append(dict_chapt_tf)
tf = list_tf_chapter[target_chapter].get(target_word)
print(f"tf для слова '{target_word}' в главе {target_chapter}: {tf}")
   