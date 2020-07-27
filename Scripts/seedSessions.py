import requests

sessions = [
    {
    "title": "Sesión Técnica Maquetación de un sitio web [C2/C3] - Básico",
    "description": "Se ve como realizar la maquetación básica de un sitio web"
  },
  {
    "title": "Sesión Técnica Tipados: weak, strong, static, dynamic [C2/C3]",
    "description": "Se ve los tipos de tipado en los lenguajes de programación"
  },
  {
    "title": "Sesión Técnica CI/CD con Gitlab  [C2/C3] - Intermedio",
    "description": "Como aplicar CI/CD usando las herramientas de Gitlab"
  },
  {
    "title": "Sesión Técnica Floating point numbers in depth [C2/C3] - Avanzado",
    "description": "Manejo de números decimales en binario"
  },
  {
    "title": "Sesión Técnica Manejo de conflictos [C1/C2/C3] - Básico",
    "description": "Como manejar conflictos y actuar de la manera ideal en estos"
  },
  {
    "title": "Sesión Técnica  Map y Filter - Intermedio",
    "description": "Como usar Map y Filter en sobre arreglos en Js"
  },
  {
    "title": "Sesión Técnica Google Colab & Jupyter Notebook [C2/C3] - Intermedio",
    "description": "Uso de Colab & Jupyter Notebook"
  },
  {
    "title": "Sesión Técnica Manipulando strings: built-in de Python [C2/C3]",
    "description": "Técnicas para manipular string aprovechando las herramientas de Python"
  },
  {
    "title": "Sesión Técnica Arrays & Dynamic Arrays [C1-C3] - Avanzado",
    "description": "Como functional los Arrays & Dynamic Arrays"
  },
  {
    "title": "Sesión Técnica Web Scraping con requests y Beautiful Soup [C2/C3] - Intermedio",
    "description": "Uso de Beautiful Soup y request para realizar web screaping con Python"
  },
  {
    "title": "Sesión Técnica Lambda Functions en Python [C2/C3] - Avanzado",
    "description": "Uso de Lambdas en Python"
  },
  {
    "title": "Sesión Técnica Medir objetivos [C1/C2/C3] - Básico",
    "description": "Medir correctamente los objetivos de manera óptima "
  },
  {
    "title": "Sesión Técnica Python Exceptions: try except & assert statements [C2/C3] - Intermedio",
    "description": "Control de errores en Python con try except"
  },
  {
    "title": "Sesión Técnica Computational Complexity [C1-C4] - Avanzado",
    "description": "Como calcular la complejidad de nuestros algoritmos"
  },
  {
    "title": "Sesión Técnica Closures y Scope en Python [C2/C3] - Intermedio",
    "description": "Como funciona el Closures y el Scope en Python"
  },
  {
    "title": "Sesión Técnica Decoradores en Python [C2/C3] - Intermedio",
    "description": "Uso de decoradores en Python "
  },
  {
    "title": "Sesión Técnica Como aportar al Open Source [C1-C4] - Básico",
    "description": "Como empezar a colaborar en el Open Source"
  },
  {
    "title": "Unit Testing con Python [C2/C3]",
    "description": "Realizar Unit Testing en Python"
  },
  {
    "title": "Sesión Técnica De números, operaciones y notaciones [C1-C4] - Intermedio",
    "description": "Introducción a matemáticas para computación"
  },
  {
    "title": "Sesión Técnica Comunicación Asertiva: Aprendiendo a hablar [C1-C4] - Básico",
    "description": "Como hablar de manera asertiva"
  },
  {
    "title": "Sesión Técnica Python: Iterators and Generators [C2-C3] - Intermedio",
    "description": "Como funcionan y para qué sirven los Iterators y Generators en Python"
  },
  {
    "title": "Sesión Técnica Manejo de expresiones regulares con Python [C2-C3] - Avanzado",
    "description": "Como aplicar las expresiones regulares en Python"
  },
  {
    "title": "Sesión Técnica 05 - Linked lists + First Coding Contest - Avanzado",
    "description": "Que son las Linked list"
  },
  {
    "title": "Sesión Técnica Logaritmos y la complejidad computacional - Intermedio",
    "description": "Introducción a la complejidad computacional"
  },
  {
    "title": "Sesión Técnica Crear un proyecto Open Source - Básico",
    "description": "Como iniciar un proyecto Open Source"
  },
  {
    "title": "Sesión Técnica 06 - Stacks and Queues + Coding Contest 02 - Avanzado",
    "description": "Que son las Stacks and Queues"
  },
  {
    "title": "Sesión Técnica Hash Tables [C1-C5] - Avanzado",
    "description": "Que son el hash tables"
  },
  {
    "title": "Sesión Técnica Representación gráfica de funciones y relaciones [C1-C5] - Intermedio",
    "description": "Tipos de gráficas y sus usos"
  },
  {
    "title": "Sesión Técnica Graph theory fundamentals [C1-C5] - Avanzado",
    "description": "Introducción a arboles binarios"
  },
  {
    "title": "08 - Binrary search trees",
    "description": "Que son los Binrary Search Trees"
  },
  {
    "title": "Lógica, Notación lógica",
    "description": "Que es y cómo se usa la notación lógica"
  },
  {
    "title": "08 - Binrary search trees (Solution to problems)",
    "description": "Ampliación Binrary Search Trees"
  },
  {
    "title": "08 - Binary Search Trees (solution to problems) [C1-C5]",
    "description": "Solución de los retos de Binrary Search Trees"
  },
  {    
    "title": "09 - Heaps [C1-C5]",
    "description": "Que son los Heaps"
  },
  {
    "title": "Integración de API con Alexa [C1-C5]",
    "description": "Como integran un API usando Alexa"
  }
]

def run():
  for session in sessions:
    requests.post('http://127.0.0.1:8000/sessions', json={
      "title": session['title'],
      "description": session['description']
    })

if __name__ == "__main__":
    run()