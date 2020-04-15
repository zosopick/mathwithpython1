import matplotlib.pyplot as plt
def create_bar_chart(data,labels):
     num_bars=len(data)
     positions=range(1,num_bars+1)
     plt.barh(positions,data,align='center')
     plt.yticks(positions,labels)
     plt.xlabel('Amount')
     plt.ylabel('Categories')
     plt.title('Weekly expenditures')
     plt.grid()
     plt.show()

if __name__=='__main__':
     n=int(input('Enter the number of categories: '))
     labels=[]
     expenditures=[]
     for i in range(n):
          category=input('Enter category: ')
          expenditure=float(input('Expenditure: '))

          labels.append(category)
          expenditures.append(expenditure)
     create_bar_chart(expenditures,labels)
