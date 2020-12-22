Yearly_investment = 420000
Rate = 0.3
n = int(input('Number of years: '))
Asset = 0
Wealth = []

print(' Years       Investment       Return       Asset')
for i in range(n):
  if i !=0:
    Yearly_investment = Yearly_investment + 60000
    #print(Yearly_investment)
    

  Asset = int(Asset + Yearly_investment + (Asset + Yearly_investment)*Rate)

  Wealth.append(Asset)



  if i == 0:
    print(f'   {i+1}          {Yearly_investment}         {int(( Yearly_investment)*Rate)}        {Wealth[i]}')
  else:
    print(f'   {i+1}          {Yearly_investment}         {int((Wealth[i-1]+Yearly_investment)*Rate)}       {Wealth[i]}')


#print(Wealth)

  


  
  




