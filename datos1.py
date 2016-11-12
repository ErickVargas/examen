import csv
import web

render = web.template.render('')

urls =('/(.*)','index'
      )

class index:
    def GET(self,resul):
        datos=[]
        with open("datosexamen.csv","r") as file:
            data=csv.reader(file,delimiter=",")
            for row in data:
                datos.append(row)

        #print datos

        numOcIn=[] 
        menor=[]
        mayor=[]               
        def estadomayor():
            for x in range(len(datos)):
                numOcIn.append(datos[x][2])
            numero = len(datos)
            i= 0
            while (i < numero):
                j = i
                while (j < numero):
                    if(int(numOcIn[i]) < int(numOcIn[j])):
                        temp = numOcIn[i]
                        numOcIn[i] = numOcIn[j]
                        numOcIn[j] = temp
                    j= j+1
                i=i+1
 
            for x in range(len(datos)):
                if datos[x][2]==numOcIn[0]:
                    mayor= datos [x]
            return mayor
        def estadoMenor():
            for x in range(len(datos)):
                numOcIn.append(datos[x][2])
            numero = len(datos)
            i= 0
            while (i < numero):
                j = i
                while (j < numero):
                    if(int(numOcIn[i]) > int(numOcIn[j])):
                        temp = numOcIn[i]
                        numOcIn[i] = numOcIn[j]
                        numOcIn[j] = temp
                    j= j+1
                i=i+1
 
        #print numOcIn[0]
    
            for x in range(len(datos)):
                if datos[x][2]==numOcIn[0]:
                    menor=datos [x]
            return menor
        
        
        resul=[estadomayor(),estadoMenor()]
        
        return render.index(resul)
 
if __name__ == '__main__':
     app = web.application(urls, globals())
     web.config.debug = True
     app.run()
