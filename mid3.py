# Task 1 from lesson 2
sentence = 'Thisisnotourfirstlesson'
a = []
for i in range(0, len(sentence), 2):  # index 0-dan başlayır, hər 2-ci simvolu götürür
    a.append(sentence[i:i+2])  # 2 simvolu alır (i-dən başlayaraq)
print(' '.join(a))  # Siyahını boşluqla birləşdirir və çap edir
