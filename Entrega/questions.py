import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
score=0.0

#aqui tengo una lista con 3 ternas aleatorias compuestas de la siguiente manera (pregunta,posibles respuestas,respuesta correcta)    es decir(un string,una tupla(?,un integer)  !!!!!!!
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)

for question,answer,correct in questions_to_ask:
    
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answ in enumerate(answer):
        print(f"{i + 1}. {answ}")
    # El usuario tiene 2 intentos para responder correctamente int(input("Respuesta: ")) - 1
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        if (user_answer not in ["1","2","3","4"]):
            print("respuesta invalida")
            exit(1)
        user_answer=int(user_answer) - 1
        if user_answer ==correct:
            print("¡Correcto!")
            score=score+1
            break
        score=score-0.5
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es: ")
        print(answer[correct])
    # Se imprime un blanco al final de la pregunta
    print()
print(score)