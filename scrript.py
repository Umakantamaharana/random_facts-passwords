import randfacts,random,string
def choose(num):
    todo = { 1 : "The fact is : " + randfacts.getFact(), 2 : 'The password is : '+''.join((random.choice(string.ascii_letters+string.digits) for i in range (8)))}
    print(todo.get(num,"Choose \"1\" or \"2\"",))
choose(int(input("Choose to print a [1] random fact \n \t \t  [2] random password  \n>>> ")))
