'''
For this challenge, you’ll write a program that creates a bar chart for
easy comparison of weekly expenditures.
'''

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
     num_categories=int(input('How many categories do you please? '))
     categories=[]
     expenses=[]
     for i in range(num_categories):
          cat=input('Enter a category: ')
          exp=float(input('Enter the cost: '))

          categories.append(cat)
          expenses.append(exp)
     create_bar_chart(expenses,categories)
