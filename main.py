def mediana(nums1, nums2):
    logicali_laba013 = nums1 + nums2
    logicali_laba013.sort()
    withoutlogical = len(logicali_laba013)
    if withoutlogical % 2 == 0:
        mediana = (logicali_laba013[withoutlogical // 2 - 1] + logicali_laba013[withoutlogical // 2]) / 2
    else:
        mediana = logicali_laba013[withoutlogical // 2]
    return format(mediana, '.5f')

mediana(nums1,nums2)

#По двум отсортированным спискам чисел nums1 и nums2 размерами m и n элементов, вернуть медиану объединения этих двух списков.
#Общее время выполнения должно быть O(log (m+n)).
#Выполнить без использования numpy.
#Реализовать код в виде изолированной функции medians(nums1, nums2) в файле main.py, выложить в отдельный репозиторий, ссылку для клонирования репозитория приложить в ответ к заданию.
