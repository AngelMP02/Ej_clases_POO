class Logger:
      def llamada():
    miCadenadeTexto = str(input("Escribe el mensaje:"))
    n=6
    m =str(n) 
    fichero = open("fichero.txt", 'w')
    fichero.write("--Start log--"+ "\n")
    for i in range(n):
      fichero.write(miCadenadeTexto + "\n")
    fichero.write("--End log: "+m+" log(s)")
    fichero.close()
    fichero=open("fichero.txt")
    print(fichero.read())
    
  print(llamada())
