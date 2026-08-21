"""
Magic methods-> sao metodos que usam duplo underscore, sao executados automaticamente sem necessidade de os chamar
"""

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):#retorna os valores
        return f'{self.title}  by {self.author}'

    def __eq__(self, other):#verifica se sao iguais
        return self.title == other.title and self.author ==other.author

    def __lt__(self,other):#verifica se primeiro e menor que o segundo(less than)
        return self.num_pages < other.num_pages

    def __gt__(self,other):#verifica se primeiro e maior que o segundo(greater than)
        return self.num_pages > other.num_pages

    def __add__(self,other):#adiciona
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self,keyword):#verifica se existe a palavra
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):#retorna os item na key
        if key =="title":
            return self.title
        elif key =="author":
           return self.author
        elif key== "num_pages":
            return self.num_pages
        else:
            return f"key{key} was not found"


book1=Book("The Hobbit","J.R.R Tolkien",310)
book2=Book("Harry Potter ","J.K.Rolling",223)
book3=Book("The Lion","C.S.Lewis",172)


print(book1)
print(book1==book2)
print(book2>book3)
print(book1+book2)
print("Rowling" in book2)
print(book2['audio'])
