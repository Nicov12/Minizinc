from tkinter import *
from PIL import ImageTk, Image
#LECTURA DEL TXT

datos2=[]

 

#FIN LECTURA DE TXT

#INICIO DE INTERFAZ

campo = Tk()
campo.title("Proyecto de Complejidad y Optimización")
campo.config(bg="#DCEBF5")
campo.geometry("1060x650")  #Width,Height

#raiz.iconbitmap("") #icono



def enviar():
    
    datos2 = ingresar.get('1.0','end')
 #   mostrar.insert('1.0',datos2) #Enviar datos a la ventana
    with open("ejemplo.txt","w") as file:
        file.write(datos2)
    #Abrir txt con el problema ingresado
    datos=[]
    datos3=[]
    z=[]
    with open("ejemplo.txt") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))
    #Abrir nuevo txt con la solucion
   # with open("solucion.txt","w") as file:
        
       # mostrar.insert('1.0',datos3)
        mostrar.insert('1.0',"var int: x; %Pos x\n")
        mostrar.insert('2.0',"var int: y; %Pos y\n")

        mostrar.insert('3.0',"%Restricciones triviales\n")
        mostrar.insert('4.0',"constraint x >= 0;\n")
        mostrar.insert('5.0',"constraint y >= 0;\n")

        mostrar.insert('6.0',"%Restricciones\n")
        mostrar.insert('7.0',"constraint x <= "+datos[0]+";\n")
        mostrar.insert('8.0',"constraint y <= "+datos[0]+";\n")
        a=0
        for i in range(2,len(datos)):
            if(datos[i][len(datos[i])-2]==" "):
                if(datos[i][len(datos[i])-4]==" "):
                    z.append("abs(" + datos[i][len(datos[i])-3] + " - x) + abs(" + datos[i][len(datos[i])-1] + " - y)")
                    mostrar.insert(str(i+7)+'.0',"constraint abs(" + datos[i][len(datos[i])-3] +" - x) + abs(" + datos[i][len(datos[i])-1] + " - y) > 0;\n")
                else:
                    z.append("abs(" + datos[i][len(datos[i])-4] + datos[i][len(datos[i])-3] + " - x) + abs(" + datos[i][len(datos[i])-1] + " - y)")
                    mostrar.insert(str(i+7)+'.0',"constraint abs(" + datos[i][len(datos[i])-4] + datos[i][len(datos[i])-3] +" - x) + abs(" + datos[i][len(datos[i])-1] + " - y) > 0;\n")
            else:
                if(datos[i][len(datos[i])-5]==" "):
                    z.append("abs(" + datos[i][len(datos[i])-4] + " - x) + abs(" + datos[i][len(datos[i])-2] + datos[i][len(datos[i])-1] + " - y)")
                    mostrar.insert(str(i+7)+'.0',"constraint abs(" + datos[i][len(datos[i])-4] +" - x) + abs(" + datos[i][len(datos[i])-2] + datos[i][len(datos[i])-1] + " - y) > 0;\n")
                else:
                    z.append("abs(" + datos[i][len(datos[i])-5] + datos[i][len(datos[i])-4] + " - x) + abs(" + datos[i][len(datos[i])-2] + datos[i][len(datos[i])-1] + " - y)")
                    mostrar.insert(str(i+7)+'.0',"constraint abs(" + datos[i][len(datos[i])-5] + datos[i][len(datos[i])-4] +" - x) + abs(" + datos[i][len(datos[i])-2] + datos[i][len(datos[i])-1] + " - y) > 0;\n")
            a =i+7
        
        mostrar.insert(str(a+1)+'.0',"solve minimize ")
        b=a+1

        for i in range(0,len(z)):
            if i==(len(z)-1):
                mostrar.insert(str(i+(b+1))+'.0',z[i]+";\n")
                
            else:
                mostrar.insert(str(i+(b+1))+'.0',z[i]+" + ")
            b = i+b
            print(b) 

        mostrar.insert(str(b+1)+'.0','output["Pos x: ", show(x), " Pos y: ", show(y)];')

    #Lectura del txt con la solucion
    with open("solucion.txt") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos3.append(linea.strip('\n'))
    
    



ingresar = Text(campo, bg='#F5EDF2')
ingresar.place(x=110,y=80, width=200, height=180)

boton1 = Button(campo, text="Resolver", command=enviar, bg="#DDDFF3")
boton1.place(x=110,y=285, width=200, height=30)

imagen = Image.open("ejemplo.jpg")
render = ImageTk.PhotoImage(imagen)
img = Label(campo, image=render)
img.place(x=10, y=400)

texto = Label(campo, text="EJEMPLO DE ENTRADA", font= "black" )
texto.place(x=110, y=370, width= 200)

texto2 = Label(campo, text="CÓDIGO MINIZINC", font= "black", bg='#CAF4F4')
texto2.place(x=420, y=10, width= 600)

mostrar = Text(campo, bg='#CAF4F4')
mostrar.place(x=420,y=45, width=600, height=550)
text_content = ingresar.get('2.0','3.0')
#mostrar.insert('1.0',text_content)
campo.mainloop()

#FIN INICIO INTERFAZ