courses = {
    'python': {
        'nome': 'Python para Análise de Dados', 'duracao': 2.5
    }, 
    'sql': {
        'nome': 'SQL para Análise de Dados', 'duracao': 2
    }
}

current_course = courses['analista']
print(current_course)

# KeyError                                  Traceback (most recent call last)
# <ipython-input-21-19f376de48ff> in <cell line: 10>()
#       8 }
#       9 
# ---> 10 current_course = courses['analista']
#      11 print(current_course)

# KeyError: 'analista'
